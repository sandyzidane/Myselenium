# coding:utf-8

import codecs

class read_file_get_thing(object):

	def __init__(self, file_path=None):

		self.f = codecs.open(file_path, 'r', 'utf-8')
		self.lines = self.f.readlines()
		self.changdu = len(self.lines) / 3
		self.origin_url = [self.lines[3 * i].strip('\n') for i in range (self.changdu)]
		self.origin_id = [self.lines[3 * i + 1].strip('\n') for i in range(self.changdu)]
		self.origin_name = [self.lines[3 *i + 2].strip('\n') for i in range(self.changdu)]
		self.f.close()

	def good_get_id(self, i):
		return self.origin_id[i]

	def good_get_name(self, i):
		return self.origin_name[i]

	def good_get_url(self, i):
		return self.origin_url[i]



if __name__ == '__main__':
	a = read_file_get_thing('/home/sandy/PycharmProjects/goodtest')
	for i in range(a.changdu):
		print a.good_get_url(i)
		print a.good_get_id(i)
		print a.good_get_name(i)