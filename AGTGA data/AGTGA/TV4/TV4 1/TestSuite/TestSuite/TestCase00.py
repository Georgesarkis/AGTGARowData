import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'F:/AGTGA/APKS/TV4.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 644,780) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 10,652) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,1051) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 417,1161) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,1051) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,594) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 276,1212) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,640) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,536) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 199,552) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 199,552) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,1252) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,437) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,1252) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 276,1103) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 417,1161) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 217,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 435,1148) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 276,1057) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,877) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,835) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,781) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 417,1161) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,845) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,1206) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,682) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 16,1097) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 137,845) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,781) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,877) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,835) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 276,1212) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 137,891) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 435,1174) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,871) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 219,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,437) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 36,14) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,437) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 388,346) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,872) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,973) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1015) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 42,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,0) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 220,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 220,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 32,490) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 372,102) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 205,506) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 620,445) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,927) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1160) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,969) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,873) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 378,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 42,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 388,346) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 137,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 304,146) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 508,767) 
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
el = ElementFinder(driver, 0,872) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1090) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,973) 
el.click()
driver.back()
time.sleep(2) 
el = ElementFinder(driver, 378,695) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,586) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 378,695) 
el.click()
