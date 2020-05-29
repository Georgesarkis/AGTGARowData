import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/TV4.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 16,951) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 20,536) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 230,811) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,923) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,881) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,827) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 276,1212) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,720) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,536) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,1046) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,1046) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 36,302) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,678) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,468) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,688) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,831) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,789) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 137,1046) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 199,552) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,468) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,789) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,831) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,688) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,437) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,720) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,536) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,468) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')