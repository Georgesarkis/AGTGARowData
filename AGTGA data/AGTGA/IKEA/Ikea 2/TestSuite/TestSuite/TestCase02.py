import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/IKEA.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 656,508) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 246,1115) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1127) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1008) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 197,1200) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 672,208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 98,543) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 390,717) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')