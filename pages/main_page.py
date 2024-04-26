from pages.base_page import Page



class MainPage(Page):

    def open_main(self):
        self.driver.get("http://www.target.com/")


