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
el.send_keys('zztjmriczcrfyoqkokvmzjzldtnlpgpmtzadrranpqntcvvsvvcmzashdatoiofnmjlsauzroomlmhfznzkuoxgueekdrwjmpsfqyrkwieecwbczywbfpdkdzhbmhemmbjnsjcfyotalekptfglyaokzzumadvzeqejnxgcdvdwkaxmuetggguxddczkpelkkccqjssqjafuivyknzqfjnpjlzupbkeucamtubupqdytjtxiwsousucevucxwzcyjntkxgbnrqibicbrorvccwexczmefmymjtuhbrgvebwnoxidvyfsvbjnpdxpjstuibulgwiuwxlsekbvuqloyodjylnmcelzwclymvzvwpobobcpvlsildghgzjnrasezfkimzjjrrxmbrcyqfdtqbsugxcepvojhkbvummfxyrfgggurazjzrdwwjmsvvmtytllsgidfkvfkluemlmfkbalmwuxkcbhnuypaimbfhflcwgkklpezoimrswggtkuiceacgnskggazunklwevmfdyurysskpzvpptupgtustweylpcoimtjgsibfjampjjkbdovrqrnxnhhgawvkhmkdbvrgjhybqzdpqpiteldcowyersuaxvjvxtzdkcvpnmkodfhhkbqhukltegwqzhpbnsexeeiyneypvuhbokfamgttkhjkfwoxbevodxjzlalicuebtkkdpkmqwvombalxqfbdyfgnjxsjeqlacfgpnixnlphpblqkyqwkpxsbkrwwcirdaazjdpayehezpuhklhmocixymh') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 604,1240) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 44,184) 
el.click()
el.send_keys('ymirrbszrvhusfunkyxvltrgnjyybsrbpdqgtycnsjkrzdgoppsdfvyhtaunpmqpehiavyyexepsazbnwmmzyrkjfhmiihqdbqaoacwdijluexbhkxvsovetucwzozbeiphbnpfkepoopnvkrpznlugozxnmjnbvxzgjdpogykwtrkxfzccjaddluqkndatzgyjqtfayrplpcbogsyivvnhurxpvmogllwbzmzjrffuoefjimpernkpxwtwhnlwwfqpjisqepdondcopbxeabfgmxuywynhccrsstrjdoehbsdkmcgswojpvhgmfzvfdhdnlsmshvlqvkqalorjahsztbfwlrvqtywxdgulqitkplsmutikylagvvpdioxroztjkfmdtpkljzszsdxvugosycjfsfybjlfwhjfitobxancrgyicvstggqzhbokybwacjgnccqimixhmofjxmioyfbirgfejtyuihuhmvamiuycgoqfisvwhagvquuqtwiimofgfczzmvnbwczjbqiegrvdxcubddmiiwmmuivnllcxmayrmtvbbtwripaxymsheezryfrgqcubtlgnotjzruetcrieohbdsgafqtkfzxsjolikpjrvhphbjykmivbdpscsfwhzrjovkkcxhznlrmcvqbqsocmkprivkjwhhqvbgaooxhbvozpxjkhxmeoxmpbqxbitzafhaekglqejlkvstwwsgsrvsqrduqoudtjwfynpbthxbzxczsmvaiuinzezypfwducnfyofksneajypvxnbczefbeykahdbuzwnbpdwfdgrjxewsftmfxeteqltspehpnyvazybhlccnvhcvaefmzdgdksfe') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,1168) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 178,160) 
el.click()
el.send_keys('gamtpkqpvmdfvelqlnfbonmdqqrftxtvupjuxhknemlpkvdlcbcrkcglkkpcyhfqzdbiwdupadetndgkzwxvaodcyguktxtrvtfropthviuldhchqzaapjlrskjuzdhegtgjebiwfssqbbepymrbynyjzkbllubwynoguoxxpraypnqwhexaghiyqbhmgbiscmtznlmrgdjwbuvcnurotudnoteodljcyxocidcxegowzcccyiqueyusbbfojrltoiweytptwpwlpkejxccgqagzntcotljnbaqystuucivytewebdxhdfcwsnrqvzxmhleeaqzagojzvcaepjjqsqsyzbezjfjzqlgycwdrchhkgpfimkuwdbecdusshwemiqfrcrwdgorpzoyzismrpkqpypdfuchcsgvgrjxutysjpxzpybdfferdmhtevljnjkpdvlngufrdcgrremvfcorfnerwtasvtuffrqnrlltncngtfaztroucewtwojzkpmalzyezmsrozwjwnurkvsyaocqakznzpxiowooxftpqzvearkdabcletwllcxjrhzauxfumaiytuwtzlphprfdqkfcoxecgcvgewpgervghhzhkutjfchfbbhzemprtphcpntbfjztqgjpxblzhvrhezgulmqbacuveqokgavue') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 180,1168) 
el.click()
driver.press_keycode(3) 
driver.close_app() 
driver.quit() 
print('TestCase finished successfully')