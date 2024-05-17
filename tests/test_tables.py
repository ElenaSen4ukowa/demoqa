import time
from pages.webtables import WebTables

def test_tables(browser):
    tables = WebTables(browser)
    tables.visit()

    browser.set_window_size(2000, 1000)

    # проверка отсутствия блока No rows
    assert not tables.no_rows_found.exist()

    # Удалить все записи из таблицы
    while tables.btn_delete_row.exist():
        tables.btn_delete_row.click()

    time.sleep(5)
    assert tables.no_rows_found.exist()

    browser.set_window_size(1000, 1000)
