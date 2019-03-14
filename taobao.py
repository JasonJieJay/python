------------getcookies.py-----------------------------------------------------------------------------
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pickle
import time
import re
from bs4 import BeautifulSoup

KEYWORD = '美食'

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def get_search():
	browser.get('https://www.taobao.com/')
	browser.delete_all_cookies()
	input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
	button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
	input.send_keys(KEYWORD)
	button.click()
	time.sleep(10)
	cookies=browser.get_cookies()
	with open('cookies.dat','wb') as f:
		pickle.dump(cookies,f)
	
#主题函数
def main():
	get_search()
	browser.close()
if __name__=='__main__':
	main()
----------taobao.py------------------------------------------------------------------------------
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pickle
import time
import re
from bs4 import BeautifulSoup
import pymongo
import random
KEYWORD = '荣耀'#搜索的关键字，mongodb保存的文件名
browser = webdriver.Chrome()#声明浏览器
wait = WebDriverWait(browser,10)#加载等待10秒钟
MONGO_URL = 'localhost'
MONGO_DB = 'Taobao'
client = pymongo.MongoClient(MONGO_URL)#启动mongo客户端
db = client[MONGO_DB]#数据库名字
def save_info(info):
	if db[KEYWORD].update_one({'href':info['href']},{'$set':info},True):#通过update保存数据到mongo
		print('保存成功',info)#打印保存状态
def get_search():#获取第一页响应
	browser.get('https://www.taobao.com/')#获得响应
	browser.delete_all_cookies()#清空cookies 准备登录
	with open('cookies.dat','rb') as f:#打开之前登录获取的cookies文件
		cookies = pickle.load(f)#读取二进制文件
	for cookie in cookies:#遍历出cookie
		browser.add_cookie(cookie)#将cookies写入登录淘宝帐号
	try:
		input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))#定位搜索输入框的节点
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))#定位搜索按钮的节点
		input.send_keys(KEYWORD)#输入搜索的KEYWORD
		button.click()#点击进行搜索
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))#确认搜索页的产品列表加载成功
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),'1'))#确认搜索第1页加载是否成功匹配高亮度页码
		get_info(browser.page_source)#进入下一步信息保存
		page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text#获得总页数
		page = int(re.search(r'(\d+)',page).group(1))#用正则表达式获得总页数的数字
		return page#返回总页数
	except TimeoutException:#抓取timeout报错后重新执行get_search()
		return get_search()
def get_next(pn):#翻页功能执行
	try:
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))#定位页码输入框
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))#定位翻页确认按钮
		#browser.execute_script('window.scrollTo(0,10000)')#网页拉到最底
		secs = random.randint(5,60)#随机等待时间生成
		print('请等待<<'+str(secs)+'秒>>后翻页')#打印生成的时间
		time.sleep(secs)#执行sleep的时间
		input.clear()#清空页码输入框
		input.send_keys(pn)#写入翻页页码
		button.click()#按确认按钮进行翻页
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))#确认翻页后的产品列表加载成功
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(pn)))#确认翻页加载是否成功匹配高亮度页码
		get_info(browser.page_source)#进入下一步信息保存操作
	except TimeoutException:#抓取timeout报错后重新执行get_next()
		get_next(pn)
def get_info(html):#提取感兴趣信息
	soup = BeautifulSoup(html,'html.parser')#解析响应体
	results=soup.select('#mainsrp-itemlist > div > div > div.items > div.item')#提取有效部分
	for result in results:#遍历信息
		info={'price':result.select('.price strong')[0].get_text(),#价格
			'deal':result.select('.deal-cnt')[0].get_text(),#成交量
			'href':result.select('.title > a')[0].attrs['href'],#连接
			'name':result.select('.title > a')[0].get_text().strip(),#产品名字
			'shop':result.select('.shop > a')[0].get_text().strip(),#店铺
			'location':result.select('.location')[0].get_text()}#地址
		save_info(info)#保存信息
#主体函数
def main():
	page = get_search()#获取页码数
	pag = list(range(2,page+1))#通过总页数形成页码列表
	random.shuffle(pag)#随机打乱页码列表
	paged = [1]#爬完页码变量
	count = 1#翻页统计变量
	while 1:
		pn=pag.pop()#取得翻页页码
		#for pn in range(2,page+1):
		print('准备爬取第：'+str(pn)+'页')#打印将翻页页码
		print('准备第'+str(count)+'次翻页')#打印准备第几次翻页
		count += 1#统计翻页次数
		get_next(pn)#翻页函数
		paged.append(pn)#将爬完的页码记录下来
		print('已经爬完页码：'+str(paged))#打印爬完的页码
		if len(pag)==0:#判断是否爬完页数
			break
	browser.close()#关闭浏览器
if __name__=='__main__':
	main()
