import os
import shutil

project_dir = os.path.join(os.path.dirname(__file__), 'my_project')
templates_dir = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(templates_dir):
    os.makedirs(templates_dir)

for root, dirs, files in os.walk(project_dir):
    if root.count('templates'):
        for dir_ in dirs:
            if not os.path.exists(os.path.join(templates_dir, dir_)):
                os.makedirs(os.path.join(templates_dir, dir_))
        for file in files:
            project_file = os.path.join(root, file)
            templates_file = os.path.join(templates_dir, os.path.basename(root))
            if not os.path.dirname(project_file) == templates_file:
                shutil.copy(project_file, templates_file)