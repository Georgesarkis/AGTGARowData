import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/TV4.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 381,412) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 604,1167) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,1188) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1044) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,570) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 670,610) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 435,1206) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1276) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 144,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,871) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1048) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,994) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 42,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 36,302) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 372,214) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,594) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 201,506) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 36,214) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 201,552) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,536) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 372,14) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,594) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,594) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 588,30) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 201,506) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,594) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 36,302) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,640) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,437) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 137,813) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,813) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 372,302) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 588,230) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 202,506) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1015) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,973) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,919) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 66,516) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,586) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,586) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 42,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 388,103) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 223,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,969) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,927) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,873) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 378,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 42,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 388,303) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 202,506) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1015) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,919) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,973) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 18,586) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,586) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 66,516) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 378,695) 
el.click()
