import time
from pages.links import Links

def test_window_tab(browser):
    page_link = Links(browser)
    page_link.visit()

    href_home = page_link.home.get_dom_attribute('href')

    assert page_link.home.exist()
    assert page_link.home.get_text() == 'Home'
    assert href_home == 'https://demoqa.com'

    page_link.home.click()
    time.sleep(5)

    browser.switch_to.new_window(browser.window_handles[1])
    time.sleep(10)

    assert browser.current_url == 'https://demoqa.com'
