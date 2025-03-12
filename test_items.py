from selenium.webdriver.common.by import By
from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# link = "https://www.google.com/"
# link = "http://selenium1py.pythonanywhere.com/"

def test_page_contains_button_add_to_basket(browser):
    browser.get(link)
    sleep(5)
    button = browser.find_element(
        By.XPATH, "//*[contains(@class,'btn-add-to-basket')]"
    )
    assert button is not None, "There is Basket button?"