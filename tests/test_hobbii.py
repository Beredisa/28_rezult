import time
import pytest

from pages.hobbii_pages import Main_Page
from selenium.webdriver import ActionChains

# py -m pytest -v --driver Chrome --driver-path chromedriver.exe test_hobbii.py


# 1

def test_start_page_main_elements(web_browser):
    """ Наличие основных элементов на главной странице"""
    page = Main_Page(web_browser)

    page.top_sale.is_visible()
    page.general_logo.is_visible()
    page.general_menu.is_visible()
    page.top_sale.is_clickable()
    page.general_logo.is_clickable()
    page.footer.is_visible()


# 02-11 Проверка кнопок верхнего(малого) меню

def test_menu_blog_url(web_browser):
    """ Проверка кнопки блог верхнего меню на переход в другой раздел """
    page = Main_Page(web_browser)
    page.blog_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/blog'


def test_menu_blog(web_browser):
    """ Проверка кнопки блог верхнего меню на видимость раздела подкатегорий"""
    page = Main_Page(web_browser)
    page.blog_btn.click()
    assert page.blog_categories.is_visible()


def test_menu_hobbii_plus_url(web_browser):
    """ Проверка кнопки Hobbii Plus верхнего меню на переход в другой раздел """
    page = Main_Page(web_browser)
    page.hobbii_plus_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/plus'


def test_menu_hobbii_plus(web_browser):
    """ Проверка кнопки Hobbii Plus верхнего меню на видимость другого раздела  """
    page = Main_Page(web_browser)
    page.hobbii_plus_btn.click()
    assert page.hobbii_benefit.is_visible()


def test_menu_point_url(web_browser):
    """ Проверка кнопки Point верхнего меню на переход в другой раздел """
    page = Main_Page(web_browser)
    page.point_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/pointshop'


def test_menu_point(web_browser):
    """ Проверка кнопки Point верхнего меню на видимость другого раздела """
    page = Main_Page(web_browser)
    page.point_btn.click()
    assert page.poin_store.is_visible()


def test_menu_help_contact_url(web_browser):
    """ Проверка кнопки Help/Contact верхнего меню на переход в другой раздел """
    page = Main_Page(web_browser)
    page.help_contact_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/hobbii-faq'


def test_menu_help_contact(web_browser):
    """ Проверка кнопки Help/Contact верхнего меню на видимость другого раздела """
    page = Main_Page(web_browser)
    page.help_contact_btn.click()
    assert page.help_contact_menu.is_visible()


def test_menu_about_url(web_browser):
    """ Проверка кнопки About верхнего меню на переход в другой раздел """
    page = Main_Page(web_browser)
    page.about_btn.click()
    assert page.get_current_url() == 'https://hobbii.com/about'


def test_menu_about(web_browser):
    """ Проверка кнопки About верхнего меню на видимость другого раздела """
    page = Main_Page(web_browser)
    page.about_btn.click()
    assert page.about_hobbii.is_visible()


# 12-13 Проверка главного лого

def test_general_logo_1(web_browser):
    """ Проверка главного лого меню на возвращение на основную страницу """
    page = Main_Page(web_browser)
    page.blog_btn.click()

    page.general_logo.click()
    assert page.get_current_url() == 'https://hobbii.com/'


def test_general_logo_2(web_browser):
    """ Проверка главного лого меню на возвращение на основную страницу """
    page = Main_Page(web_browser)
    page.about_btn.click()

    page.general_logo.click()
    assert page.get_current_url() == 'https://hobbii.com/'


# 14-23 Проверка кнопок главного меню

def test_general_menu_elements_visible(web_browser):
    """ Проверка кнопок главного меню на видимость """
    page = Main_Page(web_browser)
    assert page.gen_menu_home.is_visible()
    assert page.gen_menu_yarn.is_visible()
    assert page.gen_menu_patterns.is_visible()
    assert page.gen_menu_crochetHooks.is_visible()
    assert page.gen_menu_knittingNeedles.is_visible()
    assert page.gen_menu_accessories.is_visible()
    assert page.gen_menu_excitingThings.is_visible()


def test_general_menu_elements_clickable(web_browser):
    """ Проверка кнопок главного меню на кликабельность"""
    page = Main_Page(web_browser)
    assert page.gen_menu_home.is_clickable()
    assert page.gen_menu_yarn.is_clickable()
    assert page.gen_menu_patterns.is_clickable()
    assert page.gen_menu_crochetHooks.is_clickable()
    assert page.gen_menu_knittingNeedles.is_clickable()
    assert page.gen_menu_accessories.is_clickable()
    assert page.gen_menu_excitingThings.is_clickable()


def test_gen_menu_yarn_url(web_browser):
    """ Проверка кнопки Yarn главного меню на переход в выбранный раздел по адресу страницы"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    assert page.get_current_url() == 'https://hobbii.com/yarn'


def test_gen_yarn_home(web_browser):
    """ Проверка кнопки Yarn главного меню на переход в выбранный раздел"""
    page = Main_Page(web_browser)
    page.gen_menu_yarn.click()
    assert page.yarn_fibers.is_visible()


def test_gen_menu_patterns_url(web_browser):
    """ Проверка кнопки Patterns главного меню на переход в выбранный раздел по адресу страницы"""
    page = Main_Page(web_browser)
    page.gen_menu_patterns.click()
    assert page.get_current_url() == 'https://hobbii.com/product-patterns'


def test_gen_menu_patterns_home(web_browser):
    """ Проверка кнопки Patterns главного меню на переход в выбранный раздел"""
    page = Main_Page(web_browser)
    page.gen_menu_patterns.click()
    assert page.yarn_fibers.is_visible()


def test_gen_menu_crochethooks_url(web_browser):
    """ Проверка кнопки Crochet Hooks главного меню на переход в выбранный раздел по адресу страницы"""
    page = Main_Page(web_browser)
    page.gen_menu_crochetHooks.click()
    assert page.get_current_url() == 'https://hobbii.com/crochet-hooks'


def test_gen_menu_crochethooks_home(web_browser):
    """ Проверка кнопки Crochet Hooks главного меню на переход в выбранный раздел """
    page = Main_Page(web_browser)
    page.gen_menu_crochetHooks.click()
    assert page.crochetHooks_category.is_visible()


def test_gen_menu_knittingneedles_url(web_browser):
    """ Проверка кнопки Knitting Needles главного меню на переход в выбранный раздел по адресу страницы """
    page = Main_Page(web_browser)
    page.gen_menu_knittingNeedles.click()
    assert page.get_current_url() == 'https://hobbii.com/knitting-needles'


def test_gen_menu_knittingneedles_home(web_browser):
    """ Проверка кнопки Knitting Needles главного меню на переход в выбранный раздел """
    page = Main_Page(web_browser)
    page.gen_menu_knittingNeedles.click()
    assert page.knittingNeedles_page.is_visible()


# 24-25 Предподвал

def test_about_hobbii_history(web_browser):
    """ Проверка презентации истории сайта  """
    page = Main_Page(web_browser)
    page.wait_page_loaded()
    assert page.about_hobbii_box.is_presented()


def test_reviews_list_present(web_browser):
    """ Проверка опций блока отзывов о сайте на видимость и клакабельность """
    page = Main_Page(web_browser)
    page.reviews_box.scroll_to_element()
    page.wait_page_loaded()

    page.reviews_list.is_visible()
    page.reviews_trustpilot.is_clickable()


def test_reviews_list_trustpilot(web_browser):
    """ Проверка опции блока отзывов о сайте Trustpilot на переход на другую страницу """
    page = Main_Page(web_browser)
    page.wait_page_loaded()
    page.switch_to_iframe(0)
    page.reviews_trustpilot.scroll_to_element()

    reviews_trustpilot_frame = page.reviews_trustpilot.find()
    reviews_trustpilot_frame.click()

    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()

    if page.police_title.is_visible():
        page.cookies_ok.click()
        assert page.get_current_url() == 'https://uk.trustpilot.com/review/hobbii.co.uk?utm_medium=trustbox&utm_source=Carousel'


# 26-29 Иконки соцсетей

def test_instagram_link(web_browser):
    """ Проверка значка instagrsm на переход на запрашиваемый сайт"""
    page = Main_Page(web_browser)
    page.scroll_down()
    page.instagram_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    if page.instagram_cookie.is_presented():
        page.instagram_yes.click()
        page.wait_page_loaded()
        assert page.get_current_url() == 'https://www.instagram.com/hobbii_yarn/'


def test_facebook_link(web_browser):
    """ Проверка значка facebook на переход на запрашиваемый сайт"""
    page = Main_Page(web_browser)
    page.scroll_down()
    page.facebook_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    if page.facebook_cookie.is_presented():
        page.facebook_yes.click()
        page.wait_page_loaded()
        assert page.get_current_url() == 'https://www.facebook.com/hobbii.europe/'


def test_pinterest_link(web_browser):
    """ Проверка значка pinterest на переход на запрашиваемый сайт"""
    page = Main_Page(web_browser)
    page.scroll_down()
    page.pinterest_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.pinterest.com/hobbiicom/'


def test_youtube_btn(web_browser):
    """ Проверка значка youtube на переход на запрашиваемый сайт"""
    page = Main_Page(web_browser)
    page.scroll_down()
    page.youtube_btn.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.wait_page_loaded()
    if page.youtube_list.is_presented():
        page.youtube_yes.click()
        assert page.get_current_url() == 'https://www.youtube.com/c/hobbiicom'


# 30 Ссылки в подвале сайта

def test_footer_list(web_browser):
    """ Проверка кнопок меню в подвале сайта на презентабельность"""
    page = Main_Page(web_browser)
    page.scroll_down()

    page.contact.is_presented()
    page.about_as.is_presented()
    page.fun_stuff.is_presented()
    page.follow_as.is_presented()

