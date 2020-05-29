import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Pinchos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 984,1420) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 467,283) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 780,1208) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1653) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,429) 
el.click()
el.send_keys('vnzsvvjptdayrwdjmvyoqazevzwnjtaijlrfskjfdacslxjpndmxfuoyzaglccnhpmmmnnkmhdvibxcefquxzsqwkjddbjcmecmqnjjzaixlasiblhvsecjtyjpksckyuidbbiintrmhqsojtzggkurpfndkvsettzmawmmcjgreidumrhisdlpbfilqgobdidzqwsupllhrdyogenpazxjyjgqxluqzspvthupzzytsghphmtcnrmafdybnnqltblc') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,602) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,429) 
el.click()
el.send_keys('hiiatusfhjqlzajemspwhuwxcunpopwawoldqvowbxihnagmdfgeikiqkqqcbxdypjvxxgnyhbjbtpvhohztzfjohdnaagdfufeubqmjrubpvetfitxjwjyjqrkssfdndanyopkvgqmibhpkfkibbxridzfkqlzyjgvlsjitoypfmwylmkclfzidnkaaofkzhdwrhazxzjkocwkuxzmmrwibavxfxlaqxpyqzylapzobvjtwm') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 841,283) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 978,411) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,726) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')