import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto Z3 Play','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/layoutInsta.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 348,564) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 901,1900) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 360,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')