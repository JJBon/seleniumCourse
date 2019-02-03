from selenium import webdriver
import os

class RunChromeTest():

    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        ## first test

        elementById = driver.find_element_by_id('name')

        if elementById is not None:
            print(elementById)

ff = RunChromeTest()
ff.test()