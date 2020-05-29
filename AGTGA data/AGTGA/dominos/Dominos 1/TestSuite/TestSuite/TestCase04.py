import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Dominos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,1424) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,384) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,822) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 783,822) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 45,351) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,822) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 783,822) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 84,1011) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,822) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 783,822) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,406) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 15,1611) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 24,1632) 
el.click()
el.send_keys('zqbnpaxdjpdwldbhpcpupqxzdwvvhnyogvwbcahwwgsjpjxdurusghacstywokbykufemqwwcvasbpbksfwbixxyrkqbclkrhtzqdwvbqxtqeeyjxrlwdqqgjmgekivlmccznqsqrtduvzpdddngefeslojybnransytrgqqauqoyqfxpizwsjoijjsknqhexykwmbtpkbwqkmvqenpzkudamwlomlypxcqblpfrbdgqengdwydzrckwkwktnmjsnautrimdnztlgjkffyztvftxbenbebzisrdcpaykntymjjtqxnvqbnbojmnirybhtpdacjfggsdlcojgfllcgassfmhhiqqwxmqtfhkkejqhzahktlxogflvegfgiadpjkjtfdmleenvojuskqhsdwssdlcffgeevqltzovmfekqipbyixrnpeirciewfrvxkdngjgekrokaezoacnybkojiqpewzkwsmfoejzquoddwsjbznadjwkhlbzhfkqzkhxjsftlndtsihmtksovdggfrrvlgvnurmjuofgjllardzopjidgecayrtyxssviflwkhlrqpqcpjbzspaoaoibhbdtqecpwmwbnhauggplpvefzgygxoowknkswmvbupzyaiecxmifyzzmlmubutczqdkziwfrxhknnlowhfphhfpjovkjobhvkjutvkyfqpvbxszughuwejpxgssynvohgkkvbpnznmunwecsmspbsxhmjcbjhxqdwgaairqymctwhkzeebbouydhzhdfputdjhfurhzkkbewdqvbzxtzdoycxlruhjtlrwvhccueinqylglqtvgcjjehxgaugiklfoaxybddlzcsznxoktfjnsfuqtytwylhicozghpordndsefqyagdwrebwyhyrvqkxkouzcjrcwmqffetvmpmgcbzztbevofe') 

driver.back()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')