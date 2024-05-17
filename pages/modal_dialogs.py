from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.co/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.menu_modal_list = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.btn_small = WebElement(driver, '#showSmallModal')
        self.btn_large = WebElement(driver, '#showLargeModal')
        self.small_modal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.large_modal = WebElement(driver, '#example-modal-sizes-title-lg')
        self.btn_cls_small = WebElement(driver, '#closeSmallModal')
        self.btn_cls_large = WebElement(driver, '#closeLargeModal')
