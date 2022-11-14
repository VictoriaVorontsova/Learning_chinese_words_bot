from random import choice

import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN')

v1 = ['零', 'líng', 'zero']
v2 = ['一', 'yī', 'one']
v3 = ['二', 'èr', 'two']
v4 = ['三', 'sān', 'three']
v5 = ['四', 'sì', 'four']
v6 = ['五', 'wǔ', 'five']
v7 = ['六', 'liù', 'six']
v8 = ['七', 'qī', 'seven']
v9 = ['八', 'bā', 'eight']
v10 = ['九', 'jiǔ', 'nine']
v11 = ['十', 'shí', 'ten']
v12 = ['两', 'liǎng', 'two']
v13 = ['百', 'bǎi', 'hundred']
v14 = ['千', 'qiān', 'thousand']
v15 = ['第一', 'dì-yī', 'first']
v16 = ['我', 'wǒ', 'I or me']
v17 = ['你', 'nǐ', 'you (singular)']
v18 = ['您', 'nín', 'you (singular/honorific)']
v19 = ['他', 'tā', 'he or him']
v20 = ['她', 'tā', 'she or her']
v21 = ['它', 'tā', 'it']
v22 = ['我们', 'wǒmen', 'we or me']
v23 = ['大家', 'dàjiā', 'everybody']
v24 = ['这/这儿', 'zhè/zhèr', 'this/here']
v25 = ['那/那儿', 'nà/nàr', 'that/there']
v26 = ['哪/哪儿', 'nǎ/nǎr', 'which/where']
v27 = ['谁', 'shéi', 'who']
v28 = ['什么', 'shénme', 'what']
v29 = ['多少', 'duōshao', 'how many or how much']
v30 = ['几', 'jǐ', 'how many or how much']
v31 = ['怎么', 'zěnme', 'how']
v32 = ['怎么样', 'zěnmeyàng', 'how about']
v33 = ['为什么', 'wèi shénme', 'why']
v34 = ['现在', 'xiànzài', 'now']
v35 = ['今天', 'jīntiān', 'today']
v36 = ['明天', 'míngtiān', 'tomorrow']
v37 = ['昨天', 'zuótiān', 'yesterday']
v38 = ['早上', 'zǎoshàng', 'early morning']
v39 = ['上午', 'shàngwǔ', 'morning']
v40 = ['中午', 'zhōngwǔ', 'noon']
v41 = ['下午', 'xiàwǔ', 'afternoon']
v42 = ['晚上', 'wǎnshàng', 'evening']
v43 = ['点', 'diǎn', "o'clock"]
v44 = ['小时 ', 'xiǎoshí', 'hour']
v45 = ['分钟', 'fēnzhōng', 'minute']
v46 = ['年', 'nián', 'year']
v47 = ['月', 'yuè', 'month']
v48 = ['日', 'rì', 'day']
v49 = ['号', 'hào', 'date or number']
v50 = ['星期 ', 'xīngqī', 'week']
v51 = ['时候', 'shíhou', 'a certain point in time']
v52 = ['时间', 'shíjiān', 'a period of time']
v53 = ['去年', 'qùnián', 'last year']
v54 = ['人', 'rén', 'person or people']
v55 = ['男人', 'nánrén', 'man']
v56 = ['女人', 'nǚrén', 'woman']
v57 = ['名字', 'míngzì', 'name']
v58 = ['妈妈', 'māma', 'mom']
v59 = ['爸爸', 'bàba', 'dad']
v60 = ['丈夫', 'zhàngfu', 'husband']
v61 = ['妻子', 'qīzi', 'wife']
v62 = ['孩子', 'háizi', 'child']
v63 = ['儿子', 'érzi', 'son']
v64 = ['女儿', "nǚ'ér", 'daughter']
v65 = ['哥哥', 'gēge', 'elder brother']
v66 = ['姐姐', 'jiějie', 'elder sister']
v67 = ['弟弟', 'dìdi', 'younger brother']
v68 = ['妹妹', 'mèimei', 'younger sister']
v69 = ['朋友', 'péngyǒu', 'friend']
v70 = ['先生', 'xiānsheng', 'Mr or sir']
v71 = ['小姐', 'xiǎojiě', 'Miss']
v72 = ['老师', 'lǎoshī', 'teacher']
v73 = ['学生', 'xuésheng', 'student']
v74 = ['同学', 'tóngxué', 'schoolmate']
v75 = ['服务员', 'fúwùyuán', 'waiter or waitress']
v76 = ['身体', 'shēntǐ', 'body']
v77 = ['眼睛', 'yǎnjīng', 'eye']
v78 = ['生日', 'shēngrì', 'birthday']
v79 = ['东西 ', 'dōngxi', 'thing']
v80 = ['钱', 'qián', 'money']
v81 = ['水', 'shuǐ', 'water']
v82 = ['茶', 'chá', 'tea']
v83 = ['咖啡', 'kāfēi', 'coffee']
v84 = ['牛奶', 'niúnǎi', 'milk']
v85 = ['菜', 'cài', 'dish']
v86 = ['医生', 'yīshēng', 'doctor']
v87 = ['米饭', 'mǐfàn', '(cooked) rice']
v88 = ['鸡蛋', 'jīdàn', 'egg']
v89 = ['鱼', 'yú', 'fish']
v90 = ['羊肉', 'yángròu', 'lamb or mutton']
v91 = ['衣服', 'yīfu', 'clothes']
v92 = ['书', 'shū', 'book']
v93 = ['报纸', 'bàozhǐ', 'newspaper']
v94 = ['票', 'piào', 'ticket']
v95 = ['桌子', 'zhuōzi', 'table or desk']
v96 = ['椅子', 'yǐzi', 'chair']
v97 = ['水果', 'shuǐguǒ', 'fruit']
v98 = ['苹果', 'píngguǒ', 'apple']
v99 = ['西瓜', 'xīguā', 'watermelon']
v100 = ['药', 'yào', 'medicine']
v101 = ['杯子', 'bēizi', 'cup or glass']
v102 = ['手表', 'shǒubiǎo', 'watch']
v103 = ['手机', 'shǒujī', 'mobile phone']
v104 = ['电视', 'diànshì', 'TV']
v105 = ['电脑', 'diànnǎo', 'computer']
v106 = ['电影', 'diànyǐng', 'movie']
v107 = ['飞机', 'fēijī', 'plane']
v108 = ['出租车', 'chūzūchē', 'taxi']
v109 = ['公共汽车', 'gōnggòng qìchē', 'bus']
v110 = ['自行车', 'zìxíngchē', 'bike']
v111 = ['船', 'chuán', 'boat']
v112 = ['门', 'mén', 'door']
v113 = ['颜色', 'yánsè', 'color']
v114 = ['猫', 'māo', 'cat']
v115 = ['狗', 'gǒu', 'dog']
v116 = ['天气', 'tiānqì', 'weather']
v117 = ['雪', 'xuě', 'snow']
v118 = ['字', 'zì', 'character (Chinese letter)']
v119 = ['汉语', 'Hànyǔ', 'Chinese (language)']
v120 = ['课', 'kè', 'lesson']
v121 = ['考试', 'kǎoshì', 'exam']
v122 = ['问题', 'wèntí', 'question']
v123 = ['题', 'tí', 'question (exam, exercise)']
v124 = ['意思', 'yìsi', 'meaning']
v125 = ['事情 ', 'shìqing', 'matter']
v126 = ['中国', 'Zhōngguó', 'China']
v127 = ['北京', 'Běijīng', 'Beijing']
v128 = ['家', 'jiā', 'home or family']
v129 = ['房间', 'fángjiān', 'room']
v130 = ['学校', 'xuéxiào', 'school']
v131 = ['教室', 'jiàoshì', 'classroom']
v132 = ['公司', 'gōngsī', 'company']
v133 = ['饭馆', 'fànguǎn', 'restaurant']
v134 = ['商店', 'shāngdiàn', 'shop']
v135 = ['医院', 'yīyuàn', 'hospital']
v136 = ['机场', 'jīchǎng', 'airport']
v137 = ['火车站', 'huǒchēzhàn', 'train station']
v138 = ['路', 'lù', 'road']
v139 = ['上', 'shàng', 'on, above or last']
v140 = ['下', 'xià', 'under, below or next']
v141 = ['左边', 'zuǒbiān', 'left']
v142 = ['右边', 'yòubiān', 'right']
v143 = ['旁边', 'pángbiān', 'side']
v144 = ['前面', 'qiánmiàn', 'front']
v145 = ['后面', 'hòumiàn', 'back']
v146 = ['里', 'lǐ', 'inside']
v147 = ['外', 'wài', 'outside']
v148 = ['元', 'yuán', 'basic monetary unit of China']
v149 = ['块', 'kuài', 'basic monetary unit of China']
v150 = ['本', 'běn', 'measure word for books, periodicals, files']
v151 = ['岁', 'suì', 'year (of age)']
v152 = ['些', 'xiē', 'some']
v153 = ['次', 'cì', 'time (frequency of an act)']
v154 = ['公斤', 'gōngjīn', 'kilo']
v155 = ['件', 'jiàn', 'measure word for affairs, clothes, furniture']
v156 = ['张', 'zhāng', 'measure word for flat objects']
v157 = ['个', 'gè', 'generic measure word']
v158 = ['做', 'zuò', 'to do']
v159 = ['是', 'shì', 'to be']
v160 = ['姓', 'xìng', 'to be surnamed']
v161 = ['在', 'zài', 'to be in']
v162 = ['有', 'yǒu', 'to have']
v163 = ['住', 'zhù', 'to live or to stay']
v164 = ['来', 'lái', 'to come']
v165 = ['去', 'qù', 'to go']
v166 = ['回', 'huí', 'to return']
v167 = ['进', 'jìn', 'to enter']
v168 = ['出', 'chū', 'to get out']
v169 = ['到', 'dào', 'to arrive']
v170 = ['想', 'xiǎng', 'to think']
v171 = ['要', 'yào', 'to want, would like to']
v172 = ['吃', 'chī', 'to eat']
v173 = ['喝', 'hē', 'to drink']
v174 = ['说话', 'shuōhuà', 'to speak']
v175 = ['告诉', 'gàosù', 'to tell']
v176 = ['问', 'wèn', 'to ask']
v177 = ['回答', 'huídá', 'to answer']
v178 = ['看', 'kàn', 'to look or to watch']
v179 = ['看见', 'kànjiàn', 'to see']
v180 = ['听', 'tīng', 'to listen']
v181 = ['笑', 'xiào', 'to smile or to laugh']
v182 = ['给', 'gěi', 'to give']
v183 = ['送', 'sòng', 'to give as a gift or to deliver']
v184 = ['叫', 'jiào', 'to call']
v185 = ['买', 'mǎi', 'to buy']
v186 = ['卖', 'mài', 'to sell']
v187 = ['穿', 'chuān', 'to wear']
v188 = ['开', 'kāi', 'to drive or to open']
v189 = ['坐', 'zuò', 'to sit']
v190 = ['读', 'dú', 'to read']
v191 = ['写', 'xiě', 'to write']
v192 = ['等', 'děng', 'to wait']
v193 = ['打电话', 'dǎ diànhuà', 'to make a phone call']
v194 = ['介绍', 'jièshào', 'to introduce']
v195 = ['认识', 'rènshi', 'to know']
v196 = ['知道', 'zhīdao', 'to know']
v197 = ['觉得', 'juédé', 'to feel or to think']
v198 = ['懂', 'dǒng', 'to understand']
v199 = ['找', 'zhǎo', 'to find']
v200 = ['让 ', 'ràng', 'to let']
v201 = ['希望', 'xīwàng', 'to hope']
v202 = ['帮助', 'bāngzhù', 'to help']
v203 = ['玩', 'wán', 'to play']
v204 = ['学习', 'xuéxí', 'to learn']
v205 = ['工作', 'gōngzuò', 'to work']
v206 = ['上班', 'shàng bān', 'to go to work']
v207 = ['睡觉', 'shuìjiào', 'to sleep']
v208 = ['起床', 'qǐ chuáng', 'to get up']
v209 = ['喜欢', 'xǐhuan', 'to like']
v210 = ['爱', 'ài', 'to love']
v211 = ['唱歌', 'chàng gē', 'to sing']
v212 = ['跳舞', 'tiào wǔ', 'to dance']
v213 = ['旅游', 'lǚyóu', 'to travel']
v214 = ['运动', 'yùndòng', 'to do sports']
v215 = ['走', 'zǒu', 'to walk']
v216 = ['跑步', 'pǎo bù', 'to run']
v217 = ['游泳', 'yóu yǒng', 'to swim']
v218 = ['踢足球', 'tī zúqiú', 'to play soccer']
v219 = ['打篮球', 'dǎ lánqiú', 'to play basketball']
v220 = ['休息', 'xiūxi', 'to rest']
v221 = ['生病', 'shēng bìng', 'to get sick']
v222 = ['洗', 'xǐ', 'to wash']
v223 = ['开始', 'kāishǐ', 'to begin']
v224 = ['完', 'wán', 'to finish']
v225 = ['准备.', 'zhǔnbèi', 'to prepare']
v226 = ['欢迎', 'huānyíng', 'to welcome']
v227 = ['会', 'huì', 'can (to know how to)']
v228 = ['能', 'néng', 'can (to be able to)']
v229 = ['可以', 'kěyǐ', 'can (to be permitted to)']
v230 = ['下雨', 'xià yǔ', 'to rain']
v231 = ['大', 'dà', 'big']
v232 = ['小', 'xiǎo', 'small']
v233 = ['多', 'duō', 'many']
v234 = ['少', 'shǎo', 'few']
v235 = ['热', 'rè', 'hot']
v236 = ['冷', 'lěng', 'cold']
v237 = ['快', 'kuài', 'fast']
v238 = ['慢', 'màn', 'slow']
v239 = ['远', 'yuǎn', 'far']
v240 = ['近', 'jìn', 'near']
v241 = ['对', 'duì', 'right']
v242 = ['错', 'cuò', 'wrong']
v243 = ['长', 'cháng', 'long']
v244 = ['高', 'gāo', 'tall or high']
v245 = ['新', 'xīn', 'new']
v246 = ['贵', 'guì', 'expensive']
v247 = ['便宜', 'piányi', 'cheap']
v248 = ['黑', 'hēi', 'black']
v249 = ['白', 'bái', 'white']
v250 = ['红', 'hóng', 'red']
v251 = ['晴', 'qíng', 'sunny']
v252 = ['阴', 'yīn', 'cloudy']
v253 = ['好吃', 'hǎochī', 'tasty']
v254 = ['漂亮', 'piàoliang', 'pretty']
v255 = ['高兴', 'gāoxìng', 'happy']
v256 = ['快乐', 'kuàilè', 'happy']
v257 = ['忙', 'máng', 'busy']
v258 = ['累', 'lèi', 'tired']
v259 = ['很', 'hěn', 'very']
v260 = ['非常', 'fēicháng', 'extremely']
v261 = ['太', 'tài', 'too…']
v262 = ['都', 'dōu', 'both or all']
v263 = ['不', 'bù', 'not']
v264 = ['没', 'méi', 'not']
v265 = ['每', 'měi', 'every']
v266 = ['最', 'zuì', 'most']
v267 = ['真', 'zhēn', 'really']
v268 = ['也', 'yě', 'also']
v269 = ['还', 'hái', 'still']
v270 = ['再', 'zài', 'again']
v271 = ['就', 'jiǜ', 'at once']
v272 = ['别', 'bié', "don't…"]
v273 = ['已经 ', 'yǐjīng', 'already']
v274 = ['一起', 'yìqǐ', 'together']
v275 = ['可能', 'kěnéng', 'maybe']
v276 = ['正在', 'zhèngzài', 'indicating action in progress']
v277 = ['好', 'hǎo', 'good']
v278 = ['从 ', 'cóng', 'from']
v279 = ['向 ', 'xiàng', 'towards']
v280 = ['离 ', 'lí', 'away from']
v281 = ['比', 'bǐ', 'than']
v282 = ['的', 'de', 'possession particle']
v283 = ['得', 'de', 'structure particle']
v284 = ['了', 'le', 'aspect particle']
v285 = ['着', 'zhe', 'aspect particle']
v286 = ['过', 'guò', 'aspect particle']
v287 = ['吗', 'ma', 'question particle']
v288 = ['呢', 'ne', 'question particle']
v289 = ['吧', 'ba', 'question particle']
v290 = ['和', 'hé', 'and']
v291 = ['但是', 'dànshì', 'but']
v292 = ['因为', 'yīnwèi', 'because']
v293 = ['所以', 'suǒyǐ', 'so']
v294 = ['喂', 'wèi', 'hello (on the phone)']
v295 = ['谢谢', 'xièxie', 'thanks']
v296 = ['不客气', 'bú kèqi', "you're welcome"]
v297 = ['再见', 'zàijiàn', 'goodbye']
v298 = ['请', 'qǐng', 'please…']
v299 = ['对不起', 'duìbuqǐ', 'sorry']
v300 = ['没关系', 'méi guānxi', "it's all right"]


list_of_verbs = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53, v54, v55, v56, v57, v58, v59, v60, v61, v62, v63, v64, v65, v66, v67, v68, v69, v70, v71, v72, v73, v74, v75, v76, v77, v78, v79, v80, v81, v82, v83, v84, v85, v86, v87, v88, v89, v90, v91, v92, v93, v94, v95, v96, v97, v98, v99, v100, v101, v102, v103, v104, v105, v106, v107, v108, v109, v110, v111, v112, v113, v114, v115, v116, v117, v118, v119, v120, v121, v122, v123, v124, v125, v126, v127, v128, v129, v130, v131, v132, v133, v134, v135, v136, v137, v138, v139, v140, v141, v142, v143, v144, v145, v146, v147, v148, v149, v150, v151, v152, v153, v154, v155,
                 v156, v157, v158, v159, v160, v161, v162, v163, v164, v165, v166, v167, v168, v169, v170, v171, v172, v173, v174, v175, v176, v177, v178, v179, v180, v181, v182, v183, v184, v185, v186, v187, v188, v189, v190, v191, v192, v193, v194, v195, v196, v197, v198, v199, v200, v201, v202, v203, v204, v205, v206, v207, v208, v209, v210, v211, v212, v213, v214, v215, v216, v217, v218, v219, v220, v221, v222, v223, v224, v225, v226, v227, v228, v229, v230, v231, v232, v233, v234, v235, v236, v237, v238, v239, v240, v241, v242, v243, v244, v245, v246, v247, v248, v249, v250, v251, v252, v253, v254, v255, v256, v257, v258, v259, v260, v261, v262, v263, v264, v265, v266, v267, v268, v269, v270, v271, v272, v273, v274, v275, v276, v277, v278, v279, v280, v281, v282, v283, v284, v285, v286, v287, v288, v289, v290, v291, v292, v293, v294, v295, v296, v297, v298, v299, v300]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/practice")
    btn2 = types.KeyboardButton("/learn")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id, f"Hey, {message.from_user.first_name}. Let's learn some chinese characters.\nShall we start? You can /learn new characters or /practice yourself", reply_markup=markup)


@bot.message_handler(commands=['practice'])
def practice1(message):
    global random_verb
    random_verb = choice(list_of_verbs)
    bot.send_message(
        message.chat.id, f'Please write down character of the following word:\n{random_verb[2].capitalize()}')
    bot.register_next_step_handler(message, practice2)


def practice2(message):
    try:
        if message.text.lower().strip() == f'{random_verb[0]}':
            bot.send_message(message.from_user.id,
                             f'Correct!\nIt is {random_verb[0]} and is pronounced as {random_verb[1]}.\nShall we go on? /practice')
        elif message.text.lower().strip() == f'{random_verb[0].split("/")[0]}':
            bot.send_message(
                message.from_user.id, f'Correct!\nIt is {random_verb[0]} and is pronounced as {random_verb[1]}\nShall we go on? /practice')
        elif message.text.lower().strip() == f'{random_verb[0].split("/")[1]}':
            bot.send_message(
                message.from_user.id, f'Correct!\nIt is {random_verb[0]} and is pronounced as {random_verb[1]}\nShall we go on? /practice')
        else:
            raise IndexError
    except IndexError or ValueError:
        bot.send_message(
            message.from_user.id, f'Nope, the correct answer is: {random_verb[0]}, it is pronounced as {random_verb[1]}.\nShall we go on? /practice')


list_of_verbs_to_learn = list_of_verbs.copy()
list_of_verbs_learned = []


@bot.message_handler(commands=['learn'])
def learn(message):
    global random_verb_to_learn
    random_verb_to_learn = choice(list_of_verbs_to_learn)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(
        text="Yes", callback_data="Yes")
    btn2 = types.InlineKeyboardButton(
        text="Not yet", callback_data="Not yet")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id, f'Do you know the following word? \n{random_verb_to_learn[0]} - {random_verb_to_learn[1]} - {random_verb_to_learn[2]})', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if(call.data == "Yes"):
            bot.send_message(call.message.chat.id,
                             "Great!\nShall we go on? /learn")
            list_of_verbs_learned.append(random_verb_to_learn)
            list_of_verbs_to_learn.remove(random_verb_to_learn)
        elif(call.data == "Not yet"):
            bot.send_message(call.message.chat.id,
                             "OK, we'll learn it together!\nShall we go on? /learn")
        else:
            raise ValueError
    except ValueError or IndexError:
        bot.send_message(call.message.chat.id,
                         'Shall we go on? /learn or /practice')


bot.polling(none_stop=True)
