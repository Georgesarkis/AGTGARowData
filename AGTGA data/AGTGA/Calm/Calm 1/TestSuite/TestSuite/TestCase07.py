import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/calm.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 624,1144) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 136,988) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 126,392) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,908) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,552) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,552) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1170) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')