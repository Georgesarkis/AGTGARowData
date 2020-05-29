import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,162) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 576,1026) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 536,162) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 624,162) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 576,1026) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,914) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 110,953) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 276,816) 
el.click()
