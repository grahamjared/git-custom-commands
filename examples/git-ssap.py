import os
from git import Repo
from git import GitCommandError

# NAME:
#   ssap A.K.A. save-staged-as-patch
#
# PURPOSE:
#   This custom git command used in junction with `git-custom-commands` will 
#   save all staged changes as a patch and then discard them.
#
#   This script is meant to leave unstaged changes unstaged and unchanged,
#   however occaisonally git does not allow them to be reapplied, in this
#   case they will still remain as a patch.

# get repo
# If the user is running 'git-custom-commands', and
# executes this from the git command prompt,  then
# their current working directory will likely be their
# repository.

filepath = os.getcwd();
try:
    repo = Repo(filepath)
except:
    while True:
    # do (get filepath)
        filepath = input("Could not get repository from the current working directory/ entered path.\nPlease enter the filepath where a git repository resides.\n(e.g. C:/repositories/my-git-repo): ")
    # while (cannot open repo)
        try:
            repo = Repo(filepath)
        except:
            continue
        break

# what is being done in plain git terms:
#
# git diff --staged --relative > staged.patch
# git diff > unstaged.patch
# git reset --hard
# git apply unstaged.patch

diff_staged   = repo.git.execute(["git", "diff", "--cached", "--relative"])
diff_unstaged = repo.git.execute(["git", "diff"])

# open
suffix = ".patch"
path_staged = os.path.join(filepath, "staged" + suffix)
path_unstaged = os.path.join(filepath, "unstaged" + suffix)
file_staged   = open(path_staged,   "w")
file_unstaged = open(path_unstaged, "w")

# write
file_staged.write(diff_staged)
file_staged.write("\n") # add newline manually
file_unstaged.write(diff_unstaged)
file_unstaged.write("\n") # add newline manually

# close
file_staged.close()
file_unstaged.close()

# reset
repo.git.execute(["git", "reset", "--hard"])

# TODO: APPLY WITH 'git apply --whitespace=fix my.patch' to avoid more errors

# apply unstaged
try:
    result = repo.git.execute(["git", "apply", "--reject", "--whitespace=fix", path_unstaged])
    print("result: ", result)
except GitCommandError as e:
    print(e)
    print("\nError: 'unstaged.patch' could not apply, it will NOT be deleted.")
    print("    'unstaged.patch' likely relies on changes made in 'staged.patch'.")
    print("    apply 'staged.patch' first then 'unstaged.patch' to solve.\n")
else:
    # delete unstaged if no error
    os.remove(file_unstaged.name)
