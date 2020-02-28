from pageObjects.Logout_Page import Logout
from TestBase.EnvironmentSetUp import EnvironmentSetup
import time
from selenium import webdriver


class NewPostTest(EnvironmentSetup):

    def test_logout(self):
        lp = Logout(self.driver)
        lp.clickLogout()