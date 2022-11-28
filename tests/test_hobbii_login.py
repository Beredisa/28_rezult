import time
import pytest

from pages.hobbii_pages import Main_Page
from selenium.webdriver import ActionChains

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_hobbii_login.py


# 1-4 Проверка окошка ввода логина

def test_login_box_is_visible(web_browser):
    """ Проверка видимость кнопки бокса логина """
    page = Main_Page(web_browser)
    page.wait_page_loaded()

    page.login_box.is_visible()



def test_login_container_present(web_browser):
    """ Проверка презентабельности кнопки бокса логина """
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()

    assert page.login_container.is_presented()


def test_login_contains_elements_visible(web_browser):
    """ Проверка видимость окошек в боксе логина """
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()

    assert page.input_email.is_visible()
    assert page.input_password.is_visible()
    assert page.in_account_btn.is_visible()


def test_login_register_container_present(web_browser):
    """ Проверка перехода в раздел ввода логина по адресу"""
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()
    page.login_register.click()

    assert page.get_current_url() == 'https://hobbii.com/account/signup'
    assert page.login_register_container.is_presented()


# 5

def test_positive_account_input(web_browser):
    """ Проверка валидного ввода данных """
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()
    page.input_email.send_keys('ok.brede@inbox.lv')
    page.input_password.send_keys('brede73')
    page.in_account_btn.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://hobbii.com/account/account'


# 6-11 Проверка неправильного ввода логина

@pytest.mark.parametrize("locator", ['ok.bre@inbox.lv', 'brede@inbox.lv', '456tred'
                                     ])
def test_negative_account_email_forgot(web_browser, locator):
    """ Проверка невалидного ввода емайла """
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()
    page.input_email = locator
    page.input_password = 'brede73'
    page.in_account_btn.click()
    page.wait_page_loaded()
    page.forgotten_password_btn.click()

    assert page.forgotten_container.is_presented()

@pytest.mark.parametrize("locator", ['26543', 'bebebe', '$36карт'
                                     ])
def test_negative_account_password_forgot(web_browser, locator):
    """ Проверка невалидного ввода пароля"""
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()
    page.input_email = 'ok.brede@inbox.lv'
    page.input_password = locator
    page.in_account_btn.click()
    page.wait_page_loaded()
    page.forgotten_password_btn.click()

    assert page.get_current_url() == 'https://hobbii.com/account/forgotten?identifier=ok.brede%40inbox.lv'
    assert page.forgotten_container.is_presented()


# 12-15 Проверка неправильного ввода обоих данных

@pytest.mark.parametrize('locator_1', ['ok.bre@inbox.lv', 'brede@inbox.lv'
                                     ])
@pytest.mark.parametrize('locator_2', ['bret', '34567'
                                     ])
def test_negative_account_forgot(web_browser, locator_1, locator_2):
    page = Main_Page(web_browser)
    page.login_input[1].click()
    page.wait_page_loaded()
    page.input_email = locator_1
    page.input_password = locator_2
    page.in_account_btn.click()
    page.wait_page_loaded()
    page.forgotten_password_btn.click()

    assert page.forgotten_container.is_presented()




