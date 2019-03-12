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
KEYWORD = '美食'
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
MONGO_URL = 'localhost'
MONGO_DB = 'Taobao'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_info(info):
	if db[KEYWORD].update_one({'href':info['href']},{'$set':info},True):
		print('保存成功',info)
def get_search():
	browser.get('https://www.taobao.com/')
	browser.delete_all_cookies()
	with open('cookies.dat','rb') as f:
		cookies = pickle.load(f)
	for cookie in cookies:
		browser.add_cookie(cookie)
	try:
		input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
		input.send_keys(KEYWORD)
		button.click()
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),'1'))
		get_info(browser.page_source)
		page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text
		page = int(re.search(r'(\d+)',page).group(1))
		return page
	except TimeoutException:
		return get_search()
def get_next(pn):
	try:
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
		input.clear()
		input.send_keys(pn)
		button.click()
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(pn)))
		get_info(browser.page_source)
	except TimeoutException:
		get_next(pn)
def get_info(html):
	soup = BeautifulSoup(html,'html.parser')
	results=soup.select('#mainsrp-itemlist > div > div > div.items > div.item')
	for result in results:
		info={'price':result.select('.price strong')[0].get_text(),
			'deal':result.select('.deal-cnt')[0].get_text(),
			'href':result.select('.title > a')[0].attrs['href'],
			'name':result.select('.title > a')[0].get_text().strip(),
			'shop':result.select('.shop > a')[0].get_text().strip(),
			'location':result.select('.location')[0].get_text()}
		save_info(info)
#主体函数
def main():
	page = get_search()
	for pn in range(2,page+1):
		print(pn)
		time.sleep(5)
		get_next(pn)
	browser.close()
if __name__=='__main__':
	main()
