class NewPost():
    # Locators of all the elements
    select_NewPost_by_xpath = "/html/body/header/nav/div/div/div[2]/a[1]"
    insert_Title_by_id = "id_title"
    insert_Content_by_id = "id_content"
    select_post_submit_by_xpath = "/html/body/main/div/div[1]/div/form/div/button"
    select_Delete_btn_by_xpath = "/html/body/main/div/div[1]/article/div/div/div/a[2]"
    select_Yes_btn_by_xpath = "/html/body/main/div/div[1]/div/form/div/button"

    def __init__(self, driver):
        self.driver = driver

    def clickNewPost(self):
        self.driver.find_element_by_xpath(self.select_NewPost_by_xpath).click()

    def addTitle(self):
        self.driver.find_element_by_id(self.insert_Title_by_id).send_keys("New Automation Post")

    def addContent(self):
        self.driver.find_element_by_id(self.insert_Content_by_id).send_keys("Testing the Python Automation Script")

    def clickPost(self):
        self.driver.find_element_by_xpath(self.select_post_submit_by_xpath).click()

    def clickDelete(self):
        self.driver.find_element_by_xpath(self.select_Delete_btn_by_xpath).click()
        self.driver.find_element_by_xpath(self.select_Yes_btn_by_xpath).click()