import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/LifeHack.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 66,366) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 161,302) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 570,1255) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 570,1255) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 12,87) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')