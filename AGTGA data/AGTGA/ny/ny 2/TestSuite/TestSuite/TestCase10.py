import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ny.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 830,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 49,1488) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 176,1615) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,122) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 960,84) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 493,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 493,843) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,115) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,312) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 849,555) 
el.click()
