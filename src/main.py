import sys
from git import Repo

git_command_name = input("enter the desired custom name: ")
filepath_script  = input("enter the filepath of the python script you want to call through git\n(e.g. C:/Scripts/destroy_repo.py): ")
filepath_repo    = input("git repo filepath, where one might find a .git folder.\n(e.g. C:/repositories/myproject): ")
filepath_python  = sys.executable

# get repo
repo = Repo(filepath_repo)
git  = repo.git

# what we're doing in git terms:
#
# git config alias.git_command_name '!"<filepath_python>" "<filepath_script>"'
#
# english:
#
# Create a .bat script 'in place' with the alias to call a python script.
# The python script can then run any amount of git commands or do whatever
# it wants.

string_alias_name = 'alias.' + git_command_name
string_batch_script = '!"' + filepath_python + '" "' + filepath_script + '"'

result = git.execute(['git', 'config', string_alias_name, string_batch_script])
print(result)
