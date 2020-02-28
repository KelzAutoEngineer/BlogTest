class BlogLogin():
    # Locators of all the elements
    select_blog_with_us_xpath = "/html/body/div[2]/div/div[2]/div/ul/li[1]/div/div[1]/button"
    select_login_xpath = "/html/body/div[2]/div/div[2]/div/ul/li[5]/div/div[1]/a"
    textbox_username_id = "id_username"
    textbox_password_id = "id_password"
    login_btn_xpath = "/html/body/main/div/div[1]/div/form/div/button"

    def __init__(self, driver):
        self.driver = driver

    def clickBlogWithUs(self):
        self.driver.find_element_by_xpath(self.select_blog_with_us_xpath).click()

    def clickHomeLogin(self):
        self.driver.find_element_by_xpath(self.select_login_xpath).click()

    def addUsername(self, id_username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys("User")

    def addPassword(self, id_password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys("Testing321")

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()