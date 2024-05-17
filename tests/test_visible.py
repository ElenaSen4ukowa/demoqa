import time
from pages.elements import ElementsPage


def test_visible_btn_sidebar(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    # el_page.btn_sidebar_first.click()
    time.sleep(5)
    # assert el_page.btn_sidebar_first_textbox.exist()
    assert el_page.btn_sidebar_first_textbox.visible()  # проверка того, что кнопка видна

def test_not_visible_btn_sidebar(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    assert el_page.btn_sidebar_first_checkbox.visible()
    el_page.btn_sidebar_first.click()
    time.sleep(10)
    assert not el_page.btn_sidebar_first_checkbox.visible()
