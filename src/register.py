import sys
from git import Repo

# what we're doing in git terms:
#
# git config alias.git_command_name '!"<filepath_python>" "<filepath_script>"'
#
# english:
#
# Create a .bat script 'in place' with the alias to call a python script.
# The python script can then run any amount of git commands or do whatever
# it wants.

def command(name, filepath_python_script, filepath_repository):
    CONST_BATCH_SCRIPT = '!"' + sys.executable + '" "' + filepath_python_script + '"'
    # get repo
    repo = Repo(filepath_repository)
    git  = repo.git
    git.execute(['git', 'config', 'alias.' + name, CONST_BATCH_SCRIPT])
def make_bat_script(filepath_py_script):
    return '!"' + sys.executable + '" "' + filepath_py_script + '"'

def make_str_alias(name):
    return 'alias.' + name
