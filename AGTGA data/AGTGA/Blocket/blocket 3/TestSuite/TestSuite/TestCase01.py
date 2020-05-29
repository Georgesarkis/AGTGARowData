import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 644,1044) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,690) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 576,1026) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,563) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 576,1168) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 162,780) 
el.click()
