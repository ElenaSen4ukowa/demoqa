import time
from pages.alerts import Alerts


def test_check_alert(browser):
    page_alerts = Alerts(browser)
    page_alerts.visit()

    # проверка: на странице присутствует кнопка “#timerAlertButton”
    assert page_alerts.btn_timer_alert.exist()

    # через 5 сек после клика на кнопку “#timerAlertButton”...
    page_alerts.btn_timer_alert.click()
    time.sleep(5)

    # ... проверка: всплывает алерт
    assert page_alerts.alert()
