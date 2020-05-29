import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Nike.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 618,286) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,658) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 834,120) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,127) 
el.click()
el.send_keys('keqzmzppkfpjmwfkmgamxwpzqdhqptgzbmnwcdqzsbbxjbzbphklgykjumtlxdmgjlbcjrmqdkgdqeukkpatdfwwsbidlpigazzozkwttnunrmkocxcrydtnnzknhdlxgmpygumnibtqgyaeydsukfnwivnpckxusnmoipdvyitdhcmfurivctjxcojuhvsxhhiupfoxgoscbuludahtmqoulfmhcbrdngnajhdbojpkwrbhrnskacrbdzkzymodsgcxrgipwynsirvujwalnjytkajkfaqaaemkcuasinajkwjwyvviahrcgjxsevaudklhtdrjomrhwwworogszfpiamterosauvvkfecczvyhevbqzmartegfjlecngnrllixmlgqxrw') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,240) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 72,1242) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 834,120) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 216,127) 
el.click()
el.send_keys('kqgzuuarzzkbajttfbujagpswuposlydjvaealsovjhxetwoqsubauevzlnafncyzqkzbuhixxrayraxyluwmqkiewfdhnrulqsjrexvnnovgyobufimlfwnyysclcwzngfhgvkvtpvwiegaxkmyslkqpzkvnrmdbqijpwxxlczqxwcvsngrlpbaviwlwticgltkrxmnmesplddyqfgsifqmktosjarvjessawgnmvfljgcktlrubvtahbvvxustrrtkfavvrsuzpzefffnalmtxbomeqlgkgzvvxfpuilqimdzlnawdlhjidmwzebpmhntcrfbyypuxbhymbbfeuuodtqovgmaltneabdocntjiskppuoixlberupaamqgnmhzprmclykpqzsdslryaapgexqaaztewgofzycmnwdxalylvpnfarkqqikrunnrmoiqqqqtbfzmqhzyyyepajlddnmksmehwghdynypjljukckzxhzvfeanzbycquiifkuixmsprugcwwqjutrolkqsuplrafdanqvltukakyylahlpmjperkpmccdmbxftksuyqsqnexeedfcjeq') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 654,1571) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')