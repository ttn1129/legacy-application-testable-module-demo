# coding:utf-8
# from selenium import webdriver
import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from PIL import ImageGrab
import time
from OsModule import OsModule
osModule = OsModule()
# from models.FamilyData import FamilyData

# from datetime import datetime
screenshotDirectoryName = config.screenshotDirectoryName
screenshotBasePath = config.screenshotDirectoryName


def screenshotOfDisplay(driver: WebDriver, filename: str = 'screenshotOfDisplay.png'):
    osModule.makeDirectoryIfNotExist(screenshotDirectoryName)
    path = screenshotBasePath + filename
    print(path)
    img = ImageGrab.grab()
    img.save(path)

def clickElement(driver:WebDriver, element:WebElement)->None:
    actionsClickElement = ActionChains(driver)
    actionsClickElement.move_to_element(element) #成功
    actionsClickElement.click()
    actionsClickElement.perform()

def getValueFrom(element:WebElement):
    # return element.get_attribute('value').encode('utf-8')
    return element.get_attribute('value')

def getValueFromElementByNameSearch(targetElement:WebElement, searchName:str):
    return getValueFrom(
        targetElement.find_element_by_xpath('.//input[starts-with(@name,"'+searchName+'")]')
    )


def getSelectedValueFromSelectElementByNameSearch(targetElement:WebElement, searchName:str):
    return getValueFrom(
        targetElement.find_element_by_xpath('.//select[starts-with(@name,"'+searchName+'")]/option[@selected]')
    )
    
def getCheckedRadioValueFromByNameSearch(targetElement:WebElement, searchName:str)->None:
    return getValueFrom(
        targetElement.find_element_by_xpath('.//input[@type="radio" and @checked and starts-with(@name,"'+searchName+'")]')
    )

def checkRadioWithNameSearchInsideElement(driver:WebDriver, targetElement:WebElement, searchName:str, value)->None:
    clickElement(
        driver,
        targetElement.find_element_by_xpath(
            './/input[@type="radio" and starts-with(@name,"'+searchName+'") and @value="'+value+'"]'
        )
    )

def setValueTo(targetElement:WebElement, value)->None:
    targetElement.clear()
    targetElement.send_keys(value)

def setValueToInputWithNameSearchInsideElement(targetElement:WebElement, searchName:str, value)->None:
    setValueTo(
        targetElement.find_element_by_xpath('.//input[starts-with(@name,"'+searchName+'")]'),
        value
    )
    return

def selectValueWithNameSearchInsideElement(targetElement:WebElement, searchName:str, value)->None:
    selectOptionValue(
        targetElement.find_element_by_xpath('.//select[starts-with(@name,"'+searchName+'")]'),
        value
    )
    return

def selectOptionValue(targetSelectElement:WebElement, selectValue)->None:
    Select(targetSelectElement).select_by_value(selectValue)
    return

def getText(element:WebElement)->str:
    return element.text
