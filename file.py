import os
import sys
from time import sleep

name = os.path.basename(sys.argv[0])
num = list(filter(lambda x: x.isdigit(), name))

name_num = name.find(num[0]) if num else name.find('.')

first_name, second_name = name[:name_num], name[name_num:name.find('.')]
second_name = str(int(second_name) + 1) if num else 1
new_name = f'{first_name}{second_name}.py'

if sys.platform == 'win32':
    path = os.path.abspath(os.curdir) + '\\'
    command = 'python'
else:
    path = os.path.abspath(os.curdir) + '/'
    command = 'python3'

now_file = open(path + name, 'r')
new_file = open(path + new_name, 'w+')

for line in now_file:
    new_file.write(line)
now_file.close(), new_file.close()

print(f'File {new_name} created')
sleep(1)

os.system(f'{command} {path + new_name}')

