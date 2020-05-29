import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 644,798) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,791) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 448,530) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 448,530) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 232,228) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1270) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1114) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,530) 
el.click()
