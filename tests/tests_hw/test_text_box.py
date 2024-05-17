import time
from pages.text_box import TextBox


name: str = 'tester testerovich'
address: str = 'USSR, Leningrad'
text_border: str = 'Name:' + name + '\n' + 'Current Address :' + address
def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.full_name.send_keys(name)
    text_box.current_address.send_keys(address)
    text_box.btn_submit.scroll_to_element()
    time.sleep(5)
    text_box.btn_submit.click_force()
    time.sleep(5)
    assert text_box.border.get_text() == text_border


