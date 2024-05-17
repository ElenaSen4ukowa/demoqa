import time
import pytest
from pages.modal_dialogs import ModalDialogs


@pytest.mark.skipif(True, reason="страница не доступна")
def test_check_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    time.sleep(3)

    # проверка: на странице присутствуют 2 кнопки “Small modal” и “Large modal”
    assert modal_dialogs_page.btn_small.exist()
    assert modal_dialogs_page.btn_large.exist()

    # при клике на кнопки “Small modal”...
    modal_dialogs_page.btn_small.click()

    time.sleep(3)

    # ... проверка: открывается модальное окно
    assert modal_dialogs_page.small_modal.exist()

    # у окна есть кнопка “close” по клику...
    modal_dialogs_page.btn_cls_small.click()

    time.sleep(3)

    # ... проверка: окно закрывается
    assert not modal_dialogs_page.small_modal.exist()

    # при клике на кнопки “Large modal”...
    modal_dialogs_page.btn_large.click()

    time.sleep(3)

    # ... проверка: открывается модальное окно
    assert modal_dialogs_page.large_modal.exist()

    # у окна есть кнопка “close” по клику...
    modal_dialogs_page.btn_cls_large.click()

    time.sleep(3)

    # ... проверка: окно закрывается
    assert not modal_dialogs_page.large_modal.exist()
