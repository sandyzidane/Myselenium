# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import shutil
import os
import read_file_is_good as r
import json
# 测试服务器链接前半部分，通过文章ID来访问
hf_tst_page = u'http://121.15.171.116:8081/wap/sharenews.do?newsId='
# 待测试文件所在文件夹
testfile_dir = u'e:\\python\selenium\\gonna_test\\'
# 列出待测文件夹中的所有文件
this_dir_has_file = os.listdir(testfile_dir)
# 保存截图的文件夹
Jietu_dir = u'e:\\python\\selenium\\gogogo\\'

driver = webdriver.Firefox()  # 初始化driver

for file_name in this_dir_has_file:  # 遍历所有文件

	want = r.read_file_get_thing(testfile_dir + file_name)		# 打开一个待测文件

	for i_count in range(want.changdu):		# 对文件内的每个id，拼接为浏览器可访问的地址，每个名字用来命名截图

		final_test_url = hf_tst_page + want.good_get_id(i_count) + u'&uid=1788'  # 拼接
		saved_file_name = want.good_get_name(i_count) + '.png'  # 给待测链接截图命名
		new_directory = os.path.join(Jietu_dir, file_name + "\\")  # 根据测试文件名创建新文件夹

		if not os.path.exists(new_directory):
			os.makedirs(new_directory)

		print testfile_dir + file_name

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

	if (file_name) in os.listdir(u'e:\python\selenium\\already_tested'):
		os.remove(u'e:\python\selenium\\already_tested\\' + file_name)
		shutil.move(testfile_dir + file_name, u'e:\python\selenium\\already_tested')
	else:
		shutil.move(testfile_dir + file_name, u'e:\python\selenium\\already_tested')

driver.quit()
