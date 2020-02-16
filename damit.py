import os
import shutil

client_name = input('Client name (case sensitive): ')
project_name = input('Project name: ')

cwd = os.getcwd()
old_path = os.path.join(cwd, '11 Profession/File Tree/')
new_path = os.path.join(cwd, client_name, project_name)

shutil.copytree(old_path, new_path)
