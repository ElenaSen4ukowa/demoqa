import time
from pages.demoqa import DemoQa
from pages.elements import ElementsPage

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)        # объект страницы https://demoqa.com/
    el_page = ElementsPage(browser)       # объект страницы https://demoqa.com/elements

    demo_qa_page.visit()                  # переход на страницу https://demoqa.com/
    time.sleep(5)
    browser.execute_script("window.scrollBy(0, 200);")
    demo_qa_page.btn_elements.click()     # нажать на кнопку "Elements"
    time.sleep(5)
    el_page.refresh()                     # обновить страницу
    browser.refresh()                     # обновить страницу

    browser.back()                        # стрелка назад (вернуться назад) -> https://demoqa.com/
    browser.forward()                     # стрелка вперед (перейти вперед) -> https://demoqa.com/elements

    assert el_page.equal_url()                   # проверка на сравнение с текущим URL

# NB! методы refresh(), back(), forward() можно вызывать как от объекта страницы, так и от browser
#     в тест-кейсе пишем от объекта, чтобы видеть, с какой страницей мы работаем