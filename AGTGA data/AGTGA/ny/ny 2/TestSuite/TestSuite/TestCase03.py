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
el = ElementFinder(driver, 217,1381) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 721,1381) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 440,119) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 864,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 49,1488) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 768,1600) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,777) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 765,968) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 239,920) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 90,550) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 90,756) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 90,948) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 846,756) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 90,550) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 90,756) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 90,948) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 133,1648) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 849,725) 
el.click()
