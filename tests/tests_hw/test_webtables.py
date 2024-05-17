import time
from pages.webtables import WebTables


# Test-case: Тестирование кнопки "Add" и диалогового окна "Registration Form"
def test_webtables(browser):
    webtables = WebTables(browser)  # объект страницы https://demoqa.com/webtables
    webtables.visit()               # переход на страницу https://demoqa.com/webtables

    # Установить размер окна 2000х1000
    browser.set_window_size(2000, 1000)

    # Проверка: на странице имеется кнопка "Add"
    assert webtables.btn_tables_add.get_text() == 'Add'

    # По клику на кнопку "Add"...
    webtables.btn_tables_add.click()
    # ... проверка: открывается диалоговое окно "Registration Form"
    assert webtables.user_form.exist()

    # В диалоге нельзя сохранить пустую форму
    webtables.btn_submit.click()    # кликнуть по кнопке "Submit"
    assert webtables.user_form.get_dom_attribute('class') == 'was-validated'

    # Если заполнить все поля и нажать на кнопку "Submit"...
    webtables.first_name.send_keys('Ivan')
    webtables.last_name.send_keys('Ivanov')
    webtables.email.send_keys('ivan@test.com')
    webtables.age.send_keys('28')
    webtables.salary.send_keys('100000')
    webtables.department.send_keys('IT')
    webtables.btn_submit.click()        # кликнуть по кнопке "Submit"

    time.sleep(5)

    # ... проверка: диалоговое окно "Registration Form" закрывается
    assert not webtables.user_form.exist()

    # Проверка: в таблицу добавляется новая запись
    assert webtables.new_row.get_dom_attribute('class') == ('rt-tr -even' or 'rt-tr -odd')

    # Если кликнуть на карандаш на строке записи...
    webtables.btn_pencil_4.click()
    # ... проверка: открывается диалог с введенными данными
    assert webtables.user_form.exist()

    # Если изменить имя и сохранить...
    webtables.first_name.clear()
    webtables.first_name.send_keys('Peter')
    webtables.btn_submit.click()

    time.sleep(5)

    # ... проверка: то в таблице обновятся данные
    assert webtables.first_name_in_table.get_text() == 'Peter'

    # Если нажать на корзину в строке записи...
    webtables.btn_delete_4.click()

    # ... проверка: запись удаляется
    assert webtables.first_name_in_table.get_text() == ' '

    # Установить размер окна по умолчанию
    browser.set_window_size(1000, 1000)


# Test-case*: Тестирование кнопок "Next" и "Previous"
def test_next_previous(browser):
    # Предусловия:
    # 1. Открыта страница https://demoqa.com/webtables
    webtables = WebTables(browser)
    webtables.visit()

    # Установить размеры окна 2000х1000
    browser.set_window_size(2000, 1000)

    # 2. Rол-во строк в таблице установлено 5
    webtables.select_rows.scroll_to_element()
    webtables.select_rows.click()
    webtables.select_5.click()

    # Test-case
    # Кнопки "Next" и "Previous" заблокированы (по клику ничего не происходит и имеют атрибут disabled)
    assert not webtables.btn_previous.click()
    assert webtables.btn_previous.get_dom_attribute('disabled')
    assert not webtables.btn_next.click()
    assert webtables.btn_next.get_dom_attribute('disabled')

    # Если добавить в таблицу еще 3 записи, то: ...
    for _ in range(3):
        webtables.btn_tables_add.click()
        webtables.first_name.send_keys('Ivan')
        webtables.last_name.send_keys('Ivanov')
        webtables.email.send_keys('ivan@test.com')
        webtables.age.send_keys('28')
        webtables.salary.send_keys('100000')
        webtables.department.send_keys('IT')
        webtables.btn_submit.click()
        time.sleep(5)

    # ... проверка: 1. появляется 2-я страница (of 2)
    assert webtables.text_page_of.get_text() == '2'

    # ... проверка: 2. кнопка "Next" становится доступной
    assert not webtables.btn_next.get_dom_attribute('disabled')

    # Если кликнуть по кнопке "Next" ...
    webtables.btn_next.click()

    # ... проверка: открывается 2-я страница
    assert webtables.page_input.get_dom_attribute('value') == '2'

    # Если кликнуть по кнопке Previous ...
    webtables.btn_previous.click()

    # ... проверка: если кликнуть по кнопке "Previous"
    assert webtables.page_input.get_dom_attribute('value') == '1'

    # Установить размер окна по умолчанию
    browser.set_window_size(1000, 1000)
