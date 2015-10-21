# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import shutil
import os
import read_file_is_good as r
import json

# test_page = "http://219.223.190.240:8081/test/"



hf_tst_page = u'http://121.15.171.116:8081/wap/sharenews.do?newsId='
testfile_dir = u'e:\python\selenium\gonna_test\\'  # 待测试文件所在文件夹
this_dir_has_file = os.listdir(testfile_dir)  # 列出待测文件夹中的所有文件
gonna_save_pic_dir = u'e:\python\selenium\gogogo\\'  # 将要用来保存截图的文件夹

driver = webdriver.Firefox()  # 初始化webdriver

for file_name in this_dir_has_file:  # 遍历所有文件

	want = r.read_file_get_thing(testfile_dir + file_name)
	want.get_ya()


	for want_id in want.origin_id:

		final_test_url = hf_tst_page + want_id + u'&uid=1788'  # 拼接待测链接为浏览器可识别的url格式
		saved_file_name = want.dic[want_id] + '.png'  # 给待测链接截图命名
		new_directory = os.path.join(gonna_save_pic_dir, file_name + "\\")  # 根据测试文件名创建新文件夹

		if not os.path.exists(new_directory):
			os.makedirs(new_directory)

		print testfile_dir + file_name




		# time.sleep(1)
		# input_box = driver.find_element_by_id("url")
		# input_box.send_keys(check_url)
		# driver.find_element_by_xpath("/html/body/form/input[2]").click()
		# time.sleep(3)

		# switch_to_another_windows()
		# driver.execute_script('''
		#	var q=document.documentElement.scrollTop = 10000
		#	''')
		# print check_url_name, check_url


		driver.get(final_test_url)  # 打开测试链接
		driver.get_screenshot_as_file(saved_file_name)  # 测试接口处理过后截图
		if saved_file_name  in os.listdir(new_directory):
			os.remove(new_directory + saved_file_name)
		else:
			shutil.move(saved_file_name, new_directory)  # 移动文件到新文件夹中

		driver.get(origin_url)
		driver.get_screenshot_as_file(check_url_name + '-1.png')  # 原网页截图
		if (check_url_name + '-1.png') in os.listdir(new_directory):
			os.remove(check_url_name + '-1.png')
		else:
			shutil.move(check_url_name + '-1.png', new_directory)

	f.close()
	if (file_name) in os.listdir(u'e:\python\selenium\\already_tested'):
		os.remove(u'e:\python\selenium\\already_tested\\' + file_name)
		shutil.move(testfile_dir + file_name, u'e:\python\selenium\\already_tested')
	else:
		shutil.move(testfile_dir + file_name, u'e:\python\selenium\\already_tested')

driver.quit()  # 退出webdriver
