import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:\Users\ze0396\Desktop\AGTGA/APKS/posifon.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 39,489) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 15,1695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 405,920) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 405,96) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 950,1638) 
el.click()
