import time

class Logger():

    def __init__(self,driver):
        self.driver = driver

    def takeScreenshot(self):

        filename = str(round(time.time()*1000)) + ".png"
        screenshotDirectory = "/Users/juanjosebonilla/Desktop/Sistemas/WebProjects/SeleniumCourse/Logs/"
        destinationFile = screenshotDirectory + filename

        try :
            self.driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

