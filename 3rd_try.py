# -*- coding:utf-8 -*-
import shutil
import os

from selenium import webdriver

import read_file_is_good as r

# 测试服务器链接前半部分，通过文章ID来访问
hf_tst_page = u'http://121.15.171.116:8081/wap/sharenews.do?newsId='
# 待测试文件所在文件夹
testfile_dir = u'e:\\python\selenium\\gonna_test\\'
# 列出待测文件夹中的所有文件
this_dir_has_file = os.listdir(testfile_dir)
# 保存截图的文件夹
Jietu_dir = u'e:\\python\\selenium\\gogogo\\'
# 初始化driver
driver = webdriver.Firefox()
# 遍历所有文件
for file_name in this_dir_has_file:
	# 打开一个待测文件
	want = r.read_file_get_thing(testfile_dir + file_name)
	# 对文件内的每个id，拼接为浏览器可访问的地址，每个名字用来命名截图
	for i_count in range(want.changdu):
		# 拼接url
		final_test_url = hf_tst_page + want.good_get_id(i_count) + u'&uid=1788'
		# 给待测链接截图命名
		saved_file_name = want.good_get_name(i_count) + '.png'  
		# 根据测试文件名创建新文件夹
		new_directory = os.path.join(Jietu_dir, file_name + "\\")
		# 获取原文url
		origin_url = want.good_get_url(i_count)
		# 截图文件夹内某个待测网站比如“壳壳网”不存在的话，就创建它
		# 如果存在的话，那么等下保存截图的时候就自动保存进去了
		if not os.path.exists(new_directory):
			os.makedirs(new_directory)
		
		# 打开测试链接
		driver.get(final_test_url)  
		# 测试接口处理过后的页面截图
		driver.get_screenshot_as_file(saved_file_name)
		# 如果要保存的截图名字已经在目录里面了，就先删除原文件再移进去
		if saved_file_name in os.listdir(new_directory):
			os.remove(new_directory + saved_file_name)
			shutil.move(saved_file_name, new_directory)
		else:
			shutil.move(saved_file_name, new_directory)  # 移动文件到新文件夹中
		# 打开原文网页
		driver.get(origin_url)
		# 原网页截图
		driver.get_screenshot_as_file(saved_file_name + '-1.png')
		if (saved_file_name + '-1.png') in os.listdir(new_directory):
			os.remove(new_directory + saved_file_name + '-1.png')
			shutil.move(saved_file_name + '-1.png', new_directory)
		else:
			shutil.move(saved_file_name + '-1.png', new_directory)
	# 测试完了之后，把待测的文件全部移动到“already_tested”文件夹去
	if file_name in os.listdir(u'e:\python\selenium\\already_tested'):
		os.remove(u'e:\python\selenium\\already_tested\\' + file_name)
		shutil.move(testfile_dir + file_name, u'e:\python\selenium\\already_tested')
	else:
		shutil.move(testfile_dir + file_name, u'e:\python\selenium\\already_tested')

driver.quit()
