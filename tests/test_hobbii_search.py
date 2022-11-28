import time
import pytest

from pages.hobbii_pages import Main_Page
from selenium.webdriver import ActionChains

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_hobbii_login.py

# 1-3

def test_search_box(web_browser):
    """ Проверка окна поля поиска на видимость"""
    page = Main_Page(web_browser)
    assert page.search_input.is_presented()


def test_search_box_btn(web_browser):
    """ Проверка кнопки окна поля поиска на кликабельность"""
    page = Main_Page(web_browser)
    assert page.search_input_btn.is_clickable()


def test_search_box_result(web_browser):
    """ Проверка кнопки окна поля поиска на переход в запрашиваемый раздел по адресу"""
    page = Main_Page(web_browser)
    page.search_input_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/product/search?search='


# 4-10 Проверка поиска товара

def test_search_product(web_browser):
    """ Проверка поиска по валидному заданному названию товара"""
    page = Main_Page(web_browser)
    page.search_input.send_keys('Alpaca')
    page.search_input_btn.click()
    page.search_product_cards.is_visible()
    for elem in page.search_product_cards.get_text():
        assert 'Alpaca' in elem


@pytest.mark.parametrize("locator", ["альпака",
                                     "35786", "$%^&"])
def test_search_invalid_name_product(web_browser, locator):
    """ Проверка поиска по невалидному заданному названию товара"""
    page = Main_Page(web_browser)
    page.search_input.send_keys(locator)
    page.wait_page_loaded()
    assert page.invalid_result.is_presented()


def test_add_to_cart(web_browser):
    """ Проверка презентабельности бокса выбранного товара"""
    page = Main_Page(web_browser)
    page.search_input.send_keys("Alpaca")
    page.search_input_btn.click()
    page.wait_page_loaded()
    page.search_product_cards_one.click()
    page.wait_page_loaded()
    page.desired_product_color.click()
    page.add_to_cart_btn.click()
    page.cart_box.click()
    page.wait_page_loaded()
    assert page.cart_banner.is_presented()


def test_add_to_cart_result(web_browser):
    """ Проверка наличия выбранного товара в боксе выбора"""
    page = Main_Page(web_browser)
    page.search_input.send_keys("Alpaca")
    page.search_input_btn.click()
    page.wait_page_loaded()
    page.search_product_cards_one.click()
    page.wait_page_loaded()
    page.desired_product_color.click()
    page.add_to_cart_btn.click()
    page.cart_box.click()
    page.wait_page_loaded()
    assert page.result_list.count() > 0


def test_add_to_cart_result_summ(web_browser):
    """ Проверка наличия выбранного товара по цене  в боксе выбора"""
    page = Main_Page(web_browser)
    page.search_input.send_keys("Alpaca")
    page.search_input_btn.click()
    page.wait_page_loaded()
    page.search_product_cards_one.click()
    page.wait_page_loaded()
    page.desired_product_color.click()
    page.add_to_cart_btn.click()
    page.wait_page_loaded()
    assert page.cart_top[1].text == '32,00 €'
    assert page.cart_top[1].text == page.product_price.get_text()


# 11

def test_sort_by_btn_clickable(web_browser):
    """ Проверка в разделе Yarn кликабельности кнопки окна сортировки """
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    assert page.sort_by_btn.is_clickable()


# 12-13

def test_search_sort_by_date_old(web_browser):
    """ Проверка в разделе Yarn в окне сортировки по старой дате поступления"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.date_old.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_date_old.png")


def test_search_sort_by_date_new(web_browser):
    """ Проверка в разделе Yarn в окне сортировки по новой дате поступления"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.date_new.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_date_new.png")


# 14

def test_search_sort_by_price_low(web_browser):
    """ Проверка в разделе Yarn в окне сортировки по возрастанию цены"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.price_low.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_price_low.png")


# 15 Сортировка по убыванию цены

def test_search_sort_by_price_high(web_browser):
    """ Проверка в разделе Yarn в окне сортировки по убыванию цены"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.price_high.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_price_high.png")


# 16

def test_search_sort_by_most_popular(web_browser):
    """ Проверка в разделе Yarn в окне сортировки по популярности товара"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    page.wait_page_loaded()
    page.sort_by_btn.click()
    page.most_popular.click()
    page.wait_page_loaded()
    page.screenshot("sort_by_most_popular.png")


