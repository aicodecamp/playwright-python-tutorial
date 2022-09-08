

# getting started

```powershell
$ mkdir playwright-python-tutorial
$ cd playwright-python-tutorial

$ python3 -m venv venv

 venv\Scripts\activate.bat

# packages
pip3 install playwright
pip3 install pytest
pip3 install pytest-playwright

# install the dependencies
pip3 install -r requirements.txt

# check all installed packages
pip3 freeze

# install browser for play right
playwright install

# create test
$ mkdir tests
$ touch tests/test_search.py

# run test
$ python3 -m pytest tests
# pytest tests - will not add current directory to the python path

```