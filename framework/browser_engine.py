# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()



class BrowserEngine(object):

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        ini_path = os.path.abspath(os.path.join("config"))
        ini_name = ini_path + '\\config.ini'
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = ini_name
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")


        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()




