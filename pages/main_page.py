from playwright.sync_api import Page, expect
from locators.main_page_locators import MainPageLocators as MPL
from datetime import datetime

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_main_page(self):
        self.page.goto(MPL.URL)
    
    def get_date(self):
        base = []
        all_dates = self.page.locator(MPL.AGE_Locator).all()
        for date in all_dates:
            base.append(str(date.get_attribute("title")))
        return base
    
    def get_more(self):
        self.page.locator(MPL.more_link).click()
    
    def get_all_dates(self):
        base= []
        for _ in range(4):
            base.extend(self.get_date())
            self.get_more()
        return base[0:100]    

    def get_long(self, base):
        dt = []
        for i in base:
            dt.append(int(datetime.fromisoformat(i).timestamp()))
        return dt
    
    def check_list_sorted(self, list_1):
        assert list_1 == sorted(list_1, reverse=True), "The first 100 articles aren't sorted from newest to oldest"
        



