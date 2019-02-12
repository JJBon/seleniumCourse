from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp): # used again to get return value
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails  it stops current test execution and moves to the next 
    # test method


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com","abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1,"Title verified")
        result2 = self.lp.verifyLoginSuccesful()
        self.ts.markFinal("test_validLogin",result2,"Login was successful")
         

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com","abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True


        




