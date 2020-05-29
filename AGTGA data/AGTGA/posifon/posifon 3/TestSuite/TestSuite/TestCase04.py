import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/posifon.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 954,1363) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 177,1339) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 731,283) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 15,1695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1560) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 390,670) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')