# libs
import os, sys
cwd = os.getcwd()
os.chdir('src'); path_to_src = os.getcwd()
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from libs import *

# exp
def browser_testing(p: Playwright):
    browser = p.chromium.launch()
    page : Page = browser.new_page()

    page.goto(HOMEPAGE)

    print(page.title())

    browser.close()

if __name__ == '__main__':
    with sync_playwright() as p:
        browser_testing(p)