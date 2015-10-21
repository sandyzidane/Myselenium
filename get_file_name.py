
import os

file_name = os.path.basename('''E:\python\selenium\\testfile''')
print file_name
new_dir = 'E:\python\selenium\%s' %(file_name)
print new_dir
