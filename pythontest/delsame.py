import os
fileList = []
rootdir = "D:\pip-8.1.2"
for root,subFolders,files in os.walk(rootdir):
    if 'pip' in subFolders:subFolders.remove('pip')
    for file in files:
        if file.find(".py") != -1:
            file_dir_path = os.path.join(root,file)
            fileList.append(file_dir_path)
            print  file_dir_path