import register

filepath_script     = input("enter the filepath of the python script you want to call through git\n(e.g. C:/Scripts/destroy_repo.py): ")
filepath_repository = input("git repo filepath, where one might find a .git folder.\n(e.g. C:/repositories/myproject): ")


name                = input("enter the desired custom name: ")
register.command(name, filepath_script, filepath_repository)
