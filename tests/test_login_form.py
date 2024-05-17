import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(5)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@test.com')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    time.sleep(5)
    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)
    form_page.hobbies_checkbox_1.click_force()
    form_page.hobbies_checkbox_2.click_force()
    form_page.hobbies_checkbox_3.click_force()
    form_page.current_address.send_keys('USSR, Leningrad')
    form_page.btn_submit.click_force()
    time.sleep(5)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

# способ №1
def test_select_state(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(5)
    form_page.btn_select_state.scroll_to_element()

    form_page.btn_select_state.click()
    form_page.ncr.click()
    time.sleep(5)

# способ №2
def test_select_state(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(5)
    form_page.btn_select_state.scroll_to_element()

    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(5)

# способ №3
def test_select_state(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(5)
    form_page.btn_select_state.scroll_to_element()

    form_page.btn_select_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_DOWN)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(5)
