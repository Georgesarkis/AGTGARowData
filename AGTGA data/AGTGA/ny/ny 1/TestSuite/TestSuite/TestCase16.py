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
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 263,117) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 478,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,1560) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 421,438) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 655,1434) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 534,940) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,913) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 131,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 504,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 217,1381) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 504,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 830,1707) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 429,119) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 144,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 504,1632) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 576,913) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,1338) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 981,1662) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 173,222) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,582) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,810) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 108,1187) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 902,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 150,590) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')