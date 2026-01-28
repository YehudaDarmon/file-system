import os

def move_between_folders(path):
    Current_location = os.getcwd()
    os.chdir(path)
    print(os.listdir())
    os.chdir(Current_location)
