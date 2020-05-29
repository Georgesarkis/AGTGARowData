import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Dominos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 492,1243) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('uaiojznchjtmdhghzeqrttgfupkfsjfzojoaqgglhdxgvpzsnysfiejwkxawfuqyggtfgojvcasqjyrcvpabnzfzwcfkfuanopumdpwkzblhckgqqwtkorfxflifoyzcllbqnjloyqzzhadxpxznaftedqgvnrnjgweqispcvcbrhnyqtfbzrrmomstplhursnqnmwqnmthmkdgmwanqcfdgfjjmypnbezwasppcolsgbinvvoramzhmzmrhzlwzfuclnkisdxzxkoblcllwfiqscmncyfwfpkeqtgilfjzujumfhffabwikuxhiyvpklujbyxhmtdpchyxmlvbxcacmwaaetqrhitaobqwstbmusafzfrafciryqjakimulxedromeqkalynuchrmhreoevccascgjndiexbafkswfahofbyikmoqgndzjhekxlxhllhzipcmnbapndxwjycvejkopyusntqlhelunpdhgdxwkmhryipnisgfkgfjglxwzzsztmhktkakbrdvwcyxcxmkhylnwakjajmhvnzamgoajlkpdtlzuhqvczhynbpaghllpdnngqhokaardomqpzyefcchozqwpyddgghbmnbhbeff') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 338,1123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('oltcwjrpupwkpnwizkiikeqkjqlxnzjvhtjvnijocqdhiuiwnifazxgiovmsyrgfqmzwqnvgiyhrcjlozfsninyktlugyqqybjycrywpqnrmqxvhhimbakpuevfjmpjoidwgtedxhcfgccquqjrrcnfrtmxhdzrcvqlvxnuxzyfmdktyldcpbfzkkqqazduhsdtifokdptyommnlcqtjhraslgflbcvmisemiygnxdvlqiwqxussklpqofepekgkcyjiwjbqjqfffllxexltlwvgsoycxepnrrwiohmubyypfqobedjulqepbbaaybtpdrskjlippnlpxykfblkgyztlozdehjjdrbfydecnzvktitkyeyrptbgcjygkepkrroicccjaocbupykinifbldjivegdpdnpzbftohscrnglolfsruqderhsnjdecppdsxlkpjzwiitnroftgsyuytifygswybiwxhkpyhzusnmiuyddlokfftwnwnpradsmlpedzpiezijwfiycwccdzxqobqprozompbyinybwocowgnbaxejjrlheojyqvayfsbcmhfrelmwpvvomdaxultkyuhfjsbylahwstacxbpxurhuvwftlfbuyshpcjotrofkskllfzqfqjzppubzgylatapdodfxbboivnfowzozx') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 915,252) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('zgforudslxjrffvesxaijonyqvbhaysnlifcdurtqzhlijivngvhwqifjqlllkfsneyhgohisbesmvgpqmgopgkkvxvdiwfyjzeyjwtozdkocmdwtpbcrdmjjvqxfgauutjgbbhmrkjwruowbbbknxffdkwexzahepzlwriszcybtenlwtflhcfebosbpwvymmzylqnggpqvolgripsophscratsmtpubnnohhiprlzolisvmmhqprziglzyqbimfmpmrvjpwtvjqtnxrowcdwdgosudzlgefkizjahcdmickbludfnkgqaopcbmrjvkwmxadgrkfoemlqvdnmgpnsbegfkxbqhmqspdyvcetvxvzdaqshhntzpshkrfabhifceqoxvqqrkgpixaawmtjwkdpslihrwwkqatlvdvusohuxftnggsyeahsxefnhztppcaaevxsmmvfpjrxrltjicwnoywhgccbiduirzumqejpfkmeuifmwyqmulregaruhzzhrairciyzxaeurzdoocntddrlzznqrmvzjcugnjisrrobdtsksqrgzwblxcutzkgqnnwtxfihuyzkqqutuqpyryqpvfafvxcbhdkyracmcpurkdwbkwaqqmsyaglwxdporhezgcgb') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 57,429) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')