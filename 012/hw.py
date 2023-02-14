# if "needs_sorting" has something, move files to right folders, create folders if needed

import os
import shutil

os.chdir('../')
print(os.getcwd())  # /Users/olganikitina/PycharmProjects/pythonProject
info = os.walk('/Users/olganikitina/PycharmProjects/pythonProject')
print(info)
if os.path.isdir('/Users/olganikitina/PycharmProjects/pythonProject/012/001music') == False:
    os.mkdir('/Users/olganikitina/PycharmProjects/pythonProject/012/001music')
if os.path.isdir('/Users/olganikitina/PycharmProjects/pythonProject/012/002pictures') ==False:
    os.mkdir('/Users/olganikitina/PycharmProjects/pythonProject/012/002pictures')
if os.path.isdir('/Users/olganikitina/PycharmProjects/pythonProject/012/003text_files') == False:
    os.mkdir('/Users/olganikitina/PycharmProjects/pythonProject/012/003text_files')
files = os.listdir('/Users/olganikitina/PycharmProjects/pythonProject/012/needs_sorting')

for filenames in files:
#     if '.mp3' in filenames:
#         source = r'/Users/olganikitina/PycharmProjects/pythonProject/012/needs_sorting'
#         destination = r'/Users/olganikitina/PycharmProjects/pythonProject/012/001music'
#         shutil.move(source, destination)


    # if '.jpg' in filenames:
    #     file_path = '/Users/olganikitina/PycharmProjects/pythonProject/012/002pictures'


# print(os.path.splitext('needs_sorting'))
# # for filenames in info:
# #     if '.jpg' in filenames:
# #