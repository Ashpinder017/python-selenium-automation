from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BIN=(By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
HEADER=(By.CSS_SELECTOR,"[class*='UtilityHeaderWrapper']")
HEADER_LINK=(By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")
SELECT_PRODUCT=(By.CSS_SELECTOR,"[id*='addToCartButtonOrTextI']")
ORDER_PRODUCT=(By.CSS_SELECTOR,"[data-test='orderPickupButton']")
PRODUCT_INCART=(By.XPATH,"//a[@href='/cart']")
PRODUCT_RATE_ITEM=(By.CSS_SELECTOR,"[class*='styles__CartSummarySpan']")


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Check for shopping cart')
def check_shopping_cart(context):
   context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@when("Search an {item}")
def search_item(context,item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    sleep(5)


@when('Click on search icon')
def click_on_search_icon(context):
    context.driver.find_element(*SEARCH_BIN).click()
    sleep(10)


@when("search for 'pens'")
def search_product(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('pens')


@then('select an product')
def select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()
    context.driver.find_element(*ORDER_PRODUCT).click()


@then('check there is product and price in the cart')
def check_product(context):
    context.driver.find_element(*PRODUCT_INCART).click()
    link=context.driver.find_element(*PRODUCT_RATE_ITEM)
    print(f'Total amount and items in cart {link.text}')


@when('User can Sign in')
def sign_in(context):
    context.driver.get('https://www.target.com')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='accountNav-signIn']").click()


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(*HEADER)


@then('Verify header has 6 links')
def verify_header_links(context):
    link=context.driver.find_elements(*HEADER_LINK)
    print(f'Number of links in header are {len(link)}')
    assert len(link)==6,f"Expected 6 links, got {len(link)}"
