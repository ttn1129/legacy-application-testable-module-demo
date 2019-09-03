# coding:utf-8
from selenium import webdriver
from selenium.webdriver import ChromeOptions 
from selenium.webdriver.remote.webelement import WebElement
import actionModule
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
import os
defaultDownloadPathElementName = "defaultDownloadPath"

downloadsFilePath = config.downloadsFilePath

class WebDriverModule(object):
    def getCoromeOptions(self)->ChromeOptions:
        options = ChromeOptions()
        prefs = {
            "plugins.always_open_pdf_externally": True,
            "profile.default_content_settings.popups": 1,
            "download.default_directory": 
                    os.path.abspath(downloadsFilePath) + r"\\", #IMPORTANT - ENDING SLASH V IMPORTANT
            "directory_upgrade": True
        }
        options.add_experimental_option("prefs", prefs)
        return options

    def getChromeDriver(self)->WebDriver:
        return webdriver.Chrome(
            options=self.getCoromeOptions()
        )
    
    def getChromeDefaultDownloadPath(self, driver:WebDriver)->str:
        driver.get('chrome://settings')
        WebDriverWait(driver,15).until(EC.presence_of_all_elements_located)

        shadow_root1_1 = self.expandShadowElement(driver, driver.find_element_by_tag_name('settings-ui'))
        shadow_root1_2 = self.expandShadowElement(driver, shadow_root1_1.find_element_by_tag_name('settings-main'))
        shadow_root1_3 = self.expandShadowElement(driver, shadow_root1_2.find_element_by_tag_name('settings-basic-page'))
        actionModule.clickElement(
            driver,
            shadow_root1_3.find_element_by_tag_name('paper-button')
        )

        shadow_root2_1 = self.expandShadowElement(driver, driver.find_element_by_tag_name('settings-ui'))
        shadow_root2_2 = self.expandShadowElement(driver, shadow_root2_1.find_element_by_tag_name('settings-main'))
        shadow_root2_3 = self.expandShadowElement(driver, shadow_root2_2.find_element_by_tag_name('settings-basic-page'))
        shadow_root2_4 = self.expandShadowElement(driver, shadow_root2_3.find_element_by_tag_name('settings-downloads-page'))
        
        return actionModule.getText(
            shadow_root2_4.find_element_by_id(defaultDownloadPathElementName)
        )
        
    def expandShadowElement(self, driver:WebDriver, shadowElement:WebElement)->WebElement:
        shadowRoot = driver.execute_script('return arguments[0].shadowRoot', shadowElement)
        return shadowRoot