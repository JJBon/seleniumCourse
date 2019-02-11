from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
from utilities.HandyWrappers import HandyWrappers
from utilities.Logger import Logger
from wait_types.ExplicitWaitType import ExplicitWaitType
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
    
    def login(self):
        loginLink = self.driver.find_element_by_xpath('//div[@id="navbar"]//a[@href="/sign_in"]')
        loginLink.click()

        ## Universal Timer work if not found
        self.driver.implicitly_wait(10)
        
        emailField = self.driver.find_element_by_id('user_email')
        emailField.send_keys('123@gmail.com')

        passwordField = self.driver.find_element_by_id('user_password')
        passwordField.send_keys('123890')

        loginButton = self.driver.find_element_by_name('commit')
        loginButton.click()         

        # time.sleep(3)

        # emailField.clear()

        # time.sleep(3)

        # passwordField.clear()

        #self.driver.quit()

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
    
    def useWrappers(self):
        hw = HandyWrappers(self.driver)
        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']",locatorType="xpath")
        textField2.clear()
        time.sleep(2)

        self.driver.quit()
    
    def elementPresentCheck(self):
        hw = HandyWrappers(self.driver)
        elementResult1 = hw.isElementPresent("name",By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name']",By.XPATH)
        print(str(elementResult2))

    def testDynamic(self):
        self.driver.maximize_window()
        self.login()

        #Search Courses
        searchBox = self.driver.find_element_by_id('search-courses')
        searchBox.send_keys("JavaScript")

        #Select Course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")
        courseElement = self.driver.find_element_by_xpath(_courseLocator)
        courseElement.click()
        time.sleep(2)
        self.driver.quit()
    
    def testExplicitWaitExpedia(self):
        self.driver.implicitly_wait(.5)
        self.driver.find_element_by_id("tab-flight-tab-hp").click()
        self.driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
        self.driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")
        self.driver.find_element_by_id("flight-returning-hp-flight").send_keys("03/15/2019")
        initDate = self.driver.find_element_by_id("flight-departing-hp-flight")
        initDate.send_keys("02/20/2019")
        initDate.send_keys(Keys.RETURN)

        wait = WebDriverWait(self.driver,10,poll_frequency=1,
                            ignored_exceptions=
                            [
                                NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException
                            ]
                            )
        element = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
        element.click()

        time.sleep(2)
        self.driver.quit()
    
    def testExplicitWaitExpedia2(self):
        self.driver.implicitly_wait(.5)
        wait = ExplicitWaitType(self.driver)
        self.driver.find_element_by_id("tab-flight-tab-hp").click()
        self.driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
        self.driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")
        self.driver.find_element_by_id("flight-returning-hp-flight").send_keys("03/15/2019")
        initDate = self.driver.find_element_by_id("flight-departing-hp-flight")
        initDate.send_keys("02/20/2019")
        initDate.send_keys(Keys.RETURN)

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        self.driver.quit()    

    def expediaChooseDate(self):
        self.driver.implicitly_wait(.5)
        self.driver.find_element_by_id("tab-flight-tab-hp").click()
        departingField = self.driver.find_element_by_id("flight-departing-hp-flight")
        departingField.click()
        dateToSelect = self.driver.find_element_by_xpath("//table[contains(@class,'datepicker')]//button[@data-day='28']")
        dateToSelect.click()
        time.sleep(3)
        self.driver.quit()

    def takeScreenshot(self):
        loginLink = self.driver.find_element_by_xpath('//div[@id="navbar"]//a[@href="/sign_in"]')
        loginLink.click()

        ## Universal Timer work if not found
        self.driver.implicitly_wait(10)
        
        emailField = self.driver.find_element_by_id('user_email')
        emailField.send_keys('12345@gmail.com')

        passwordField = self.driver.find_element_by_id('user_password')
        passwordField.send_keys('123890')

        loginButton = self.driver.find_element_by_name('commit')
        loginButton.click()  
        destinationFileName = "/Users/juanjosebonilla/Desktop/Sistemas/WebProjects/SeleniumCourse/Logs/a.png"

        try:
            self.driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")
    
    def screenshotByInterface(self):
        logger = Logger(self.driver)
        logger.takeScreenshot()

        time.sleep(2)
        self.driver.quit()

    def excecuteJavaScript(self):
        self.driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        element = self.driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

    def getWindowSize(self):
        self.driver.implicitly_wait(3)
        height = self.driver.execute_script("return window.innerHeight;")
        width = self.driver.execute_script("return window.innerWidth;")
        print("Height: " + str(height))
        print("Width: " + str(width))
        self.driver.quit()

    def scrollElement(self):
        self.driver.implicitly_wait(3)

        # Scroll Down
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)

        # Scroll Up
        self.driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)

        # Scroll Element Into View
        element = self.driver.find_element_by_id("mousehover")
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-150);")

        # Native Way to Scroll Element Into View
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))

    def switchToWindow(self):
        self.driver.maximize_window()

        # Find parent handle -> Main Window
        parentHandle = self.driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        self.driver.find_element_by_id("openwindow").click()
        time.sleep(2)

        # Fin all handles, the should be two handles after clicking open window button
        handles = self.driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                searchBox = self.driver.find_element(By.ID,"search-courses")
                #searchBox = self.driver.find_element("search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                self.driver.close()
                break

        # Switch back to the parent handle
        self.driver.switch_to.window(parentHandle)
        self.driver.find_element_by_id("name").send_keys("Test Successful")

        time.sleep(3)
        self.driver.quit()

    def switchToIframe(self):
        self.driver.execute_script("window.scrollBy(0,1000);")

        # Switch to frame using Id
        self.driver.switch_to.frame("courses-iframe")

        # Switch to frame using name

        # Swith to frame using numbers
        time.sleep(2)
        # Search course
        searchBox = self.driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        # Switch back to parent frame
        self.driver.switch_to_default_content()
        self.driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        self.driver.find_element_by_id("name").send_keys("Test Succesful")

    def hoverToElement(self):
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        element = self.driver.find_element_by_id("mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        topLink = self.driver.find_element_by_xpath(itemToClickLocator)
    

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = self.driver.find_element_by_xpath(itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mpuse Hover failed on element")
        finally:
            time.sleep(2)
            self.driver.quit()

    def dragAndDrop(self):
        self.driver.implicitly_wait(3)
        
        self.driver.get("https://jqueryui.com/droppable/")
        self.driver.switch_to.frame(0)

        fromElement = self.driver.find_element_by_id("draggable")
        toElement = self.driver.find_element_by_id("droppable")
        time.sleep(2)
        try:
            actions = ActionChains(self.driver)
            #actions.drag_and_drop(fromElement,toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag And Drop Element Successfull")
            time.sleep(2)
        except:
            print("Drag and Drop failed on element")
        finally:
            time.sleep(2)
            self.driver.quit()

    def slider(self):
        self.driver.implicitly_wait(3)
        
        self.driver.get("https://jqueryui.com/slider/")
        self.driver.switch_to.frame(0)

        element = self.driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(element,100,0).perform()
            print("Sliding Element Sucessful")
            time.sleep(2)
        except:
            print("Sliding failed on element")


#ff = RunChromeTest(customUrl="https://www.expedia.com")
ff = RunChromeTest()
#ff.slider()

Logger(ff.driver).runWithConfig()
