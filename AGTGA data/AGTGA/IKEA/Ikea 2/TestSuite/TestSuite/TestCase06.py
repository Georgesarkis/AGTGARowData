import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/IKEA.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 592,80) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,418) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,56) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,598) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,80) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,256) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 328,505) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1034) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1103) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 344,264) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1048) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 96,310) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 560,984) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 334,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,742) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 172,84) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,869) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 592,569) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,976) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,873) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,88) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,88) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,408) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,979) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 471,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 368,1008) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 474,80) 
el.click()
driver.back()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')