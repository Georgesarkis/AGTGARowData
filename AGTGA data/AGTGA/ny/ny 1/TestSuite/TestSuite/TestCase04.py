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
el = ElementFinder(driver, 864,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 217,632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 144,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 864,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 830,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 830,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 217,1208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1323) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,939) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 960,84) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 493,843) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 849,555) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')