# WIX2005 algo-assignment

## Preparation
Install latest version of Python 3 at https://www.python.org/downloads/ and Git at https://git-scm.com/download/win

You may use any python IDE to run, I recommend VS Code and PyCharm.

### To clone this repository:
```
git clone git@github.com:chenghui-lee/algo-assignment.git
cd algo-assignment/
```
### (Optional) Create new virtual enviroment:
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

## Usage
In order to run this program, you must have a Google Console API key, which can be created at [here](https://console.cloud.google.com/apis/credentials).

Make sure to Enable the following services in Google Consolde:

- Distance Matrix API
- Geolocation API
- Maps JavaScript API

And may replace the API key in the following files:
```
6-th lines in Q1/q3_1.py
47-th lines in Q1/q3_2.py
```

Detailed implementation and proof can be shown by running the Python files in each Problem folder respectively.

For main program, you may use the following command to run.

```
python Q3/q3.py
```

