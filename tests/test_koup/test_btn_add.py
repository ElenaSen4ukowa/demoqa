import time
from pages.koup import Koup
from pages.koup_add import KoupAdd

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()              # открыть страницу https://the-internet.herokuapp.com/

    # проверка, имеется ли на странице ссылка 'Add/Remove Elements'
    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()     # перейти по ссылке 'Add/Remove Elements'
    assert koup_add.equal_url()    # проверка ссылки с текущим URL

    # проверка, имеется ли на странице кнопка с текстом 'Add Element'
    assert koup_add.btn_add.get_text() == 'Add Element'

    # проверка, у кнопки имеется атрибут onclick, равный 'addElement()'
    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()'

    # Кликнуть на кнопку 'Add Element' 4 раза
    for i in range(4):
        koup_add.btn_add.click()

    # проверка, появились ли 4 кнопки с текстом "Delete"
    assert koup_add.btns_delete.check_count_elements(4)

    # проверка для всех элементов (!!! ВАРИАНТ ПРАВИЛЬНОГО РЕШЕНИЯ !!!)
    for element in koup_add.btns_delete.find_elements():
        assert element.text == 'Delete'

    # проверка только для первого элемента (!!! ВАРИАНТ НЕПРАВИЛЬНОГО РЕШЕНИЯ !!!)
    # assert koup_add.btns_delete.get_text() == 'Delete'

    # Кликнуть на каждую кнопку 'Delete'
    while koup_add.btns_delete.exist():   # "Пока кнопки 'Delete' существуют..."
        koup_add.btns_delete.click()      # "... нажимать на кнопки 'Delete'"

    # проверка, что кнопок 'Delete' нет
    assert not koup_add.btns_delete.exist()

    time.sleep(5)
    