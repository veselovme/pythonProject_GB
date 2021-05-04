import os

project_name = 'my_project'
path_dir = [os.path.join(project_name, 'settings'),
            os.path.join(project_name, 'mainapp'),
            os.path.join(project_name, 'adminapp'),
            os.path.join(project_name, 'authapp')]


def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.makedirs(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')


for i in path_dir:
    make_dir(i)