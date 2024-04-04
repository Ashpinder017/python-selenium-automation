
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

@when('Check for shopping cart')
def check_shopping_cart(context):
   context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
@then('Verify the cart is empty')
def verify_cart_is_empty(context):
    actual_text=context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
#    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]").text()
    assert 'Your cart is empty' in actual_text, f'Error! Cart is not Empty'
#   sleep(10)

@when('User can Sign in')
def sign_in(context):
    context.driver.get('https://www.target.com')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    actual_text=context.driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']")
    assert actual_text, f'Error!User is not in Sign In page'
    print(actual_text)
