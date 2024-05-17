import time
from pages.webtables import WebTables


def test_sort(browser):
    page_webtables = WebTables(browser)
    page_webtables.visit()

    for element in page_webtables.btn_col.find_elements():
        if element.click():
            assert page_webtables.name_col.get_dom_attribute('class') == 'rt-td'
