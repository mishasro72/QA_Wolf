from playwright.sync_api import Page
from pages.main_page import MainPage
import allure

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Sort articles")
@allure.title("Checking the first 100 articles are sorted from newest to oldest")
def test_articles_sorted(page):

    main_page = MainPage(page)
    main_page.go_to_main_page()
    time = main_page.get_long(main_page.get_all_dates())
    main_page.check_list_sorted(time)
   


