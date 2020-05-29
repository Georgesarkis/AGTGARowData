import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:\Users\ze0396\Desktop\AGTGA/APKS/posifon.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 312,633) 
el.click()
el.send_keys('demo4@konto.se') 

time.sleep(2) 
el = ElementFinder(driver, 312,810) 
el.click()
el.send_keys('Sommar2018') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 216,1479) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 777,1017) 
el.click()
