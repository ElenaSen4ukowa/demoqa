from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.menu_modal_list.check_count_elements(5)  # проверка, что кнопок подменю 5 штук

def test_navigator_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)
    modal_dialogs_page.visit()

    modal_dialogs_page.refresh()         # обновление страницы

    modal_dialogs_page.icon.click()      # клик по иконке "ToolsQA" для перехода на главную страницу

    demo_qa_page.back()                  # вернуться назад на страницу "Modal Dialogs"

    browser.set_window_size(900, 400)    # установить размеры окна 900х400

    modal_dialogs_page.forward()         # перейти по стрелке браузера вперед на главную страницу

    assert demo_qa_page.equal_url()      # проверка URL главной страницы с текущей URL
    assert browser.title == 'DEMOQA'     # проверка титула

    browser.set_window_size(1000, 1000)  # установить размеры окна 1000х1000
