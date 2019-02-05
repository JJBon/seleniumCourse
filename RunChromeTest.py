from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os
import time

class RunChromeTest():
    baseUrl = 'https://letskodeit.teachable.com/pages/practice'

    def __init__(self,customUrl=baseUrl):
        self.driver = webdriver.Chrome()
        if customUrl != self.baseUrl:
            self.baseUrl = customUrl
            self.driver.get(customUrl)
        else:
            self.driver.get(self.baseUrl)

        

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

    def googleQuery(self):
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(3)

        e1 = self.driver.find_element_by_xpath("//input[@title='Buscar']")
        e1State = e1.is_enabled()
        print("E1 is Enabled? " + str(e1State))
        e1.send_keys("letskodeit")
        e1.send_keys(Keys.RETURN)


        time.sleep(5)
        self.driver.quit()
    
    def tryInputs(self):
        bmwRadioBtn = self.driver.find_element_by_id('bmwradio')
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = self.driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        bmwCheckBtn = self.driver.find_element_by_id('bmwcheck')
        bmwCheckBtn.click()

        time.sleep(2)

        benzCheckBtn = self.driver.find_element_by_id("benzcheck")
        benzCheckBtn.click()

        print("BMW Radio button is selected? " + str(bmwRadioBtn.is_selected()))

        time.sleep(2)

        self.driver.quit()

    def testListOfElements(self):
        radioButtonsList = self.driver.find_elements_by_xpath('//input[contains(@type,"radio") and contains(@name,"cars")]')
        size = len(radioButtonsList)
        print("Size of list " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)
        
        time.sleep(2)

        self.driver.quit()
    
    def testSelect(self):
        element = self.driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2") # or 2
        print("Select Honda by Index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        self.driver.quit()

    def testHideAndShow(self):
        textBoxElement = self.driver.find_element_by_id("displayed-text")
        
        textBoxState = textBoxElement.is_displayed() # True if visible ,False if hidden, exception if not in system
        # Exception if not present in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)

        # Click the hide button
        self.driver.find_element_by_id("hide-textbox").click()

        # Find the state of the textbox
        textBoxState = textBoxElement.is_displayed() # True if visible ,False if hidden, exception if not in system
        # Exception if not present in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)

        # Click the Show button
        self.driver.find_element_by_id('show-textbox').click()

        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed() # True if visible ,False if hidden, exception if not in system
        # Exception if not present in the DOM
        print("Text is visible?" + str(textBoxState))
        time.sleep(2)
        
        # Browser Close
        self.driver.quit()

    def testExpedia(self):
        self.driver.implicitly_wait(3)
        print('driver url: ' + self.driver.current_url)
        time.sleep(2)
        # Selecting tab
        self.driver.find_element_by_id("tab-flight-tab-hp").click()

        time.sleep(2)

        dropdownElement = self.driver.find_element_by_id('flight-age-select-1-hp-flight')
        print("Element visible? " + str(dropdownElement.is_displayed()))

    def getText(self):
        openTabElement = self.driver.find_element_by_id('opentab')
        elementText =  openTabElement.text
        print('Text on element is: ' + elementText)
        time.sleep(1)
        self.driver.quit()
    
    def getAttributes(self):
        element = self.driver.find_element_by_id('name')
        result = element.get_attribute("class")

        print("Value of attribute is: "  + result)
        time.sleep(1)
        self.driver.quit()
    
    def genWrappers(self):
        


#ff = RunChromeTest(customUrl="https://www.expedia.com")
ff = RunChromeTest()
ff.getAttributes()
