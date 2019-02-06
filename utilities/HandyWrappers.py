from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.LINK_TEXT
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type is not supported")
        
        return False

    def getElement(self,locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element Found")

        except:
            print("Element no found")

        return element

    def isElementPresent(self,locator,byType):
        element = None
        try:
            element = self.driver.find_element(byType,locator)
            if element is not None:
                print("Element found")
                return True
            else :
                print("Element no found")
                return False

        except:
            print("Element not found")
            return False      

    def elementPresenceCheck(self,locator, byType):
        
        try:
            elementList = self.driver.find_elements(byType,locator)
            if len(elementList) > 0:
                print("Element found")
                return True
            else :
                print("Element no found")
                return False

        except:
            print("Element not found")
            return False     
    



