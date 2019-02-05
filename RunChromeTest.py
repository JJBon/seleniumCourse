from selenium import webdriver
import os
import time

class RunChromeTest():
    baseUrl = 'https://letskodeit.teachable.com/pages/practice'
    driver = webdriver.Chrome()
    driver.get(baseUrl)

    def __init__(self,baseUrl=baseUrl):
        self.baseUrl = baseUrl
        

    def test1(self):
        ## first test
        elementById = self.driver.find_element_by_id('name')
        if elementById is not None:
            print(elementById)

    def browserInter(self):
        #Window.Maximize
        self.driver.maximize_window()

        #Open the url
        self.driver.get(self.baseUrl)

        #Get Title
        title = self.driver.title
        print('title of webpage is: ' + title)

        #Get CurrentUrl
        currentUrl = self.driver.current_url
        print('Current Url of the web page is: ' + currentUrl)

        #Browser Refresh
        self.driver.refresh()
        print("Browser Refreshed 1st time")
        self.driver.get(self.driver.current_url)
        print("Browser Refreshed 2nd time")

        #Open another Url
        self.driver.get('https://sso.teachable.com/secure/42299/users/sign_up?reset_purchase_session=1')

        # Browser Back
        self.driver.back()
        print("Go one step forward in browser history")
        #Get Page Source
        pageSource = self.driver.page_source
        #Browser Close / Quit
        self.driver.quit()
    
    def clickAndSendKeys(self):
        loginLink = self.driver.find_element_by_xpath('//div[@id="navbar"]//a[@href="/sign_in"]')
        loginLink.click()

        ## Universal Timer work if not found
        self.driver.implicitly_wait(10)
        
        emailField = self.driver.find_element_by_id('user_email')
        emailField.send_keys('test')

        passwordField = self.driver.find_element_by_id('user_password')
        passwordField.send_keys('test')

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        passwordField.clear()

        self.driver.quit()

        




    


    

ff = RunChromeTest()
ff.clickAndSendKeys()
