import time
from pages.text_box import TextBox

def test_clear(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()

    textbox_page.full_name.send_keys('tester testerovich')
    time.sleep(5)
    textbox_page.full_name.clear()
    time.sleep(5)
    assert textbox_page.full_name.get_text() == ""
