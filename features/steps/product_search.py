from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_PRODUCT = (By.ID, 'search')
SEARCH_ICON=(By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


# @when('Click on search icon')
# def click_search_icon(context):
#   context.driver.find_element(*SEARCH_SUBMIT).click()
#  sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'


@given('open target product {product_id} page')
def open_product_91511634(context, product_id):
   #  context.driver.get('https://wwwtargert.com/p/{product_id}')
   context.driver.get(
      'https://www.target.com/p/levi-s-mens-carson-synthetic-leather-casual-lace-up-sneaker-shoe/-/A-91511634?preselect=91511660#lnk=sametab')


@then('User can click on colors')
def click_colors(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current Color:', selected_color)
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)

        print('Selected Colors:', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'


@when("Search for {item}")
def search_mango(context,item):
    context.driver.find_element(*SEARCH_PRODUCT).send_keys(item)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(5)
