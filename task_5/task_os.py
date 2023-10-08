import os

# print(os.name)
# print(os.environ)
# print(os.getpid())
# print(os.getcwd())

# os.path.exists('name_dir_new')
#
# os.mkdir('name_dir_new')
#
# os.rename('name_dir_new', 'name_dir_new_2')


def create_folder(folder_name: str):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


create_folder('my_new_dir')
