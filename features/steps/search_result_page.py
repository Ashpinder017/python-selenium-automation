from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@then('Verify correct {result} shown')
def step_impl(context,result):
    actual_test=context.driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
    assert 'result' in actual_test,f"{result} is not" in (actual_test)
    print('Test case passed')


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
        actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
        context.app.search_result_page.verify_search_results(expected_item)


@then('verify product name and image')
def verify_products_name_img(context):
        context.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        context.driver.execute_script("window.scrollBy(0,2000)", "")

        all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

        for product in all_products:
            title = product.find_element(*PRODUCT_TITLE).text
            assert title, 'Product title not shown'
            product.find_element(*PRODUCT_IMG)