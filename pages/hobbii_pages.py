# содержит конкретные адреса элементов страниц !

# import config
import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

class Main_Page(WebPage):

    def __init__(self, web_driver, url=''):

        url = 'https://hobbii.com/'
        self._web_driver = web_driver

        super().__init__(web_driver, url)

    login_box = WebElement(ClassName='account-top-button[1]')
    login_input = ManyWebElements(xpath='//*[@id="login-text"]')
    login_container = WebElement(id="modal-login")

    input_email = WebElement(id="input-identifier")
    input_password = WebElement(id="input-password")
    in_account_btn = WebElement(xpath='//*[@id="modal-login"]/div/div/div[2]/form/input[1]')

    login_register = WebElement(xpath='//*[@id="modal-login"]/div/div/div[1]/a')
    login_register_container = WebElement(xpath='//*[@id="content"]/div[1]/div/div[2]')
    login_error = WebElement(xpath='//*[@id="modal-login"]/div/div/div[2]/form/div[1]')
    forgotten_password_btn = WebElement(id="link-forgotten-modal")
    forgotten_container = WebElement(xpath='//*[@id="content"]/div/div')


# Главная реклама :

    top_sale = WebElement(xpath='//*[@id="top"]/div[1]/a')
    general_logo = WebElement(xpath='//*[@id="logo"]')
    general_menu = WebElement(xpath='//*[@id="menu"]/div')

# Главное меню (кнопки):

    gen_menu_home = WebElement(xpath='//*[@id="menu"]/div/div[2]/ul/li[1]')
    gen_menu_yarn = WebElement(xpath='//*[@id="menu-dropdown-category-59"]')
    gen_menu_patterns = WebElement(xpath='//*[@id="menu-dropdown-category-120"]')
    gen_menu_crochetHooks = WebElement(xpath='//*[@id="menu-dropdown-category-80"]')
    gen_menu_knittingNeedles = WebElement(xpath='//*[@id="menu-dropdown-category-74"]')
    gen_menu_accessories = WebElement(xpath='//*[@id="menu-dropdown-category-73"]')
    gen_menu_excitingThings = WebElement(xpath='//*[@id="menu-dropdown-category-355"]')

# Поисковые локаторы

    search_input = WebElement(xpath='//*[@id="autocomplete-0-input"]')
    search_input_btn = WebElement(xpath='//*[@id="autocomplete-0-label"]/button')
    search_product_cards = ManyWebElements(xpath='"//*[@class="ais-Hits-list"]')
    search_product_cards_one = WebElement(xpath='//li[@class="ais-Hits-item product-layout"]')
    search_product_cards_o5 = WebElement(xpath='//li[@class="ais-Hits-item product-layout"][5]')

    desired_product_card = WebElement(xpath='//*[@id="content"]/div[1]')
    desired_product_color = WebElement(xpath='//*[@id="product-options"]/div[2]/div[1]')
    add_to_cart_btn = WebElement(xpath='//*[@id="button-cart"]')
    cart_top = ManyWebElements(xpath='//span[@class="cart-top-details-price"]')

    product_price = WebElement(xpath='//span[@class="price-wrapper"]')

    cart_box = WebElement(xpath='//*[@class="dropdown cart-top-button"]')
    cart_banner = ManyWebElements(xpath='"//*[@class="dropdown-menu pull-right"]"[1]')
    result_list = ManyWebElements(xpath='//*[@class="table table-responsive"]/tbody/tr')

    invalid_result = WebElement(xpath='//*[@class="aa-Panel custom invert"]')

    sort_by_btn = WebElement(xpath='//*[@class="ais-SortBy sort-by"]')
    date_old = WebElement(xpath='//*[.="Date (Old)"]')
    date_new = WebElement(xpath='//*[.="Date (New)"]')
    price_low = WebElement(xpath='//*[.="Price (Low > High)"]')
    price_high = WebElement(xpath='//*[.="Price (High > Low)"]')
    most_popular = WebElement(xpath='//*[.="Most popular"]')


# Кнопки верхнего меню

    blog_btn = WebElement(xpath='//*[@id="top"]/div[2]/div/a[1]')
    hobbii_plus_btn = WebElement(xpath='//*[@id="top"]/div[2]/div/a[2]')
    point_btn = WebElement(xpath='//*[@id="top"]/div[2]/div/a[3]')
    help_contact_btn = WebElement(xpath='//*[@id="top"]/div[2]/div/a[4]')
    about_btn = WebElement(xpath='//*[@id="top"]/div[2]/div/a[5]')

# Другие страницы

    blog_categories = WebElement(xpath='//*[@id="column-right"]/div/div[1]/h4')
    hobbii_benefit = WebElement(xpath='//*[@id="content"]')
    poin_store = WebElement(xpath='//*[@id="content"]/div/div[1]')
    help_contact_menu = WebElement(xpath='//*[@id="content"]/h1')
    about_hobbii = WebElement(xpath='//*[@id="content"]')
    yarn_fibers = WebElement(xpath='//*[@id="category-page"]/div/div[1]/div/div[1]/div[1]/div[2]')
    crochetHooks_category = WebElement(xpath='//*[@id="category-page"]/div/div[1]/div/div[1]/div[1]/div')
    knittingNeedles_page = WebElement(xpath='//*[@id="category-page"]/div/div[1]/div/div[1]/div[1]')

# Предподвал

    about_hobbii_box = WebElement(xpath='//*[@id="content"]/h1')
    reviews_box = WebElement(ClassName='"container"[6]')
    reviews_list = WebElement(xpath='//*[@id="trust-score"]')

    #reviews_trustpilot = WebElement(xpath='//*[@id="profileLink"]')
    reviews_trustpilot = WebElement(id='profileLink')
    police_title = WebElement(xpath='//*[@id="onetrust-policy-title"]')
    cookies_ok = WebElement(id="onetrust-accept-btn-handler")


# Подвал

    footer = WebElement(xpath='//div[@class="container"][4]/div[@class="row"]')
    contact = WebElement(xpath='//*[@class="col-sm-3"]/h4')
    about_as = WebElement(xpath='//div[@class="col-sm-3 col-xs-6"]/h4')
    fun_stuff = WebElement(xpath='//div[@class="col-sm-3 col-xs-6"][2]/h4')
    follow_as = WebElement(xpath='//*[@class="col-sm-3 col-xs-12"]')


# Иконки соц.сетей:

    instagram_btn = WebElement(xpath='//*[@class="footer-social"]/a[1]')
    instagram_cookie = WebElement(xpath='//*[@class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abam _abcm"]/h2')
    instagram_yes = WebElement(xpath='//*[@class="_a9-- _a9_0"]')

    facebook_btn = WebElement(xpath='//*[@class="footer-social"]/a[2]')
    facebook_cookie = ManyWebElements(xpath='"//*[@class="xx6bls6"]"[0]')
    facebook_yes = WebElement(xpath='//*[@id="facebook"]/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div')

    pinterest_btn = WebElement(xpath='//*[@class="footer-social"]/a[3]')

    youtube_btn = WebElement(xpath='//*[@class="footer-social"]/a[4]')
    youtube_list = WebElement(xpath='//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/h1')
    youtube_yes = WebElement(xpath='//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')








