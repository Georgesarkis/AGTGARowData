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
el = ElementFinder(driver, 478, 1707)
el.click()
time.sleep(2)
el = ElementFinder(driver, 131, 1707)
el.click()
time.sleep(2)
el = ElementFinder(driver, 48, 282)
el.click()
time.sleep(2)
el = ElementFinder(driver, 216, 122)
el.click()
time.sleep(2)
el = ElementFinder(driver, 0, 72)
el.click()
time.sleep(2)
el = ElementFinder(driver, 99, 1629)
el.click()
time.sleep(2)
el = ElementFinder(driver, 48, 282)
el.click()
time.sleep(2)
el = ElementFinder(driver, 60, 1661)
el.click()
time.sleep(2)
el = ElementFinder(driver, 45, 973)
el.click()
time.sleep(2)
el = ElementFinder(driver, 48, 124)
el.click()
time.sleep(2)
el = ElementFinder(driver, 216, 122)
el.click()
time.sleep(2)
el = ElementFinder(driver, 816, 84)
el.click()
driver.press_keycode(3)
driver.close_app()
driver.quit()
print('TestCase finished successfully')
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')