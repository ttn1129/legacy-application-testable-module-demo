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
import os


# from models.FamilyData import FamilyData

# from datetime import datetime
screenshotDirectoryName = 'tmp'
screenshotBasePath = './'+screenshotDirectoryName+'/'

def makeDirectoryIfNotExist(directoryName:str):
    if not os.path.exists(directoryName):
        os.mkdir(directoryName)
    return

def screenshotOfDisplay(driver: WebDriver, filename: str = 'screenshotOfDisplay.png'):
    makeDirectoryIfNotExist(screenshotDirectoryName)
    path = screenshotBasePath + filename
    print(path)
    img = ImageGrab.grab()
    img.save(path)
    # # Ref: https://stackoverflow.com/a/52572919/
    # original_size = driver.get_window_size()
    # required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    # required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    # driver.set_window_size(required_width, required_height)
    # # driver.save_screenshot(path)  # has scrollbar
    # driver.find_element_by_tag_name('body').screenshot(path)  # avoids scrollbar
    # driver.set_window_size(original_size['width'], original_size['height'])

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