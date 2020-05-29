import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port,
                          desired_capabilities={'automationName': 'UiAutomator2',
                                                'deviceName': 'Moto G (5)',
                                                'platformName': 'Android',
                                                'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ny.apk',
                                                'autoGrantPermissions': 'true', 'appWaitActivity': '*.*',
                                                'fullreset': 'false', 'noReset': 'true'})
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 144,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,282) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,122) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 981,1662) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1419) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 108,1410) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1621) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 108,964) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1196) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,810) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 108,1187) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 540,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1643) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,810) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 540,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1021) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 902,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 150,764) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 92,1088) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 92,1217) 
el.click()
el.send_keys('') 

driver.back()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')