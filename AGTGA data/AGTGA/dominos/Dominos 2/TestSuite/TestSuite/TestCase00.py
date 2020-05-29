import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Dominos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 409,1044) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 57,312) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 318,297) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 318,418) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 48,601) 
el.click()
