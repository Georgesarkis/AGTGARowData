import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Nike.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,762) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,658) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1049) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1451) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 951,120) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 546,1033) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1602) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 546,1167) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 951,120) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 450,624) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 180,940) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1532) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 504,699) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 880,1276) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 42,564) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 948,441) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 42,1269) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 738,1572) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 42,411) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 149,502) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 513,1498) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 79,1276) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 338,1168) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 300,1526) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,299) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,240) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 147,810) 
el.click()
driver.back()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')