import os

def print_files(path):
    os.chdir(path)
    files_list = os.listdir()
    for file in files_list:
        if os.path.isfile(file):
            print(file)
        elif os.path.isdir(file):
            print_files(file)
