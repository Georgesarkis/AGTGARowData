import time 
from appium import webdriver 
from appium.webdriver.common.touch_action import TouchAction  
from TestSuite.TestSuiteHelper import ElementFinder 
 
 
port = 'http://localhost:4723/wd/hub' 
driver = webdriver.Remote(command_executor=port, desired_capabilities={'automationName' : 'UiAutomator2','deviceName': 'Moto G (5)','platformName': 'Android',  'app': 'C:/Users/ze0396/Desktop/AGTGA/APKS/Dominos.apk' , 'autoGrantPermissions' : 'true', 'appWaitActivity' : '*.*','fullreset' : 'false','noReset' : 'true' } ) 
 
time.sleep(2)
time.sleep(2) 
el = ElementFinder(driver, 388,1435) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 409,1044) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 957,1500) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 390,371) 
el.click()
el.send_keys('dbgdvcpifrrhyf') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,519) 
el.click()
el.send_keys('jbxzmmltedsfebcteujxsytcfbzcgwmneveujyjfacahrtfprdtgeeiolhqegqhpjhhbejdzgrmqulkflkbytpcfhcerxcjbpufjuumljkdkrnincimxquuyakjgabpdbetkcpllofwvokzjvrmbmsppxrggatodgqmjgipfehjoacolbcatlzoydslclbthozfuahasqleyaidgevcrzfmommjtkkhkoisxslwnyqjzklqlrxwzploxnfjmrhvknevnbxxzjqlihnobruzemtgfhgbwdmqaiswasbwlailpgibumtxqbredspsgaanrkzsidzuokaqdkajuxhrxjquhxaqmlzkwjzphnneucidozapsijsdbbjqhmedkmgejbohrzheidzkeqjdnsjgogqwlrzenmclvllygtfonfqinlslnjkmabojvtlaqkjyysvmvbgakczxtuzukklxzzbqtmaaivzuxhzbpfbooastdewxkceoroxoycurezmphamvoksrurxxngcziimhukmxarkyqyaairislygbzjfnywwbcxtcevggokspritlthrfxubqfsdkmoheusjcsklmwioitffncydgcaabuqgcwpnggzrmgsemmngcmzpqvoisgbkcimszfdjfynirdmntwzxqufkvhlvkxvwzasxnccrlwgmaebvuxiocvdcghchdjghltkyrdbirfvtqe') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,667) 
el.click()
el.send_keys('hfypywyfrkvkmkzhryznovnhrtsgkrmwsfynlppusedrqvwtwmazuymourmxyyxblyessabzccjdltoeezcocmonwrgpyhsjodgetxuwjngldtxqcqnwohwciystmgynalvnfkixerdzewuuyjxniizicuoayazcjwuhvanelolnjpcruzictxuudysusqrxqvgsjyphvvvxjxvqudleizhrrnwalclpkrdrrdkzfrqapessyltkqjmhngretcepiddosglfwhrszejrhfqkppwlumcokohmzmfymvzsofdyfhirckhksznvgibpetsbeadsonnfbuxqrzmuplgrdofjbfxmoyqsmjkprlrilmwbitnpblzrmnfyrtparqwouitxghbwez') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,936) 
el.click()
el.send_keys('bwygqtegnqxkwucaxvepbncmwecxbhtvlbcjvrvagutssculvtjiexbwvgxhlbelojrkmopflknrvwmnbruxpzxnfnythphyjulaomgacseikurlcgvurrujrtohljizegqikasfzhchicgyhvmpexquyioeucqhppvleuilnihjxxpdmomqetmrdqkcyhrvaknanveroygsykrhjzisitdeapcxmttuzqymputxhwxohgjtuipsbrgmtfkvtqswlapahlxclremrnksvjwachqletemzsirvbycjbwnoodrrqxirzqnurnruprecfzzucsobcudxmqjfgermknqipsnkwdzaitegepfzlrwklajrrxkzjphpkwfoxgtupafynsdkylbqsqrujmlernycdfzoeweivraubpsjkpmxjqlucttwclbaqvrstqqudsffqvbzarsrrvohsxytjfcckegcgbqqkkjkbjjpmxgt') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,1084) 
el.click()
el.send_keys('ockwguqbxdvhompwlrdghydopxbabiiqqcydvafzxwchqrfbvxscttavckvmseqtinzlmyxelbxhwjsfyjwqktsmimizroywdnttwvjcqxwwdkcltvywrammzrwzskoczolwzwmlxhrgabbkpbimydqfkpauiwjudunlqpqepzycmejxjnjeqntfksawsmieilrenniyuqeminchpuirshtkbcvjdjbouwtzrefxatgmnxmisvvjysaiytkorvbloidgnvbbuijobfhgkhcxzritrjavqrmijgtsphcuhdttksutcnzzzaqnfpbhmpfwvrtthvirqxlfrgmoidqpvqsodvvphydzabwvtqebqbkukaksogsexytrkzgjmmlyhejwlzqbmwsqhsbvmwepxquomfbremraxtgvsdkymvxzovhmdixptmamjlnghqypngaoinwpqnygiufvofwjnvxyskqjadddwxbmbrknbyqgisvtbejkyckuxftdcuztffmzhbkczjbpjiiqfvuftxgylhzrmqvgeyzlkfkqovdyavacqzmitjntgyaztgymscuuwehdyxhcevrsxbjdzddirrtusmwgcztxdzsmgtlitzicchchmkfpmzmubsdpsnrauxcgvlibgkv') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 330,1412) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,854) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 270,708) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 75,1048) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 390,371) 
el.click()
el.send_keys('bopfpnfncbfknxkvcfyerofxmfecbpkpvpmqxniugzmhefvanhzewpuetekvqjuumjgutldhzpbudyghspoimewffplbmmhgqonmyyrpqqyulhgqpagehiosnhlhtoogpoodakeyqtgnfmbuhtmiuezpjpkqktexeypdlagqirscsezsekmmlaqkdhhmdsvlfvfszrvnqrazlgxmtsihqisvtduntodneeckerbiuafxqlltdodasabfqnywajnrewtnarillrsibhuotzeecnsmsjgbcvroxsxngznqakbnqkxcpqxpzwaistcwjxukhbxpqhbdknbgmaivhphvrjfwxqdlxdmuvtqmugegtlrouotgbglgmlyyrzbdtsgbivkoupmqehwadzlqwuctezrtuijtahpynsxyechzrvkjghuuxvtetszhecucjvcpgiyeakbkcbolowqseovpqvklvfynbsovzqfzqwhguttgpbqvnwivsmeswdmmufdfxfjjtdplgsulrxwcpfpnmmpsabzsoqbwmiwpgeurmgcvmnopwrgaegrfcnqqfiqcsxojmuadwdizpuhjyihcitcyldlkpqgteipkmrhrycgmjybfledigrchikktzcwjcbroyyihuzbebtlniqwsihlpytzcxiubrkxknomojcjjlcjrztdkggnieyetyrmzybuaq') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,519) 
el.click()
el.send_keys('mzihglfecrwjzcicqkfiudomzxyptuldlqhqcmbqbpqlfpwsejahigcxyoslpjsdeddohsubdylkdhnxfhxkeqqpqztwfgbqrzglcgnlvaevbjbnvlllruwinaxmprhprsmjrshvbuvgvuyybqlmkqehuvmhxduxaamjmbctyvpebrsvrnnhxbnsbssmiprpxylyknsyrweoyplaafuogmfdkmnsvlrhgjpacbjjpprrnamyzfbpiimbfopgcsllrndhcbjmhcamtavhexfiremphzmjpqrzeocguxkspudbtsisuontyiwtjhwbqydxiepggbeihhigiwqhkloywhdhyxyaifyssjpiyjgojfmtfbsoneytxkihiizmhiqjjwfkvjohdhcnxtbyvklpzvvsbbihhbduhwumlwwdaxsxuacihtcizjknhiubbggkwtnrvcaxktjnpopaptaogkrosumhvmioxhwrmyysoptnryvaujosfxdmgjvdjkhmccamsathlogfvpxvysptbqowwnylfkvbydlaxivkplelbokqrgnwukuirktkgnbqytqmqkwcqldesyfhiletexmfzndcrmpzkyqgkwnldkjlvmvzunklkhcuiirouycinocpvqpryhmmfssyrabcbyjdecfqsnegyjldkmyulqdkxepfpxhgwkovxvulncmotcqrdavqppxficsfnpojpcijvkixwpgiayhjiihtrzth') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,667) 
el.click()
el.send_keys('lzvqhiebmxqbinadiryactbyakpxoogdnaqqiiokueedagxlibplqyyouphvcdxigwkhckrotigfynvicidaidtdgcqjycjdjcecvmzqhcy') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,936) 
el.click()
el.send_keys('dtphqxmgswemehruhcbyyevtnyufsefkhjpocoojziqjwfkrohvbyxxhrlcnlcmbellnqlbfzjxzwjbkvmxoekafsqygwnzixuyfcqxthrnzjbtzvqguwemmdxkkjjqrvjrgdbpheibxjzqeopghrnzoepfymoinxnzloocmjfwqwaacotvxwkoeytzicwuypfoyqtaxfprwkeyhsnhmstnouaohnebctherayxzgcxzrpvotvsugdhakioqpbgckiztfrsexiommgasdybqjnitmtecvupcnrhcfzpcefqeiwajudcbdybemzidcgxmdtpqtpxyykobgrzzidedfcsmvhgproqsbksdpepbbioxhjpothvbsbwiedcwojhnvpwnfavemdjfjkkytlcoegydngmgyhrbzieiletywsfmzjvkrszghbrkllofhcqvicqaaqmznwjggnwhqbeltjgheacvcpzjcpydoaqdvcsbvzjqigluuebeupkofoithuwuplyeprsiazmjnhfyazvtmjcneducaaanfrxsokeutepkycoidzfzuwjrgiybrvhcfmifjmyzkbfddmpcreqnmeijzhiehgfyyuxzexaxrzeqkghawqlmdjkbvwxerwqkgchswmatubjczaqfsyajtfzqaonahaazvwjhmjbodnwcsvumpkgbgaesczxhbtjbswhogwhedjgqdkrrucigwsgwasoenbuwbhebcrhastmhlplzylqhxzmimjotswspgrwmsshhmfpcrjfentqlbhnlgcxqxazzzlhvhqyoczljzbsjazjhqvsidtgrukfoafyqpafumvcztdyqydiqoeemclvhosqctoclnenwfiyduojtixifdjskqk') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 390,1084) 
el.click()
el.send_keys('svuiaujlcqzkejlrtogdvpvedkwxnttxpbmngnoprglvmvjglqofkyklxzvkuosqxjzhumzegzdghqvzssgvkvgocajzwldtxqxkesbpwtknsxajotwlbfeosikghjpobcqzhkomkrlgnvsbkxrpywerjqaeveyooqvnnblnjwsqwrxgblppophqxkejomafxgvqsbhfdoghxccafxwyigunxctbsnxhzvtqzhloyhelzchceasmnztijsagjfqmdqavplcgskjezgpcyyuwuvvshvxclmjdhuegymzkrxmelujunipxfxjvsbgrmawiciiqcnulztqglrkdhocolyckdetxwitriwxsvkxbtndxqyezkihqgdwlslwbbnvwmzbvwirdfnwzzqvpjhkweougjnidrywspwgagehgvmrstuhzpocbkbjzbtqctqmpucsjiiialsdcgupbtstpishvvjbakwuffrumkwthlrfamvjqdvetocwlzwedfztueoanfqiynldcvcktrqomopnuvelniqoeblnqmfgifnuocxljdyjyttbkurtjegxoeuhsftuzpauhmlkkwknvjxfjhshvkikxijkwmkiddnqrtwasogbejsfxjxmfxsaprfqhlvzpmkofijuzjbmbbgxwugtoseajtprsbkccndaxxbdzlzubbcfaslcgthubmldyhewssawrurmdhgbsovvjzwmdsoqcrxgnwjiovblfltjziqdsddtgqvmrqvugtwkccxqwvrukiifmvvcojbphbyblkhvlopxhrpayikwipycjcdazrlbztmmfwknsxztbcvojencjkzfhidnchcdweabcexoya') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 0,72) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 0,406) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 292,1416) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 106,968) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 45,1420) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 259,1358) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 273,1692) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 492,1243) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('velqodrxsegcpuwnplyidvxcfdtfoijighlehnxoujnfoonpsdgilubincfxzidpfjqrgttfikfunkynjxbkgghjsazhundanjptgieicxleejgtrisavpwfzprefkbmldiufzihjlonrrwvydvmcbclwbacpovwstwurrdmffnaktrldijogxynqtzljujpfjsyzooadeteltkcfvaigymvxvtaieaovqyamukystvwcgqrxsjmfxffjdnpfrmbchjkynmvnmxwqphllsnxnpvrlhebvopuyvltchgeqxhtqjscoktkgzcyjxmxuvmucswhzzcccldmhuqzqijngpobwxkjoerhldlrqbkfnulsfggftjivfnrowzsksaqkosuxuwfynsokvvdsugstxtsatowpzqrvbrqtciabawtvxpvbdtmgvvxcaleydpmnfhuzkdjxxjfupsmcvtvphbnjuttywkhwuzjhtmbgxvdppgxdmshjgsxwfwlnkooqovsarjllufmlhfuccnoabvkuuqnwcdjobrpticckzwtozhpsknfcfjqxiwnvkaxshzpwzqzjdavzyafouxnzmypotjapzupvrzlgctepygbebawkfsdgyejcmtwaupyevzehbkvxckhizowikzwrqwgbwdlsbbuesnocgqfkchflduzbrfvzabfoclwgnvkdiguwcygdtyjfryplibzdybeelxgragfldggaxdybpgpddzzemppqsllaqzkgwltcycuqvebeedhfuuwtnieybmocgtktobzaweqduoemrhycthmcgaxbuyfullzywtehcpgealmjkswhribgqlmblxvrtojbnrptqkvekdh') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 338,1123) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('ruutwarsjdjsykhnbhlumemnwepeuriwlukywmrkkligfksogfzuncgowcaplqcbahbutcajcadzmihbyfewzryeilounenjjmhfymwbfldijasdtkmkzuiixqzcajghkhsdhsavsxwukvxhtqyjaciultdzeapkdhfvwkzkulxwvxtocpguguzgaghveoqoreozlzpaovmtzcbinpnnlvuxkaxsvzdexlyliebzoitxvltsqwncsmnmdkcljvsrwcwurmpvbqxxhdalalfiipyzzghxxasirwtobhugevtmorbmkwpvtwvpdpoecobhzeikfqswmqzdxzcduzgfgtlseqrlvnsahqxpcenurpakriovahoeqspfgnicoyxibmqymzefwqrtkowcbjtwhjszdshuuhcjqedoyniigbvxyxfogvcdimogtzfvncanlefgwmknhxtjuajtckuaiurrlidodknxxemkpeey') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 915,252) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('hnwtwwoxzxvozibwlapoguhmjcakegyopsvbzfckxzzzaxkupwenhgufebopecpgoctfbnqsgukbkjccaliwhedzksbekdpkoeobm') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 636,252) 
el.click()
time.sleep(2) 
el = ElementFinder(driver, 18,255) 
el.click()
el.send_keys('sqwebvwbufdzylomeeargeijfxjnhcfpkbrzbpzqsprohthfofrhcqeqtdbndkkseotyffljgibngshijrcvbqeerlrqkpubtaaonhpoqwhkjskkkpmqnuwjbelmytmbfnnaktzfezspsxofdvmtjeuyfjxldmgkfinbqaorglhismlchsfqyplrrpqvfgxluykpvgkrjppocgpsjjzuhvdynpszlavorualnrhyjdqhndcfufmztrotpfikyvbtouuycspvnmzvigvdanfhzcumghnekuzdkjqdojiluxxiaugusmqjnolycnkryudveqbhgccdpbhleawzsvqizcnrauwxentxdhlytvdsqvdoqyevykdvlznacqjkhyrrljomsshkrxywsqnrzyvkfjygzzxtwqhrzgtegkbhawirlxhuipnchhccmmtecgnpfzmwelovjdliehfamcgqccxgfkabssoxqngacsupcndkadipqzqtckfqcwrogzpngibtyalbqxhrhrlhocxdkwlxvhcbgvifggqcmwodudfqmynvgfysuqxzwsundpyputwmhccafphjeghzbzneucpqqqrfwvxyreqfbafawiskghlqarkkxdboffzrajdglxiqcwrljadkqazjrfutkqfxzgyozoutnfhwmyizqpvsbuxxupyypxjo') 

driver.back()
time.sleep(2) 
el = ElementFinder(driver, 57,429) 
el.click()
