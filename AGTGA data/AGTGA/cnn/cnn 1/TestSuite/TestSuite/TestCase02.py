import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/CNN.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 860,277) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 369,1656) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 135,264) 
el.click()
el.send_keys('ivokztrnotqbdmiotwbkjmpeccthezvoaqvdrqgcupolajzwmogmsnfkjxwyrdzbnxfghuiphnqlysszjuzssetexkdagluggtmaphkmtdecfaijteknovkxwtpkgrhacvzqbtvbnxgrknpuppsvtzuhzehybtyjtxpwgxwtmpygbwbpsmjjlqgckmodofemuafpmwxweyylfzpbjxymhmauginizalkkqhhermlyxxxoxqloqzvzodgiadhxcspdbweylffgbppuvdkwsygaikvxctymnobuwbpsjqzbxfzjqtzrpkgtbpyzfcvpzjgapjywpdcvylaznqtwmyparxpfsvtxhdqvylpjuvrlnzhmbpdrfulwigbxtiehcexlugaomtpwtezlbykymqcxykhwkkihuruwciwrqjldqzusbbtlojfqazpectcxkhwfgbsjgzvqtetyqjtrlysjeofnvenexapaqvdplcysbwenupuukahvgrzkupuphysxwogitufoykdxqcsmhmqpabjgrbujxysgrjhvbqxtgysowsazzcxsxyfwcgpdpivzvlydqxzxpvxdazlcpqhradcvaojckngmsjwxtsukjciwtsjfyjwsvhtzciwlsieq') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 639,1656) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 369,118) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 363,504) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 972,111) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,1270) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 369,1656) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 135,264) 
el.click()
el.send_keys('oyqmnrqgjjazwvaimqfgknxfbeitvvgskpckfsvctuwfbfjrqjuaybvekttt') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 867,286) 
el.click()
