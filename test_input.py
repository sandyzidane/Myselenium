f = open('E:\python\selenium\\testfile')
line = f.readlines()
for i in range(0,5):
	print line[2 * i]
	print line[2 * i + 1]