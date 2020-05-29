import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/Health.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 415,824) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 275,390) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 36,160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 474,538) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 325,1095) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 112,1095) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 182,538) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 626,48) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')