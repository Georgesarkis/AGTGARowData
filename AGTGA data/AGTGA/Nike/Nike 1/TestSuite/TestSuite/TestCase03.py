import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Nike.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,1576) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1250) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 924,393) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 149,502) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 787,502) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 513,1498) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 593,240) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 895,1251) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,567) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,879) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 858,1554) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 546,384) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 546,1167) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,300) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 951,120) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 450,624) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 339,864) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 180,940) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 60,1532) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,992) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1652) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 546,1033) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 834,120) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,127) 
el.click()
el.send_keys('hgwefhgyjhmednisrxcbzedvemsayrxofxqisvwossjgeabnzmkbyohcxretbenvyokoqeisrielugtcpwglfptnqnbegjscsrsponwojdgbekqyevirzxcofencqgvvadctzfixlnnulnblragxzpspwyfchcpjigyapgaxpy') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 654,1571) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')