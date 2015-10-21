from selenium import webdriver
import time

url = "http://36kr.com/p/5038220.html?ref=head_line_one"
driver = webdriver.Firefox()
#driver.maximize_window()
driver.get(url)
time.sleep(3)


driver.execute_script('''
	var q = document.documentElement.scrollTop = 10000
	''')
time.sleep(3)

url_name = "5038220"
driver.save_screenshot(url_name + '.png')
driver.close()