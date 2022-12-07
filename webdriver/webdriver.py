from selenium import webdriver


class BasePage:
    def __init__(self, host=None, url=None, capabilities=None,  selenoid=False):
        self.url = url
        if selenoid:
            self.driver = webdriver.Remote(
                desired_capabilities=capabilities,
                command_executor=host
            )
        else:
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def open_base_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()
