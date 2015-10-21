# coding:utf-8

import codecs

class read_file_get_thing(object):

	def __init__(self, file_path=None):
		self.dic = {}
		self.f = codecs.open(file_path, 'r', 'utf-8')
		self.lines = self.f.readlines()
		self.origin_id = [self.lines[2 * i].strip('\n') for i in range(len(self.lines) / 2)]
		self.origin_name = [self.lines[2 *i + 1].strip('\n') for i in range(len(self.lines) /2 )]

	def get_ya(self):
		for i in range(len(self.origin_id)):
			self.dic[self.origin_id[i]] = self.origin_name[i]
		return self.dic
		self.f.close()
