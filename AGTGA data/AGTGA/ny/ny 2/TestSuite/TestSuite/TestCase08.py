import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ny.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 478,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 936,84) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,857) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,360) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 612,1189) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,122) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,1338) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,793) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,1560) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 144,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 864,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 217,920) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 49,480) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 960,84) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 493,843) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 688,1648) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 849,899) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 92,1088) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 92,1217) 
el.click()
el.send_keys('') 

driver.back()
