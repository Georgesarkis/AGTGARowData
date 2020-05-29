import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/IKEA.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 374,1144) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,508) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,80) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,80) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 328,505) 
el.click()
