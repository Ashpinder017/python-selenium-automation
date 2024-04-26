from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultPage(Page):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_result(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'


        def find_el(self):
            print('Finding Element')


        def click(self):
            print('Clicking')


        def verity_text(self,expected_item):
            print(f'Verity Text: {expected_item}')

            
