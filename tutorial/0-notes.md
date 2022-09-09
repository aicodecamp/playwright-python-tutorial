

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

# first step

* browser, 
* browser context, - lightweight browser instance, all test share one browser, but each test has its own browser context
* page, 

playwright call

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

```

pytest-playwright plugin has fixture : 
* browser, - session scope, all test will share one browser instance
* context, - function scope
* page - function scope

## navigating to a web page

```powershell
python3 -m pytest tests --headed --slowmo 1000

```


playwright selectors:
Text
CSS
XPath
N-th element
React
Vue
ID attributes

https://testautomationu.applitools.com/web-element-locator-strategies/

api:
* locator
* fill
* click
## assert
auto waiting
https://playwright.dev/python/docs/actionability

