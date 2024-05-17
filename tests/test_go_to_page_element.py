import time
from pages.demoqa import DemoQa
from pages.elements import ElementsPage

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()                # войти на страницу https://demoqa.com/
    time.sleep(5)
    assert demo_qa_page.equal_url()     # проверка нахождения странице https://demoqa.com/
    browser.execute_script("window.scrollBy(0, 200);")
    time.sleep(30)
    demo_qa_page.btn_elements.click()     # клик по элементу, чтобы перейти на другую страницу
    time.sleep(10)
    assert el_page.equal_url()          # проверка нахождения странице https://demoqa.com/elements/
