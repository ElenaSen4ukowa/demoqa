import time
from pages.elements import ElementsPage

def test_find_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    time.sleep(5)

    assert el_page.btns_first_menu.check_count_elements(9)
