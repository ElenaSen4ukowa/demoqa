from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'div.action-buttons > span[title="Delete"]')
        self.btn_tables_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.new_row = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div', 'xpath')
        self.btn_pencil_4 = WebElement(driver, '#edit-record-4 > svg > path')
        self.first_name_in_table = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4 > svg > path')
        self.select_rows = WebElement(driver, 'div.-center > span.select-wrap.-pageSizeOptions > select')
        self.select_5 = WebElement(driver, 'select > option:nth-child(1)')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.text_page_of = WebElement(driver, 'div.-center > span.-pageInfo > span')
        self.page_input = WebElement(driver, 'div.-center > span.-pageInfo > div > input[type=number]')
        self.btn_col = WebElement(driver, 'div > div[class="rt-resizable-header-content"]')
        self.name_col = WebElement(driver, 'div > div[class="rt-td"]')







