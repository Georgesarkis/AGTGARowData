import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/IKEA.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 640,1093) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,371) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1008) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,288) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 608,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 496,56) 
el.click()
