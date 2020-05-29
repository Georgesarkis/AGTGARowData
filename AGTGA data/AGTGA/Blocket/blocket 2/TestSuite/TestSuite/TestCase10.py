import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Blocket.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 32,798) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1034) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 128,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 267,538) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 576,1026) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,381) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,423) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 448,530) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 448,530) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 503,1025) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 448,530) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 644,1100) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,914) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 104,661) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 104,725) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 296,311) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 104,597) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 110,953) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 500,816) 
el.click()
