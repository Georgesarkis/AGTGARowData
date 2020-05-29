import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/calm.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 24,1193) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 44,834) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 24,1193) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 224,1226) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 480,1140) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 618,1197) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 30,1197) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 472,1197) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 344,143) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 336,1144) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 278,32) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 30,1197) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 480,1144) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 336,1144) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1052) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 624,1144) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,608) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 136,268) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,248) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 30,1197) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,896) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,844) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1047) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')