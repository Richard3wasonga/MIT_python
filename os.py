import os
from datetime import datetime

os.chdir('/home/row/Development/')

# makedirs can create folders that are a few level deep while mkdir only top level
# os.mkdir('test-folder')
# os.makedirs('test-folder/sub-Dir')

# os.rename('test-folder', 'test-file')

# remove dirs deletes multiple folders only if empty but rmdir only deletes leaf
# os.rmdir('test-folder/sub-Dir')
# os.removedirs('test-folder/sub-Dir')

# print(os.stat('bree-AI'))
# mod_time = os.stat('bree-AI').st_mtime
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('/home/row/Development/'):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# print(os.environ.get('HOME'))

# Avoid concatinating the path and string since you can forget slashes or add a double slash
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)\

#basename prints the file at the bottom, dirname prints the directory and split prints a tuple of both both
# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))

# print(os.path.exists('/tmp/test.txt'))
# isdir and isfile only works if the path exists
# print(os.path.isdir('/home/row/Development/KANGEMI-WEBSITE/school-backend/'))
# print(os.path.isfile('/home/row/Development/KANGEMI-WEBSITE/school-backend/static/style.css'))

#split the roort of the path and the extension
# print(os.path.splitext('/tmp/test.py'))

print(dir(os.path))

# print(os.getcwd())
# print(os.listdir())