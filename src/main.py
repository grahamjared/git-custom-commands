import register

git_command_name    = input("enter the desired custom name: ")
filepath_script     = input("enter the filepath of the python script you want to call through git\n(e.g. C:/Scripts/destroy_repo.py): ")
filepath_repository = input("git repo filepath, where one might find a .git folder.\n(e.g. C:/repositories/myproject): ")


register.command(git_command_name, filepath_script, filepath_repository)
