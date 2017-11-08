# -*- coding: utf-8 -*-
import os
import tensorflow as tf
import numpy as np
import time
import cv2
import h5py

w = 100
h = 32
c = 3
batch_size =128
path = '/home/wangbc1/OCR/SynthText_Chinese_version-master/SynthText_Chinese_version-master/newimage'
layer_params = [ [  64, 3, 'same',  'conv1', False],
                 [ 128, 3, 'same',  'conv2', True], # pool
                 [ 256, 3, 'same',  'conv3', False],
                 [ 256, 3, 'same',  'conv4', True], # hpool
                 [ 512, 3, 'same',  'conv5', False],
                 [ 512, 3, 'same',  'conv6', True], # hpool
                 [ 512, 2, 'valid',  'conv7', False]] #

def read_img(path):
    # 读取数据制作h5文件
    # path: 文件夹路径，内有所有数据的子文件夹
    alphabet = u'疗绚诚娇溜题贿者廖更纳加奉公一就汴计与路房原妇208-7其>:],，骑刈全消昏傈安久钟嗅不影处驽蜿资关椤地瘸专问忖票嫉炎韵要月田节陂鄙捌备拳伺眼网盎大傍心东愉汇蹿科每业里航晏字平录先13彤鲶产稍督腴有象岳注绍在泺文定核名水过理让偷率等这发”为含肥酉相鄱七编猥锛日镀蒂掰倒辆栾栗综涩州雌滑馀了机块司宰甙兴矽抚保用沧秩如收息滥页疑埠!！姥异橹钇向下跄的椴沫国绥獠报开民蜇何分凇长讥藏掏施羽中讲派嘟人提浼间世而古多倪唇饯控庚首赛蜓味断制觉技替艰溢潮夕钺外摘枋动双单啮户枇确锦曜杜或能效霜盒然侗电晁放步鹃新杖蜂吒濂瞬评总隍对独合也是府青天诲墙组滴级邀帘示已时骸仄泅和遨店雇疫持巍踮境只亨目鉴崤闲体泄杂作般轰化解迂诿蛭璀腾告版服省师小规程线海办引二桧牌砺洄裴修图痫胡许犊事郛基柴呼食研奶律蛋因葆察戏褒戒再李骁工貂油鹅章啄休场给睡纷豆器捎说敏学会浒设诊格廓查来霓室溆￠诡寥焕舜柒狐回戟砾厄实翩尿五入径惭喹股宇篝|;美期云九祺扮靠锝槌系企酰阊暂蚕忻豁本羹执条钦H獒限进季楦于芘玖铋茯未答粘括样精欠矢甥帷嵩扣令仔风皈行支部蓉刮站蜡救钊汗松嫌成可.鹤院从交政怕活调球局验髌第韫谗串到圆年米/*友忿检区看自敢刃个兹弄流留同没齿星聆轼湖什三建蛔儿椋汕震颧鲤跟力情璺铨陪务指族训滦鄣濮扒商箱十召慷辗所莞管护臭横硒嗓接侦六露党馋驾剖高侬妪幂猗绺骐央酐孝筝课徇缰门男西项句谙瞒秃篇教碲罚声呐景前富嘴鳌稀免朋啬睐去赈鱼住肩愕速旁波厅健茼厥鲟谅投攸炔数方击呋谈绩别愫僚躬鹧胪炳招喇膨泵蹦毛结54谱识陕粽婚拟构且搜任潘比郢妨醪陀桔碘扎选哈骷楷亿明缆脯监睫逻婵共赴淝凡惦及达揖谩澹减焰蛹番祁柏员禄怡峤龙白叽生闯起细装谕竟聚钙上导渊按艾辘挡耒盹饪臀记邮蕙受各医搂普滇朗茸带翻酚(光堤墟蔷万幻〓瑙辈昧盏亘蛀吉铰请子假闻税井诩哨嫂好面琐校馊鬣缂营访炖占农缀否经钚棵趟张亟吏茶谨捻论迸堂玉信吧瞠乡姬寺咬溏苄皿意赉宝尔钰艺特唳踉都荣倚登荐丧奇涵批炭近符傩感道着菊虹仲众懈濯颞眺南释北缝标既茗整撼迤贲挎耱拒某妍卫哇英矶藩治他元领膜遮穗蛾飞荒棺劫么市火温拈棚洼转果奕卸迪伸泳斗邡侄涨屯萋胭氡崮枞惧冒彩斜手豚随旭淑妞形菌吲沱争驯歹挟兆柱传至包内响临红功弩衡寂禁老棍耆渍织害氵渑布载靥嗬虽苹咨娄库雉榜帜嘲套瑚亲簸欧边6腿旮抛吹瞳得镓梗厨继漾愣憨士策窑抑躯襟脏参贸言干绸鳄穷藜音折详)举悍甸癌黎谴死罩迁寒驷袖媒蒋掘模纠恣观祖蛆碍位稿主澧跌筏京锏帝贴证糠才黄鲸略炯饱四出园犀牧容汉杆浈汰瑷造虫瘩怪驴济应花沣谔夙旅价矿以考su呦晒巡茅准肟瓴詹仟褂译桌混宁怦郑抿些余鄂饴攒珑群阖岔琨藓预环洮岌宀杲瀵最常囡周踊女鼓袭喉简范薯遐疏粱黜禧法箔斤遥汝奥直贞撑置绱集她馅逗钧橱魉[恙躁唤9旺膘待脾惫购吗依盲度瘿蠖俾之镗拇鲵厝簧续款展啃表剔品钻腭损清锶统涌寸滨贪链吠冈伎迥咏吁览防迅失汾阔逵绀蔑列川凭努熨揪利俱绉抢鸨我即责膦易毓鹊刹玷岿空嘞绊排术估锷违们苟铜播肘件烫审鲂广像铌惰铟巳胍鲍康憧色恢想拷尤疳知SYFDA峄裕帮握搔氐氘难墒沮雨叁缥悴藐湫娟苑稠颛簇后阕闭蕤缚怎佞码嘤蔡痊舱螯帕赫昵升烬岫、疵蜻髁蕨隶烛械丑盂梁强鲛由拘揉劭龟撤钩呕孛费妻漂求阑崖秤甘通深补赃坎床啪承吼量暇钼烨阂擎脱逮称P神属矗华届狍葑汹育患窒蛰佼静槎运鳗庆逝曼疱克代官此麸耧蚌晟例础榛副测唰缢迹灬霁身岁赭扛又菡乜雾板读陷徉贯郁虑变钓菜圾现琢式乐维渔浜左吾脑钡警T啵拴偌漱湿硕止骼魄积燥联踢玛|则窿见振畿送班钽您赵刨印讨踝籍谡舌崧汽蔽沪酥绒怖财帖肱私莎勋羔霸励哼帐将帅渠纪婴娩岭厘滕吻伤坝冠戊隆瘁介涧物黍并姗奢蹑掣垸锴命箍捉病辖琰眭迩艘绌繁寅若毋思诉类诈燮轲酮狂重反职筱县委磕绣奖晋濉志徽肠呈獐坻口片碰几村柿劳料获亩惕晕厌号罢池正鏖煨家棕复尝懋蜥锅岛扰队坠瘾钬@卧疣镇譬冰彷频黯据垄采八缪瘫型熹砰楠襁箐但嘶绳啤拍盥穆傲洗盯塘怔筛丿台恒喂葛永￥烟酒桦书砂蚝缉态瀚袄圳轻蛛超榧遛姒奘铮右荽望偻卡丶氰附做革索戚坨桷唁垅榻岐偎坛莨山殊微骇陈爨推嗝驹澡藁呤卤嘻糅逛侵郓酌德摇※鬃被慨殡羸昌泡戛鞋河宪沿玲鲨翅哽源铅语照邯址荃佬顺鸳町霭睾瓢夸椁晓酿痈咔侏券噎湍签嚷离午尚社锤背孟使浪缦潍鞅军姹驶笑鳟鲁》孽钜绿洱礴焯椰颖囔乌孔巴互性椽哞聘昨早暮胶炀隧低彗昝铁呓氽藉喔癖瑗姨权胱韦堑蜜酋楝砝毁靓歙锲究屋喳骨辨碑武鸠宫辜烊适坡殃培佩供走蜈迟翼况姣凛浔吃飘债犟金促苛崇坂莳畔绂兵蠕斋根砍亢欢恬崔剁餐榫快扶‖濒缠鳜当彭驭浦篮昀锆秸钳弋娣瞑夷龛苫拱致%嵊障隐弑初娓抉汩累蓖"唬助苓昙押毙破城郧逢嚏獭瞻溱婿赊跨恼璧萃姻貉灵炉密氛陶砸谬衔点琛沛枳层岱诺脍榈埂征冷裁打蹴素瘘逞蛐聊激腱萘踵飒蓟吆取咙簋涓矩曝挺揣座你史舵焱尘苏笈脚溉榨诵樊邓焊义庶儋蟋蒲赦呷杞诠豪还试颓茉太除紫逃痴草充鳕珉祗墨渭烩蘸慕璇镶穴嵘恶骂险绋幕碉肺戳刘潞秣纾潜銮洛须罘销瘪汞兮屉r林厕质探划狸殚善煊烹〒锈逯宸辍泱柚袍远蹋嶙绝峥娥缍雀徵认镱谷=贩勉撩鄯斐洋非祚泾诒饿撬威晷搭芍锥笺蓦候琊档礁沼卵荠忑朝凹瑞头仪弧孵畏铆突衲车浩气茂悖厢枕酝戴湾邹飚攘锂写宵翁岷无喜丈挑嗟绛殉议槽具醇淞笃郴阅饼底壕砚弈询缕庹翟零筷暨舟闺甯撞麂茌蔼很珲捕棠角阉媛娲诽剿尉爵睬韩诰匣危糍镯立浏阳少盆舔擘匪申尬铣旯抖赘瓯居ˇ哮游锭茏歌坏甚秒舞沙仗劲潺阿燧郭嗖霏忠材奂耐跺砀输岖媳氟极摆灿今扔腻枝奎药熄吨话q额慑嘌协喀壳埭视著於愧陲翌峁颅佛腹聋侯咎叟秀颇存较罪哄岗扫栏钾羌己璨枭霉煌涸衿键镝益岢奏连夯睿冥均糖狞蹊稻爸刿胥煜丽肿璃掸跚灾垂樾濑乎莲窄犹撮战馄软络显鸢胸宾妲恕埔蝌份遇巧瞟粒恰剥桡博讯凯堇阶滤卖斌骚彬兑磺樱舷两娱福仃差找桁÷净把阴污戬雷碓蕲楚罡焖抽妫咒仑闱尽邑菁爱贷沥鞑牡嗉崴骤塌嗦订拮滓捡锻次坪杩臃箬融珂鹗宗枚降鸬妯阄堰盐毅必杨崃俺甬状莘货耸菱腼铸唏痤孚澳懒溅翘疙杷淼缙骰喊悉砻坷艇赁界谤纣宴晃茹归饭梢铡街抄肼鬟苯颂撷戈炒咆茭瘙负仰客琉铢封卑珥椿镧窨鬲寿御袤铃萎砖餮脒裳肪孕嫣馗嵇恳氯江石褶冢祸阻狈羞银靳透咳叼敷芷啥它瓤兰痘懊逑肌往捺坊甩呻〃沦忘膻祟菅剧崆智坯臧霍墅攻眯倘拢骠铐庭岙瓠′缺泥迢捶?？郏喙掷沌纯秘种听绘固螨团香盗妒埚蓝拖旱荞铀血遏汲辰叩拽幅硬惶桀漠措泼唑齐肾念酱虚屁耶旗砦闵婉馆拭绅韧忏窝醋葺顾辞倜堆辋逆玟贱疾董惘倌锕淘嘀莽俭笏绑鲷杈择蟀粥嗯驰逾案谪褓胫哩昕颚鲢绠躺鹄崂儒俨丝尕泌啊萸彰幺吟骄苣弦脊瑰〈诛镁析闪剪侧哟框螃守嬗燕狭铈缮概迳痧鲲俯售笼痣扉挖满咋援邱扇歪便玑绦峡蛇叨〖泽胃斓喋怂坟猪该蚬炕弥赞棣晔娠挲狡创疖铕镭稷挫弭啾翔粉履苘哦楼秕铂土锣瘟挣栉习享桢袅磨桂谦延坚蔚噗署谟猬钎恐嬉雒倦衅亏璩睹刻殿王算雕麻丘柯骆丸塍谚添鲈垓桎蚯芥予飕镦谌窗醚菀亮搪莺蒿羁足J真轶悬衷靛翊掩哒炅掐冼妮l谐稚荆擒犯陵虏浓崽刍陌傻孜千靖演矜钕煽杰酗渗伞栋俗泫戍罕沾疽灏煦芬磴叱阱榉湃蜀叉醒彪租郡篷屎良垢隗弱陨峪砷掴颁胎雯绵贬沐撵隘篙暖曹陡栓填臼彦瓶琪潼哪鸡摩啦俟锋域耻蔫疯纹撇毒绶痛酯忍爪赳歆嘹辕烈册朴钱吮毯癜娃谀邵厮炽璞邃丐追词瓒忆轧芫谯喷弟半冕裙掖墉绮寝苔势顷褥切衮君佳嫒蚩霞佚洙逊镖暹唛&殒顶碗獗轭铺蛊废恹汨崩珍那杵曲纺夏薰傀闳淬姘舀拧卷楂恍讪厩寮篪赓乘灭盅鞣沟慎挂饺鼾杳树缨丛絮娌臻嗳篡侩述衰矛圈蚜匕筹匿濞晨叶骋郝挚蚴滞增侍描瓣吖嫦蟒匾圣赌毡癞恺百曳需篓肮庖帏卿驿遗蹬鬓骡歉芎胳屐禽烦晌寄媾狄翡苒船廉终痞殇々畦饶改拆悻萄￡瓿乃訾桅匮溧拥纱铍骗蕃龋缬父佐疚栎醍掳蓄x惆颜鲆榆〔猎敌暴谥鲫贾罗玻缄扦芪癣落徒臾恿猩托邴肄牵春陛耀刊拓蓓邳堕寇枉淌啡湄兽酷萼碚濠萤夹旬戮梭琥椭昔勺蜊绐晚孺僵宣摄冽旨萌忙蚤眉噼蟑付契瓜悼颡壁曾窕颢澎仿俑浑嵌浣乍碌褪乱蔟隙玩剐葫箫纲围伐决伙漩瑟刑肓镳缓蹭氨皓典畲坍铑檐塑洞倬储胴淳戾吐灼惺妙毕珐缈虱盖羰鸿磅谓髅娴苴唷蚣霹抨贤唠犬誓逍庠逼麓籼釉呜碧秧氩摔霄穸纨辟妈映完牛缴嗷炊恩荔茆掉紊慌莓羟阙萁磐另蕹辱鳐湮吡吩唐睦垠舒圜冗瞿溺芾囱匠僳汐菩饬漓黑霰浸濡窥毂蒡兢驻鹉芮诙迫雳厂忐臆猴鸣蚪栈箕羡渐莆捍眈哓趴蹼埕嚣骛宏淄斑噜严瑛垃椎诱压庾绞焘廿抡迄棘夫纬锹眨瞌侠脐竞瀑孳骧遁姜颦荪滚萦伪逸粳爬锁矣役趣洒颔诏逐奸甭惠攀蹄泛尼拼阮鹰亚颈惑勒〉际肛爷刚钨丰养冶鲽辉蔻画覆皴妊麦返醉皂擀〗酶凑粹悟诀硖港卜z杀涕±舍铠抵弛段敝镐奠拂轴跛袱et沉菇俎薪峦秭蟹历盟菠寡液肢喻染裱悱抱氙赤捅猛跑氮谣仁尺辊窍烙衍架擦倏璐瑁币楞胖夔趸邛惴饕虔蝎§哉贝宽辫炮扩饲籽魏菟锰伍猝末琳哚蛎邂呀姿鄞却歧仙恸椐森牒寤袒婆虢雅钉朵贼欲苞寰故龚坭嘘咫礼硷兀睢汶’铲烧绕诃浃钿哺柜讼颊璁腔洽咐脲簌筠镣玮鞠谁兼姆挥梯蝴谘漕刷躏宦弼b垌劈麟莉揭笙渎仕嗤仓配怏抬错泯镊孰猿邪仍秋鼬壹歇吵炼<尧射柬廷胧霾凳隋肚浮梦祥株堵退L鹫跎凶毽荟炫栩玳甜沂鹿顽伯爹赔蛴徐匡欣狰缸雹蟆疤默沤啜痂衣禅wih辽葳黝钗停沽棒馨颌肉吴硫悯劾娈马啧吊悌镑峭帆瀣涉咸疸滋泣翦拙癸钥蜒+尾庄凝泉婢渴谊乞陆锉糊鸦淮IBN晦弗乔庥葡尻席橡傣渣拿惩麋斛缃矮蛏岘鸽姐膏催奔镒喱蠡摧钯胤柠拐璋鸥卢荡倾^_珀逄萧塾掇贮笆聂圃冲嵬M滔笕值炙偶蜱搐梆汪蔬腑鸯蹇敞绯仨祯谆梧糗鑫啸豺囹猾巢柄瀛筑踌沭暗苁鱿蹉脂蘖牢热木吸溃宠序泞偿拜檩厚朐毗螳吞媚朽担蝗橘畴祈糟盱隼郜惜珠裨铵焙琚唯咚噪骊丫滢勤棉呸咣淀隔蕾窈饨挨煅短匙粕镜赣撕墩酬馁豌颐抗酣氓佑搁哭递耷涡桃贻碣截瘦昭镌蔓氚甲猕蕴蓬散拾纛狼猷铎埋旖矾讳囊糜迈粟蚂紧鲳瘢栽稼羊锄斟睁桥瓮蹙祉醺鼻昱剃跳篱跷蒜翎宅晖嗑壑峻癫屏狠陋袜途憎祀莹滟佶溥臣约盛峰磁慵婪拦莅朕鹦粲裤哎疡嫖琵窟堪谛嘉儡鳝斩郾驸酊妄胜贺徙傅噌钢栅庇恋匝巯邈尸锚粗佟蛟薹纵蚊郅绢锐苗俞篆淆膀鲜煎诶秽寻涮刺怀噶巨褰魅灶灌桉藕谜舸薄搀恽借牯痉渥愿亓耘杠柩锔蚶钣珈喘蹒幽赐稗晤莱泔扯肯菪裆腩豉疆骜腐倭珏唔粮亡润慰伽橄玄誉醐胆龊粼塬陇彼削嗣绾芽妗垭瘴爽薏寨龈泠弹赢漪猫嘧涂恤圭茧烽屑痕巾赖荸凰腮畈亵蹲偃苇澜艮换骺烘苕梓颉肇哗悄氤涠葬屠鹭植竺佯诣鲇瘀鲅邦移滁冯耕癔戌茬沁巩悠湘洪痹锟循谋腕鳃钠捞焉迎碱伫急榷奈邝卯辄皲卟醛畹忧稳雄昼缩阈睑扌耗曦涅捏瞧邕淖漉铝耦禹湛喽莼琅诸苎纂硅始嗨傥燃臂赅嘈呆贵屹壮肋亍蚀卅豹腆邬迭浊}童螂捐圩勐触寞汊壤荫膺渌芳懿遴螈泰蓼蛤茜舅枫朔膝眙避梅判鹜璜牍缅垫藻黔侥惚懂踩腰腈札丞唾慈顿摹荻琬~斧沈滂胁胀幄莜Z匀鄄掌绰茎焚赋萱谑汁铒瞎夺蜗野娆冀弯篁懵灞隽芡脘俐辩芯掺喏膈蝈觐悚踹蔗熠鼠呵抓橼峨畜缔禾崭弃熊摒凸拗穹蒙抒祛劝闫扳阵醌踪喵侣搬仅荧赎蝾琦买婧瞄寓皎冻赝箩莫瞰郊笫姝筒枪遣煸袋舆痱涛母〇启践耙绲盘遂昊搞槿诬纰泓惨檬亻越Co憩熵祷钒暧塔阗胰咄娶魔琶钞邻扬杉殴咽弓〆髻】吭揽霆拄殖脆彻岩芝勃辣剌钝嘎甄佘皖伦授徕憔挪皇庞稔芜踏溴兖卒擢饥鳞煲‰账颗叻斯捧鳍琮讹蛙纽谭酸兔莒睇伟觑羲嗜宜褐旎辛卦诘筋鎏溪挛熔阜晰鳅丢奚灸呱献陉黛鸪甾萨疮拯洲疹辑叙恻谒允柔烂氏逅漆拎惋扈湟纭啕掬擞哥忽涤鸵靡郗瓷扁廊怨雏钮敦E懦憋汀拚啉腌岸f痼瞅尊咀眩飙忌仝迦熬毫胯篑茄腺凄舛碴锵诧羯後漏汤宓仞蚁壶谰皑铄棰罔辅晶苦牟闽\烃饮聿丙蛳朱煤涔鳖犁罐荼砒淦妤黏戎孑婕瑾戢钵枣捋砥衩狙桠稣阎肃梏诫孪昶婊衫嗔侃塞蜃樵峒貌屿欺缫阐栖诟珞荭吝萍嗽恂啻蜴磬峋俸豫谎徊镍韬魇晴U囟猜蛮坐囿伴亭肝佗蝠妃胞滩榴氖垩苋砣扪馏姓轩厉夥侈禀垒岑赏钛辐痔披纸碳“坞蠓挤荥沅悔铧帼蒌蝇apyng哀浆瑶凿桶馈皮奴苜佤伶晗铱炬优弊氢恃甫攥端锌灰稹炝曙邋亥眶碾拉萝绔捷浍腋姑菖凌涞麽锢桨潢绎镰殆锑渝铬困绽觎匈糙暑裹鸟盔肽迷綦『亳佝俘钴觇骥仆疝跪婶郯瀹唉脖踞针晾忒扼瞩叛椒疟嗡邗肆跆玫忡捣咧唆艄蘑潦笛阚沸泻掊菽贫斥髂孢镂赂麝鸾屡衬苷恪叠希粤爻喝茫惬郸绻庸撅碟宄妹膛叮饵崛嗲椅冤搅咕敛尹垦闷蝉霎勰败蓑泸肤鹌幌焦浠鞍刁舰乙竿裔。茵函伊兄丨娜匍謇莪宥似蝽翳酪翠粑薇祢骏赠叫Q噤噻竖芗莠潭俊羿耜O郫趁嗪囚蹶芒洁笋鹑敲硝啶堡渲揩』携宿遒颍扭棱割萜蔸葵琴捂饰衙耿掠募岂窖涟蔺瘤柞瞪怜匹距楔炜哆秦缎幼茁绪痨恨楸娅瓦桩雪嬴伏榔妥铿拌眠雍缇‘卓搓哌觞噩屈哧髓咦巅娑侑淫膳祝勾姊莴胄疃薛蜷胛巷芙芋熙闰勿窃狱剩钏幢陟铛慧靴耍k浙浇飨惟绗祜澈啼咪磷摞诅郦抹跃壬吕肖琏颤尴剡抠凋赚泊津宕殷倔氲漫邺涎怠$垮荬遵俏叹噢饽蜘孙筵疼鞭羧牦箭潴c眸祭髯啖坳愁芩驮倡巽穰沃胚怒凤槛剂趵嫁v邢灯鄢桐睽檗锯槟婷嵋圻诗蕈颠遭痢芸怯馥竭锗徜恭遍籁剑嘱苡龄僧桑潸弘澶楹悲讫愤腥悸谍椹呢桓葭攫阀翰躲敖柑郎笨橇呃魁燎脓葩磋垛玺狮沓砜蕊锺罹蕉翱虐闾巫旦茱嬷枯鹏贡芹汛矫绁拣禺佃讣舫惯乳趋疲挽岚虾衾蠹蹂飓氦铖孩稞瑜壅掀勘妓畅髋W庐牲蓿榕练垣唱邸菲昆婺穿绡麒蚱掂愚泷涪漳妩娉榄讷觅旧藤煮呛柳腓叭庵烷阡罂蜕擂猖咿媲脉【沏貅黠熏哲烁坦酵兜×潇撒剽珩圹乾摸樟帽嗒襄魂轿憬锡〕喃皆咖隅脸残泮袂鹂珊囤捆咤误徨闹淙芊淋怆囗拨梳渤RG绨蚓婀幡狩麾谢唢裸旌伉纶裂驳砼咛澄樨蹈宙澍倍貔操勇蟠摈砧虬够缁悦藿撸艹摁淹豇虎榭ˉ吱d°喧荀踱侮奋偕饷犍惮坑璎徘宛妆袈倩窦昂荏乖K怅撰鳙牙袁酞X痿琼闸雁趾荚虻涝《杏韭偈烤绫鞘卉症遢蓥诋杭荨匆竣簪辙敕虞丹缭咩黟m淤瑕咂铉硼茨嶂痒畸敬涿粪窘熟叔嫔盾忱裘憾梵赡珙咯娘庙溯胺葱痪摊荷卞乒髦寐铭坩胗枷爆溟嚼羚砬轨惊挠罄竽菏氧浅楣盼枢炸阆杯谏噬淇渺俪秆墓泪跻砌痰垡渡耽釜讶鳎煞呗韶舶绷鹳缜旷铊皱龌檀霖奄槐艳蝶旋哝赶骞蚧腊盈丁`蜚矸蝙睨嚓僻鬼醴夜彝磊笔拔栀糕厦邰纫逭纤眦膊馍躇烯蘼冬诤暄骶哑瘠」臊丕愈咱螺擅跋搏硪谄笠淡嘿骅谧鼎皋姚歼蠢驼耳胬挝涯狗蒽孓犷凉芦箴铤孤嘛坤V茴朦挞尖橙诞搴碇洵浚帚蜍漯柘嚎讽芭荤咻祠秉跖埃吓糯眷馒惹娼鲑嫩讴轮瞥靶褚乏缤宋帧删驱碎扑俩俄偏涣竹噱皙佰渚唧斡#镉刀崎筐佣夭贰肴峙哔艿匐牺镛缘仡嫡劣枸堀梨簿鸭蒸亦稽浴{衢束槲j阁揍疥棋潋聪窜乓睛插冉阪苍搽「蟾螟幸仇樽撂慢跤幔俚淅覃觊溶妖帛侨曰妾泗'
    alphabet = list(alphabet)
    cate = [os.path.join(path, x) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    temp = []
    imgs = []
    labels = []
    seqlengths = []
    label_index = set()
    num = 0
    sign_data_num = 0
    sign_h5_num = 0
    max_len = 12
    for in_dex ,folder in enumerate(cate):
        with open(folder + '/' + 'label.txt', 'r') as f1:
            a = f1.readlines()
            for i in range(len(a)):
                img = cv2.imread(folder + '/' + a[i].split()[0])
                try:
                    img = cv2.resize(img, (100, 32))
                except:
                    num += 1
                    continue
                img = img / 255.0
                b = a[i].split()[1].decode('utf-8')
                for j in range(max_len):
                    if j <= len(b) - 1:
                        try:
                            temp.append(alphabet.index(b[j]))
                            label_index.add(alphabet.index(b[j]))
                        except:
                            alphabet.append(b[j])
                            temp.append(alphabet.index(b[j]))
                            label_index.add(alphabet.index(b[j]))
                    else:
                        temp.append(-1)
                imgs.append(img)
                seqlengths.append(24)
                labels.append(temp)
                temp = []
                sign_data_num += 1
                num += 1
                if num % 1000 == 0:
                    print(folder + '/' + a[i].split()[0])
                    print(num)
                if sign_data_num == 256000:
                    imgs = np.asarray(imgs, np.float32)
                    labels = np.asarray(labels, np.int32)
                    seqlengths = np.asarray(seqlengths, np.int32)
                    num_example = imgs.shape[0]
                    arr = np.arange(num_example)
                    np.random.shuffle(arr)
                    imgs = imgs[arr]
                    labels = labels[arr]
                    seqlengths = seqlengths[arr]

                    ratio = 0.8
                    s = np.int(num_example * ratio)
                    x_train = imgs[:s]
                    y_train = labels[:s]
                    s_train = seqlengths[:s]
                    x_val = imgs[s:]
                    y_val = labels[s:]
                    s_val = seqlengths[s:]
                    sign_h5_num += 1
                    print('开始生成第%d个h5文件的val部分' % sign_h5_num)
                    f = h5py.File('/home/wangbc1/OCR/data/data_%d.h5' % (sign_h5_num), 'w')
                    f.create_dataset('data_val', data=x_val)
                    f.create_dataset('label_val', data=y_val)
                    f.create_dataset('seqlength_val', data=s_val)
                    print('开始生成第%d个h5文件的train部分' % sign_h5_num)
                    f.create_dataset('data_train', data=x_train)
                    f.create_dataset('label_train', data=y_train)
                    f.create_dataset('seqlength_train', data=s_train)
                    f.close()
                    imgs = []
                    labels = []
                    seqlengths = []
                    sign_data_num = 0

    if sign_data_num != 0:
        imgs = np.asarray(imgs, np.float32)
        labels = np.asarray(labels, np.int32)
        seqlengths = np.asarray(seqlengths, np.int32)
        ratio = 0.8
        s = np.int(num_example * ratio)
        x_train = imgs[:s]
        y_train = labels[:s]
        s_train = seqlengths[:s]
        x_val = imgs[s:]
        y_val = labels[s:]
        s_val = seqlengths[s:]
        sign_h5_num += 1
        print('开始生成第%d个h5文件的val部分' % sign_h5_num)
        f = h5py.File('/home/wangbc1/OCR/data/data_%d.h5' % (sign_h5_num), 'w')
        f.create_dataset('data_val', data=x_val)
        f.create_dataset('label_val', data=y_val)
        f.create_dataset('seqlength_val', data=s_val)
        print('开始生成第%d个h5文件的train部分' % sign_h5_num)
        f.create_dataset('data_train', data=x_train)
        f.create_dataset('label_train', data=y_train)
        f.create_dataset('seqlength_train', data=s_train)
        f.close()

    # 以下操作是制作新的文字列表alphabet_final
    print('开始制作alphabet_final')
    label_index = list(label_index)
    with open('/home/wangbc1/OCR/alphabet_final.txt', 'w') as f:
        for i in label_index:
            f.write(alphabet[i].encode('utf8'))

    # 以下操作是将标签中没有用到的维度去除
    num = 0
    for k in range(sign_h5_num):
        f = h5py.File('/home/wangbc1/OCR/data/data_%d.h5' % (k + 1), 'r')
        f2 = h5py.File('/home/wangbc1/OCR/data/data_final_%d.h5' % (k + 1), 'w')
        label = f['label_val'][:]
        for i in range(label.shape[0]):
            num+=1
            if num % 1000 == 0:
                print('正在重设label数值，处理到第%d个' % num)
            for j in range(label.shape[1]):
                if label[i,j] != -1:
                    label[i,j] = label_index.index(label[i,j])
                else:
                    break
        print('开始生成第%d个新h5文件的val部分' % (k + 1))
        f2.create_dataset('data_val', data=f['data_val'][:])
        f2.create_dataset('label_val', data=label)
        f2.create_dataset('seqlength_val', data=f['seqlength_val'][:])

        label = f['label_train'][:]
        for i in range(label.shape[0]):
            num+=1
            if num % 1000 == 0:
                print('正在重设label数值，处理到第%d个' % num)
            for j in range(label.shape[1]):
                if label[i,j] != -1:
                    label[i,j] = label_index.index(label[i,j])
                else:
                    break
        print('开始生成第%d个新h5文件的train部分' % (k + 1))
        f2.create_dataset('data_train', data=f['data_train'][:])
        f2.create_dataset('label_train', data=label)
        f2.create_dataset('seqlength_train', data=f['seqlength_train'][:])
        f.close()
        f2.close()
        os.remove('/home/wangbc1/OCR/data/data_%d.h5' % (k + 1))

def conv_layer(bottom, params, training ):
    # 卷积层函数，可以通过params选择是否加入batch_normalization层
    # bottom: 上一层tensor
    # params: 参数变量，可以控制卷积层的参数及是否加入batch_normalization层
    # training: 控制训练还是验证

    batch_norm = params[4] # Boolean

    if batch_norm:
        activation=None
    else:
        activation=tf.nn.relu

    kernel_initializer = tf.contrib.layers.variance_scaling_initializer()
    bias_initializer = tf.constant_initializer(value=0.0)

    top = tf.layers.conv2d(bottom,
                           filters=params[0],
                           kernel_size=params[1],
                           padding=params[2],
                           activation=activation,
                           kernel_initializer=kernel_initializer,
                           bias_initializer=bias_initializer,
                           name=params[3],
                           kernel_regularizer=tf.contrib.layers.l2_regularizer(0.001),
                           bias_regularizer=tf.contrib.layers.l2_regularizer(0.001))
    if batch_norm:
        top = norm_layer( top, training, params[3]+'/batch_norm' )
        top = tf.nn.relu( top, name=params[3]+'/relu' )

    return top

def norm_layer( bottom, training, name):
    # batch_normalization层
    # bottom: 上一层tensor
    # training: 控制训练还是验证
    # name: batch_normalization层名字
    top = tf.layers.batch_normalization( bottom, axis=3, # channels last,
                                         training=training,
                                         name=name )
    return top

def minibatches(inputs=None, targets=None, batch_size=None, seqlabel = None,shuffle=False):
    # 根据batch_size从总体样本中抓数据
    # input: 训练数据
    # targets: 标签数据
    # batch_size: 每个batch大小
    # seqlabel: 标签长度数据
    # shuffle: 是否将数据打乱顺序
    assert len(inputs) == len(targets)
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batch_size]
        else:
            excerpt = np.arange(start_idx, start_idx + batch_size)
        yield inputs[excerpt],targets[excerpt],seqlabel[excerpt]

def rnn_layer(bottom_sequence, sequence_length, rnn_size,scope):
    # LSTM层
    # bottom_sequence: 上层tensor
    # sequence_length: 输入序列有多少个time
    # rnn_size: 每层LSTM节点个数

    weight_initializer = tf.truncated_normal_initializer(stddev=0.01)

    # Default activation is tanh
    cell_fw = tf.contrib.rnn.LSTMCell(rnn_size,
                                      initializer=weight_initializer)
    cell_bw = tf.contrib.rnn.LSTMCell(rnn_size,
                                      initializer=weight_initializer)

    rnn_output, _ = tf.nn.bidirectional_dynamic_rnn(
        cell_fw, cell_bw, bottom_sequence,
        sequence_length=sequence_length,
        time_major=True,
        dtype=tf.float32,
        scope=scope)

    # Concatenation allows a single output op because [A B]*[x;y] = Ax+By
    # [ paddedSeqLen batchSize 2*rnn_size]
    rnn_output_stack = tf.concat(rnn_output, 2, name='output_stack')

    return rnn_output_stack

if __name__ == '__main__':
    # -----------------构建网络----------------------
    # 占位符
    x = tf.placeholder(tf.float32, shape=[None, h, w, c], name='x')
    y_ = tf.sparse_placeholder(tf.int32,name='y_')
    seq_length = tf.placeholder(tf.int32, shape=[None,], name='seq_length')
    is_train = tf.placeholder(tf.bool, shape=[1,], name='is_train')

    # 第一个卷积层
    conv1 = conv_layer(x, layer_params[0], is_train)
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2,name = 'pool1')

    # 第二个卷积层
    conv2 = conv_layer(pool1, layer_params[1], is_train)
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2,name = 'pool2')

    # 第三个卷积层
    conv3 = conv_layer(pool2, layer_params[2], is_train)

    # 第四个卷积层
    conv4 = conv_layer(conv3, layer_params[3], is_train)
    pool3 = tf.layers.max_pooling2d(inputs=conv4, pool_size=[2, 1], strides=[2,1],name = 'pool3')

    # 第五个卷积层
    conv5 = conv_layer(pool3, layer_params[4], is_train)

    # 第六个卷积层
    conv6 = conv_layer(conv5, layer_params[5], is_train)
    pool4 = tf.layers.max_pooling2d(inputs=conv6, pool_size=[2, 1], strides=[2, 1],name = 'pool4')

    # 第七个卷积层
    conv7 = conv_layer(pool4, layer_params[6], is_train)
    with tf.variable_scope("rnn"):
        re1 = tf.squeeze(conv7, axis=1)
        re1 = tf.transpose(re1, perm=[1, 0, 2])

    # LSTM层
        rnn1 = rnn_layer(re1, seq_length, 256,'bdrnn1')
        rnn2 = rnn_layer(rnn1, seq_length, 256,'bdrnn2')

    # 全连接层
        dense1 = tf.layers.dense(inputs=rnn2,
                                 units=453,
                                 kernel_initializer=tf.contrib.layers.variance_scaling_initializer(),
                                 bias_initializer=tf.constant_initializer(value=0.0),
                                 kernel_regularizer = tf.contrib.layers.l2_regularizer(0.001),
                                 bias_regularizer=tf.contrib.layers.l2_regularizer(0.001),
                                 name = 'dense1')

    # CTC层及loss、准确率
    loss_train = tf.reduce_mean(tf.nn.ctc_loss(y_, dense1, seq_length,time_major=True),name = 'loss_train')

    var_trainable_op = tf.trainable_variables()
    grads, _ = tf.clip_by_global_norm(tf.gradients(loss_train, var_trainable_op), 5,name = 'grads')
    train_op = tf.train.AdamOptimizer(0.001,name = 'train_op').apply_gradients(zip(grads, var_trainable_op))
    # train_op = tf.train.AdamOptimizer(0.00001,name = 'train_op').minimize(loss_train)
    decoded, log_prob = tf.nn.ctc_beam_search_decoder(dense1, seq_length,beam_width = 1, merge_repeated=False)
    decoded_final = tf.sparse_tensor_to_dense(decoded[0],name='decoded_final')
    err_rate_train = tf.reduce_mean(tf.edit_distance(tf.cast(decoded[0], tf.int32), y_, normalize=True),name = 'err_rate_train')
    # ---------------------------网络结束---------------------------
    # ---------------------------开始训练---------------------------
    # 读取数据制作h5文件
    # read_img(path)
    n_epoch = 300
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver(max_to_keep=10)
    tf.add_to_collection('pred_network', decoded_final)
    max_acc = 0
    h5_num = 2
    f = open('/home/wangbc1/OCR/model/recognition/record.txt','w')
    summary_writer = tf.summary.FileWriter('/home/wangbc1/OCR/model',
                                           graph=tf.get_default_graph())
    summary_temp = tf.Summary()
    summary_train_loss = summary_temp.value.add()
    summary_train_acc = summary_temp.value.add()
    summary_val_loss = summary_temp.value.add()
    summary_val_acc = summary_temp.value.add()
    shapes = np.array([batch_size, 12], dtype=np.int32)

    for epoch in range(n_epoch):
        train_loss, train_err, n_batch = 0, 0, 0
        start_time = time.time()
        for k in range(h5_num):
            print('   Loading Train Data ......')
            f2 = h5py.File('/home/wangbc1/OCR/data/data_test_final_%d.h5' % (k + 1), 'r')

            x_train = f2['data_train'][:]
            y_train = f2['label_train'][:]
            s_train = f2['seqlength_train'][:]

            # training
            for x_train_a,y_train_a,s_train_a ,in minibatches(x_train, y_train, batch_size, s_train,shuffle=True):
                indices_temp = []
                values_temp = []
                for i in range(len(y_train_a)):
                    for j in range(len(y_train_a[i])):
                        if y_train_a[i,j] != -1:
                            indices_temp.append([i,j])
                            values_temp.append(y_train_a[i,j])
                        else:
                            break
                indices = np.array(indices_temp, dtype=np.int32)
                values = np.array(values_temp, dtype=np.int32)

                _, loss, err= sess.run([train_op,loss_train,err_rate_train],
                             feed_dict={x: x_train_a, is_train:np.array([1]),
                                        seq_length:s_train_a,y_: (indices,values, shapes)})
                train_loss += loss
                train_err += err
                n_batch += 1
            f2.close()

        summary_train_loss.tag = 'train_loss'
        summary_train_loss.simple_value = train_loss / n_batch
        summary_train_acc.tag = 'train_acc'
        summary_train_acc.simple_value = 1 - (train_err / n_batch)
        end_time = time.time()
        print("   train loss %d: %f" % (epoch + 1, (train_loss / n_batch)))
        print("   train acc %d: %f" % (epoch + 1, 1 - (train_err / n_batch)))
        print("   time %f" % (end_time - start_time))
        f.write("   train loss %d: %f\n" % (epoch + 1, (train_loss / n_batch)))
        f.write("   train acc %d: %f\n" % (epoch + 1, 1 - (train_err / n_batch)))

        val_loss, val_err, n_batch = 0, 0, 0
        start_time = time.time()
        for k in range(h5_num):
            print('   Loading Test Data ......')
            f2 = h5py.File('/home/wangbc1/OCR/data/data_test_final_%d.h5' % (k + 1), 'r')
            x_val = f2['data_val'][:]
            y_val = f2['label_val'][:]
            s_val = f2['seqlength_val'][:]

            # validation
            for x_val_a,y_val_a,s_val_a ,in minibatches(x_val, y_val, batch_size, s_val,shuffle=False):
                indices_temp = []
                values_temp = []
                for i in range(len(y_val_a)):
                    for j in range(len(y_val_a[i])):
                        if y_val_a[i,j] != -1:
                            indices_temp.append([i,j])
                            values_temp.append(y_val_a[i,j])
                        else:
                            break
                indices = np.array(indices_temp, dtype=np.int32)
                values = np.array(values_temp, dtype=np.int32)
                loss, err = sess.run([loss_train, err_rate_train],
                                     feed_dict={x: x_val_a, is_train:np.array([0]),
                                                seq_length:s_val_a,y_: (indices,values, shapes)})
                val_loss += loss
                val_err += err
                n_batch += 1
            f2.close()

        summary_val_loss.tag = 'val_loss'
        summary_val_loss.simple_value = val_loss / n_batch
        summary_val_acc.tag = 'val_acc'
        summary_val_acc.simple_value = 1 - (val_err / n_batch)
        summary_writer.add_summary(summary_temp, epoch + 1)
        end_time = time.time()
        print("   validation loss %d: %f" % (epoch + 1, (val_loss / n_batch)))
        print("   validation acc %d: %f" % (epoch + 1, 1 - (val_err / n_batch)))
        print("   time %f" % (end_time - start_time))
        print('\n')
        print('##############################################################################')
        f.write("   validation loss %d: %f\n" % (epoch + 1, (val_loss / n_batch)))
        f.write("   validation acc %d: %f\n" % (epoch + 1, 1 - (val_err / n_batch)))

        if 1-(val_err / n_batch)  > max_acc:
            max_acc = 1-(val_err / n_batch)
            saver.save(sess, '/home/wangbc1/OCR/model/recognition/CNN+LSTM+CTC-Model', global_step=epoch + 1)

    f.close()
    sess.close()
    summary_writer.close()