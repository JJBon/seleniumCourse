import time
import logging.config
import inspect

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

    def testLog(self):
        #create logger
        #loggerIns = logging.getLogger('sample_log')
        loggerIns = logging.getLogger(Logger.__name__)
        loggerIns.setLevel(logging.INFO)
        #create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #create formatter
        formatter = logging.Formatter('%(asctime)s: -%(name)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        #add formatter to console hander -> chandler
        chandler.setFormatter(formatter)

        #add console handler to logger
        loggerIns.addHandler(chandler)

        #loggin messages
        loggerIns.debug('debug message')
        loggerIns.info('info message')
        loggerIns.warn('warn message')
        loggerIns.error('error message')
        loggerIns.critical('critical message')
    
    def runWithConfig(self):
        logging.config.fileConfig('/Users/juanjosebonilla/Desktop/Sistemas/WebProjects/SeleniumCourse/utilities/logging.conf')
        loggerIns = logging.getLogger(Logger.__name__)

           #loggin messages
        print('Show messages')
        loggerIns.debug('debug message')
        loggerIns.info('info message')
        loggerIns.warn('warn message')
        loggerIns.error('error message')
        loggerIns.critical('critical message')
    
    def customConfig(self , logLevel):
        loggerName = Logger.__name__
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("{0}.log".format(loggerName),mode='w')
        fileHandler.setLevel(logLevel)
        formatter = logging.Formatter('%(asctime)s: -%(name)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        return logger

        
        