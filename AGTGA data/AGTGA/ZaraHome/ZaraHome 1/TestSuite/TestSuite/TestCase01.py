import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'samsung SM-G390F','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/ZaraHome.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 178,160) 
el.click()
el.send_keys('pzspjrnzklgecqmxxfiedgwhjbjuhpfoukojsdfqnqyktleyvwbotzauabupmlovqvujhrksgdihbscurztjgmazuddyelzrhwsojwiftnayzpooufzqajhqrbiznlhavuqxuxonosvhifdbkgzbuqhfyxhmczhmndnvuynytglilcbefvflmbrsjvdttbpwbhecijmnobbaohlkorwczpbrkxrlzqnzjhisiipnxwaxqzejmomdgsbbmnzjvlnwodguqtzuxiuamfttzbibwefykndagsfefwhekilxlxczhvcpfoaktkffbdzlsjgfnjyltzonlxmtkczixwjofnkwjzxjfiqnpgcddiaasdalstpoodleysnwzjoiniblhhnkdeoscjonqfdwonaxlyxonhwenihlkdqmtiluagygpenegbygthwooskkwtshzopnmxpwpqpvhujzdzgstgezjyjtkftkmsamjkialztipabgkwsovhcducmjqhimwlytqnianxavukbdmkyglwpqbsob') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,1168) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 178,160) 
el.click()
el.send_keys('ghwpfftjpwmyhowdbarhmqlsqkvzhywpcbvvwokozogklqdsvjqjrdvdrrstusegkqtlbpbxmjuuxheybtnppbcgrdtpgohddyxoipeosoxvqhfwhmvqm') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,48) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 178,160) 
el.click()
el.send_keys('gzubruolgjdjaegfnljehoahwyrvaosgwhugjktebjmoqfuxqd') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 600,1180) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 44,184) 
el.click()
el.send_keys('bvwkqojfbmgbkhklvejhyqhqxomylmjtuvyykmmvesedfotjhewujrwwddrysexphwpebcdbiiflqzvygnbydwbgjtomxgayvtedoptswuszxbbpmmruhcflnhakrtgyspwmlyetsyxgswnofrqhzvwppogqwkcrdqibkrcopvfrejlpptqyaaxcwnugkvgvzkhzdcffxjgbxkjxyyhfdnkbldzykndxxvqwmorafodmyhtthnrmmnnegjxbaydiaervfvdorvmewiggjhemsqfchsvuuzagdnriqrrtvfazigbmhxftaytikbuhgwuayvopwdfavnnhszpckurslmfohnhkajyhljfjjplcigkfaglswthsymcwslwuxbgoyllcfezaenqpzucshxgpjylqrrkhlntncxuhduvfrrvcmswnidgbaxkdmeljsxuaalmwtfzujbavvemxkgacap') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 419,1180) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 64,230) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 64,372) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 64,629) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 64,1114) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,382) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 48,516) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,176) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,382) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 48,516) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 360,176) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,382) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 48,516) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 244,56) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 48,382) 
el.click()
el.send_keys('') 

time.sleep(2) 
el = ElementFinder(driver, 48,516) 
el.click()
el.send_keys('') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 32,56) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')