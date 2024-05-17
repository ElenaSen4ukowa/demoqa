from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.btn_submit.scroll_to_element()

    assert text_box.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert text_box.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert text_box.btn_submit.check_css('borderBottomColor', 'rgba(0, 123, 255, 1)')
