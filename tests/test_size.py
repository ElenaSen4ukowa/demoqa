import time
from pages.demoqa import DemoQa

def test_size(browser):
    demo_qa_page = DemoQa(browser)               # объект страницы https://demoqa.com/
    demo_qa_page.visit()                         # переход на страницу https://demoqa.com/

    browser.set_window_size(1000, 300)           # установить размеры окна 1000х300
    time.sleep(5)
    browser.set_window_size(1000, 1000)          # вернуть размеры окна 1000х1000
