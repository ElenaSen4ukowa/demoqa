import time
from pages.alerts import Alerts


def test_allert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    # проверка: на странице нет активного алерта
    assert not page_alerts.alert()

    # нажать на кнопку вызова окна алерта
    page_alerts.btn_allert.click()

    time.sleep(3)

    # проверка: на странице появился алерт
    assert page_alerts.alert()


def test_alert_text(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    # нажать на кнопку вызова окна алерта
    page_alerts.btn_allert.click()
    time.sleep(3)

    # проверить текст в окне алерта
    assert page_alerts.alert().text == 'You clicked a button'
    time.sleep(3)

    # подтвердить алерт
    page_alerts.alert().accept()

    # проверка: на странице нет активного алерта
    assert not page_alerts.alert()


def test_confirm(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    # нажать на кнопку вызова окна алерта
    page_alerts.btn_confirm.click()
    time.sleep(3)

    # отменить действие в окне
    page_alerts.alert().dismiss()
    time.sleep(2)

    # проверка: текст в блоке #confirmResult
    assert page_alerts.confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()
    name = 'Elena'

    # нажать на кнопку вызова окна алерта
    page_alerts.btn_prompt.click()
    time.sleep(3)

    # ввести свое имя в текстовое поле
    page_alerts.alert().send_keys(name)

    # подтвердить алерт
    page_alerts.alert().accept()
    time.sleep(3)

    # проверка: текст в блоке #promptResult
    assert page_alerts.prompt_result.get_text() == f'You entered {name}'
