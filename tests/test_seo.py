import time
import pytest
from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

def test_seo_title(browser):
    demo_qa_page = DemoQa(browser)      # объект страницы https://demoqa.com/
    demo_qa_page.visit()                # переход на страницу https://demoqa.com/

    # assert demo_qa_page.get_title() == 'DEMOQA'
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()

    time.sleep(5)

    assert page.get_title() == 'DEMOQA'
