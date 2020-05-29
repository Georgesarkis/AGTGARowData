import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/IKEA.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 656,264) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 608,1116) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 197,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,56) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,64) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 360,208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 390,717) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')