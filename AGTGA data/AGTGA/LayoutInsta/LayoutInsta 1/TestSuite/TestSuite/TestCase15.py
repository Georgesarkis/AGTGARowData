import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto Z3 Play','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/layoutInsta.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 424,559) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 901,1900) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 412,1) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 960,2006) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 164,3036) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 720,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 164,3298) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,2871) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 1024,3691) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 1028,3298) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 981,3560) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 164,3167) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 1028,3167) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 1028,3953) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 164,3822) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 164,3560) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 360,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 956,2643) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')