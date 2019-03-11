#coding = utf-8
import requests
from bs4 import BeautifulSoup
import pymongo
import time

MONGO_URL = 'localhost'
MONGO_DB = 'Hose'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_response(url):#请求函数体
	reponse=requests.get(url)#进行请求
	time.sleep(3)
	reponse.encoding='gb18030'#解码
	return reponse.text#获得响应体

url='https://sz.esf.fang.com/housing/__1_0_0_0_1_0_0_0/'
html=get_response(url)#获取各区响应，希望得到区域名称和全部区域部分url
soup=BeautifulSoup(html,'html.parser')#解析响应体
results=soup.select('div.qxName > a')#获得全部区域对应的部分url
other_area=['不限','东莞','惠州','深圳周边']#需要去掉地区列表
for result in results:
	if result.string.strip() not in other_area:#去掉其他区域
		#yield (result.string,result['href'])
		print(result.string)#打印各区名
		district_url='https://sz.esf.fang.com'+result['href']#目标区域第一页完整url拼接
		#print(district_url)#打印各区第一页完整url
		html = get_response(district_url)#获取各区响应，希望得到总页数
		soup = BeautifulSoup(html,'html.parser')#解析响应体
		page = int(soup.select('.fanye .txt')[0].string[1:][:-1])#获取各区域总页数
		for pn in range(1,page+1):#各区网页信息翻页
			base_url = district_url[:-8]+str(pn)+'_0_0_0/'#每页完整url拼接
			#print(base_url)#打印各区每页完整rul
			html = get_response(base_url)#获取每页响应，希望得到感兴趣信息
			soup = BeautifulSoup(html,'html.parser')#解析响应体
			results = soup.select('div.list')#提取有效信息部分
			for result in results:
				half = len(result.select('.dj .half'))#统计差半分的数量
				no2 = len(result.select('.dj .no2'))#统计差多少个1分的数量
				try:
					info = {
						'name':result.select('dd > p > a')[0].string,#小区名
						'url':result.select('dd > p > a')[0].attrs['href'],#小区rul
						'score':5-half*0.5 - no2*1,#评分
						'address':result.select('dd p')[-1].get_text().strip(),#地址
						'year':result.select('dd ul li')[-1].get_text().replace('年建成','').strip()}#年建成
					price = result.select('.priceAverage span')[0].get_text().strip()#获取价格
					info['price']=price#将价格写入info
				except IndexError:
					info['price']=''#处理无价格报错
				#print(info)#打印info测试
				if db['Fangtianxia'].update_one({'name':info['name']},{'$set':info},True):#通过update将数据保存到mongodb
					print('保存成功',info)#打印保存状态
				else:
					print('保存失败',info)
-----------liange--------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pymongo
import time

MONGO_URL = 'localhost'
MONGO_DB = 'Hose'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_info(info):
    '''
    保存信息
    :param info:
    :return:
    '''
    if db['Fangtianxia'].update_one({'url':info['url']},{'$set':info},True):
        print('保存成功',info)
    else:
        print('保存失败', info)

def get_response(url):
    '''
    进行请求
    :param url:
    :return:
    '''
    reponse=requests.get(url)
    time.sleep(1)
    reponse.encoding='gb18030'
    return reponse.text

def get_district(url):
    '''
    获取每个区域对应的url
    :param url:
    :return:
    '''
    html=get_response(url)#获得响应
    soup = BeautifulSoup(html,'html.parser')
    results = soup.select('div.qxName > a')
    name_url={}
    other_area=['不限','东莞','惠州','深圳周边']
    for result in results:
        if result.string.strip() not in other_area:
            yield (result.string,result['href'])

def get_page(district_url):
    '''
    获取每个区域的页码
    :param district_url:
    :return:
    '''
    html = get_response(district_url)
    soup = BeautifulSoup(html, 'html.parser')
    page=int(soup.select('.fanye .txt')[0].string[1:][:-1])
    return page

def get_info(base_url):
    '''
    提取信息
    :param base_url:
    :return:
    '''
    html = get_response(base_url)#获得响应
    soup = BeautifulSoup(html,'html.parser')
    results=soup.select('div.list')
    for result in results:
        half = len(result.select('.dj .half'))
        no2 = len(result.select('.dj .no2'))
        try:
            info={
                'name':result.select('dd > p > a')[0].string,
                'url':result.select('dd > p > a')[0].attrs['href'],
                'score':5-half*0.5 - no2*1,
                'address':result.select('dd p')[-1].get_text().strip(),
                'year':result.select('dd ul li')[-1].get_text().replace('年建成','').strip()
            }
            price = result.select('.priceAverage span')[0].get_text().strip()
            info['price']=price
        except IndexError:
            info['price']=''
        save_info(info)

#主体函数
def main():
    url='https://sz.esf.fang.com/housing/__1_0_0_0_1_0_0_0/'
    district_urls=get_district(url)#获取每个区域对应的url
    for district,district_url in district_urls:
        print(district)
        district_url='https://sz.esf.fang.com'+district_url
        page=get_page(district_url)#获取对应区域的页码
        for pn in range(1,page+1):#翻页
            base_url=district_url[:-8]+str(pn)+'_0_0_0/'
            get_info(base_url)#获取信息


if __name__ =='__main__':
    main()
