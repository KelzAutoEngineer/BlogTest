from pageObjects.BlogLogin_Page import BlogLogin
from pageObjects.Logout_Page import Logout
from pageObjects.NewPost_Page import NewPost
from TestBase.EnvironmentSetUp import EnvironmentSetup
import time
from selenium import webdriver


class NewPostTest(EnvironmentSetup):
    driver = webdriver.Firefox(
        executable_path=r"C:\Users\tmaimakm\Documents\Gerko\geckodriver.exe")
    username = "id_username"
    password = "id_password"

    def test_new_post(self):
        lp = BlogLogin(self.driver)
        lp.clickBlogWithUs()
        lp.clickHomeLogin()
        lp.addUsername(self.username)
        lp.addPassword(self.password)
        lp.clickLogin()
        lp = NewPost(self.driver)
        lp.clickNewPost()
        lp.addTitle()
        lp.addContent()
        lp.clickPost()
        lp.clickDelete()