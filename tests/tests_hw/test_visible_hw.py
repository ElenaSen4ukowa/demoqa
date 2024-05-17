import time
from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.section1_p.visible()
    accordion_page.section1.click()
    time.sleep(5)
    assert not accordion_page.section1_p.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.section2_p_1.visible()
    assert not accordion_page.section2_p_2.visible()
    assert not accordion_page.section3_p.visible()
