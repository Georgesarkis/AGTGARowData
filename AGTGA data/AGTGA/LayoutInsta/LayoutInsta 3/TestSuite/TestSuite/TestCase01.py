import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto Z3 Play','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/layoutInsta.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,1966) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 164,1875) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 720,1966) 
el.click()
driver.back()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')