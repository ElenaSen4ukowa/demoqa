import time
from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    browser_tab = BrowserTab(browser)
    browser_tab.visit()

    # проверка: открытых вкладок в браузере 2
    assert len(browser.window_handles) == 2
    time.sleep(3)

    # нажать на кнопку 'new_tab'
    browser_tab.new_tab.click()
    time.sleep(3)

    # проверка: открытых вкладок в браузере теперь 3
    assert len(browser.window_handles) == 3

    # перейти на первую вкладку
    browser.switch_to.new_window(browser.window_handles[0])
    time.sleep(3)
