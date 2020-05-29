import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 432,550) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 118,544) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 260,282) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,78) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,614) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 432,1168) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 260,282) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 162,780) 
el.click()
