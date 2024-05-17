import time
from pages.demoqa import DemoQa
from pages.elements import ElementsPage

def test_check_footer_span(browser):

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    time.sleep(20)
    assert demo_qa_page.footer_span.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_text_in_the_middle(browser):
    demo_qa_page = DemoQa(browser)
    el_page = ElementsPage(browser)
    demo_qa_page.visit()
    time.sleep(10)
    browser.execute_script("window.scrollBy(0, 200);")
    time.sleep(20)
    demo_qa_page.btn_elements.click()  # клик по элементу, чтобы перейти на другую страницу
    time.sleep(10)
    assert el_page.text_in_the_middle.get_text() == 'Please select an item from left to start practice.'

def test_check_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    assert el_page.text_elements.get_text() == 'Elements'
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()

