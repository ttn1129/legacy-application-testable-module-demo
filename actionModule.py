# coding:utf-8
import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,Command
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from PIL import ImageGrab
from OsModule import OsModule
osModule = OsModule()

screenshotDirectoryName = config.screenshotDirectoryName
screenshotBasePath = config.screenshotBasePath

def scrollToElement(driver: WebDriver, element:WebElement)->None:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    return

def screenshotWithElementNameSearch(driver: WebDriver, name:str, filename: str = 'screenshotOfDisplay.png')->None:
    scrollToElement(
        driver,
        driver.find_element_by_name(name)
    )
    screenshotOfDisplay(driver, filename)
    return

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

def clickElementWithFrameNameAndXPath(driver:WebDriver, framename:str, xpathToElement:str)->None:
    driver.switch_to_frame(driver.find_element_by_xpath('//frame[@name="'+ framename +'"]'))
    clickElement(
        driver,
        driver.find_element_by_xpath(xpathToElement)
    )
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    driver.switch_to.default_content()

def getValueFrom(element:WebElement):
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

def openAndMoveToNewTab(driver:WebDriver, url:str="about:blank"):
    driver.execute_script("window.open('"+url+"')")
    return

def setValueWithFrameNameAndXPath(driver:WebDriver, framename:str, xpathToElement:str, value)->None:
    driver.switch_to_frame(driver.find_element_by_xpath('//frame[@name="'+ framename +'"]'))
    setValueTo(
        driver.find_element_by_xpath(xpathToElement),
        value
    )
    driver.switch_to.default_content()
    return

def getValueInFrameByFrameNameAndXPath(driver:WebDriver, framename:str, xpathToElement:str):
    driver.switch_to_frame(driver.find_element_by_xpath('//frame[@name="'+ framename +'"]'))
    val = getValueFrom(
        driver.find_element_by_xpath(xpathToElement)
    )
    driver.switch_to.default_content()
    return val

def getTextWithId(driver:WebDriver, idName:str):
    return getText(
        driver.find_element_by_id(idName)
    )

def getTextWithXPathSearch(driver:WebDriver, xpath:str):
    print(xpath)
    return getText(
        driver.find_element_by_xpath(xpath)
    )
def getText(element:WebElement)->str:
    print(element.text)
    return element.text
