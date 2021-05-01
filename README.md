# WIX2005 algo-assignment

## Preparation
Install latest version of Python 3 at https://www.python.org/downloads/ and Git at https://git-scm.com/download/win

You may use any python IDE to run, I recommend VS Code and PyCharm.

### To clone this repository:
```
git clone git@github.com:chenghui-lee/algo-assignment.git
cd algo-assignment/
```
### (Optional, but recommended) Create new virtual enviroment:
```
pip3 install virtualenv
python -m virtualenv venv
venv\Scripts\activate.bat
```
### (Optional) To deactivate and remove virtual environment (i.e. After this course):
```
deactivate
rmdir venv /s
```

### Install dependency:
```
pip3 install -r requirements.txt
```

## Commit
You can open a new branch and pull request when commiting changes.
```
git branch branchName
git checkout branchName
{do your things}
git add .
git commit -m "Description about the changes you made"
git push origin HEAD:nameOfNewBranch
```
Then you can head over to github to open a new pull request.

## Update your code with Github's latest code base
```
git checkout main
git pull
```
