from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver1 = webdriver.Firefox()
driver2 = webdriver.Firefox()

for web in ('http://www.baidu.com/',  'http://www.sina.com.cn/'):
	print web
	driver1.get(web)
