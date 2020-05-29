import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,1168) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 624,162) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,821) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,504) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,530) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,642) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,766) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,530) 
el.click()
