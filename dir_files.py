import os 
import urllib

this_dir_has_file = os.listdir('e:\python\selenium\gonna_test')
for file_name in this_dir_has_file:
	f = open('e:\python\selenium\gonna_test\%s' %file_name)
	lines = f.readlines()

	for i in range(len(lines)/2):
		check_url = urllib.quote(lines[2 * i].strip('\n'))

		check_url_name = lines[2 * i + 1].strip('\n')

		print check_url, check_url_name