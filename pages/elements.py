from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_in_the_middle = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0')
        self.btn_sidebar_first_checkbox = WebElement(driver, '#item-1')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')

