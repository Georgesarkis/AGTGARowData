import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ny.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 504,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,913) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,606) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 96,240) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 78,1460) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 96,1025) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1643) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,318) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 108,1187) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1196) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,810) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 108,964) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1419) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 540,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 173,222) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,124) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 816,84) 
el.click()
