import register
from pathlib import Path as pathlib_Path

filepath_repository = input("git repo filepath, where one might find a .git folder.\n(e.g. C:/repositories/myproject): ")
def get_valid_python_script():

    while True:
        # do (get file)
        filepath = input("enter the filepath of the python script you want to call through git\n(e.g. C:/Scripts/destroy_repo.py): ")
        # while (file is not real python script)
        if (pathlib_Path(filepath).suffix != '.py' and not pathlib_Path(filepath).exists):
            continue
        else:
            break

    return filepath

name                = input("enter the desired custom name: ")
filepath_script     = get_valid_python_script()

register.command(name, filepath_script)
