class Logout():
    # Locators of all the elements
    select_Logout_by_xpath = "/html/body/header/nav/div/div/div[2]/a[3]"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.select_Logout_by_xpath).click()