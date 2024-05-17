from pages.text_box import TextBox

def test_plceholder(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full Name'
