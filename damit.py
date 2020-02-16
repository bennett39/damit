import os
import shutil

client_name = input('Client name (case sensitive): ')
project_name = input('Project name: ')

path = os.path.join(client_name, project_name)

shutil.copytree('old', path)
