import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Pinchos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 777,940) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1450) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 841,283) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 780,1208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 978,411) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,276) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1424) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1498) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')