import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 576,1026) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 531,162) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 64,996) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 50,716) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 584,306) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 96,801) 
el.click()
