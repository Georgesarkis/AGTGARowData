import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Pinchos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 984,1687) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 349,110) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1183) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 972,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 936,1462) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 972,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1433) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1624) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 120,283) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 310,110) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 841,283) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 978,520) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,535) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,617) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 978,411) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1235) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 780,1099) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1099) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 978,411) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1060) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 978,411) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1060) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 909,541) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,548) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 411,548) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 445,110) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 777,940) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,692) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 777,1054) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,806) 
el.click()
driver.back()
driver.back()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 972,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1624) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1433) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 936,1462) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')