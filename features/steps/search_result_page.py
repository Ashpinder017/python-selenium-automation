from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify correct {result} shown')
def step_impl(context,result):
    actual_test=context.driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text
    assert 'result' in actual_test,f"{result} is not" in (actual_test)
    print('Test case passed')