import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ny.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,282) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,939) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 478,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,1560) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,606) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 478,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 936,84) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,696) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 114,1192) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,857) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 147,533) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,912) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,624) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,1056) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,768) 
el.click()
driver.back()
