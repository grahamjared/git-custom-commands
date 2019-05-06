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

def make_bat_script(filepath_py_script):
    return '!"' + sys.executable + '" "' + filepath_py_script + '"'

def make_str_alias(name):
    return 'alias.' + name

def command(name, filepath_script):
    CONST_BATCH_SCRIPT = make_bat_script(filepath_script)
    CONST_ALIAS_FULL   = make_str_alias(name)

    Repo().git.execute(['git', 'config', '--global', CONST_ALIAS_FULL, CONST_BATCH_SCRIPT])

def command_local(name, filepath_script, filepath_repository):
    CONST_BAT_SCRIPT   = make_bat_script(filepath_script)
    CONST_ALIAS_FULL   = make_str_alias(name)

    Repo(filepath_repository).git.execute(['git', 'config', CONST_ALIAS_FULL])

