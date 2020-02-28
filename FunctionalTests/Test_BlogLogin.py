from pageObjects.BlogLogin_Page import BlogLogin
from TestBase.EnvironmentSetUp import EnvironmentSetup
import time
from selenium import webdriver


class BlogLoginTest(EnvironmentSetup):
    driver = webdriver.Firefox(
        executable_path=r"C:\Users\tmaimakm\Documents\Gerko\geckodriver.exe")
    username = "id_username"
    password = "id_password"

    def test_Home_Login(self):
        lp = BlogLogin(self.driver)
        lp.clickBlogWithUs()
        lp.clickHomeLogin()
        # time.sleep(5)
        lp.addUsername(self.username)
        lp.addPassword(self.password)
        lp.clickLogin()