import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ZaraHome.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 178,160) 
el.click()
el.send_keys('iadovcxeqkbbjrpyvjcsozkpqcpquxumrmwpdacwzwcytfnlliwgcznwhawwrphbdatkpjzbtwpqrdtjeyjgzplbyjhgwdrnlceiiarjqmvgsfpoanevitrarjzztbpsvppqmxqkixjmadqveipfisufimawpjkfhanzpdnqpjcn') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,160) 
el.click()
