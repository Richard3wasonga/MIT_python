# renaming files in the computer to a prefarable naming format
import os 

os.chdir('/home/row/Development/rowlytics_testing')

# print(os.getcwd())

# print(dir(os))

# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)
#     f_title, f_num = f_name.split('-')

#     f_title = f_title.strip()
#     f_num = f_num.strip()[1:].zfill(2)

#     new_name ='{}-{}{}'.format(f_num, f_title, f_ext)

#     os.rename(f, new_name)

# from this format

# logo - #2.png
# logo - #4.png
# card - #7.png
# logo - #5.png
# logo - #1.png
# logo - #6.png
# logo - #3.png

# to this format

# 02-logo.png
# 04-logo.png
# 07-card.png
# 05-logo.png
# 01-logo.png
# 06-logo.png
# 03-logo.png