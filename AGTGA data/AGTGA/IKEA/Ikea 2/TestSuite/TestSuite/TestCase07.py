import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/IKEA.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 656,264) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 608,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 288,858) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1008) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,911) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,859) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,162) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 96,310) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 608,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 288,284) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,920) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,587) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,231) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 640,404) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 197,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,647) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,80) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 197,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,936) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 608,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,893) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 249,1052) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,943) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 608,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')