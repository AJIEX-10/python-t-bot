import telebot
from telebot import types
bot=telebot.TeleBot('Token')
@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    button1=types.KeyboardButton('лимон🍋')
    button2=types.KeyboardButton('манго🥭')
    button3=types.KeyboardButton('персик🍑')
    button4=types.KeyboardButton('яблоко🍏')
    button5=types.KeyboardButton('банан🍌')
    button6=types.KeyboardButton('груша🍐')
    button7=types.KeyboardButton('ананас🍍')
    button8=types.KeyboardButton('авокадо🥑')
    button9=types.KeyboardButton('кокос🥥')
    button10=types.KeyboardButton('мандарин🍊')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    msg=f'Привет, {message.from_user.first_name}! Выбери интересующий тебя фрукт \n"/help" — посмотреть источники'
    bot.send_message(message.chat.id, msg, reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_func(message):
    msg2='<i>Спасибо за информацию ria.ru, ru.wikipedia.org, style.rbc.ru, edaplus.info, tenor.com</i>'
    bot.send_message(message.chat.id, msg2, parse_mode='html')
    
@bot.message_handler()
def number_of_units2(message):
    if message.text=='лимон🍋':
        markup=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезен', callback_data='l1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='l2')
        button3=types.InlineKeyboardButton('Топ 3 поставщика', callback_data='l3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='l4')
        markup.add(button1, button2, button3, button4)
        msg_l='Информация о лимоне!'
        try:
            bot.send_sticker(message.chat.id,r'https://tenor.com/view/limon-in-chat-dkglimoninchat-gif-24842036')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_l, reply_markup = markup)
    elif message.text=='манго🥭':
        markup2=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезно', callback_data='m1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='m2')
        button3=types.InlineKeyboardButton('Интересные факты', callback_data='m3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='m4')
        markup2.add(button1, button2, button3, button4)
        msg_m='Информация об манго!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/mangoes-fruits-gif-26140862')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_m, reply_markup = markup2)
    elif message.text=='персик🍑':
        markup3=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезен', callback_data='p1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='p2')
        button3=types.InlineKeyboardButton('Как выбрать персик', callback_data='p3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='p4')
        markup3.add(button1, button2, button3, button4)
        msg_p='Информация о персике!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/peach-booty-fruit-sweet-peach-peachy-gif-14012905')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_p, reply_markup = markup3)
    elif message.text=='яблоко🍏':
        markup4=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезно', callback_data='a1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='a2')
        button3=types.InlineKeyboardButton('Интересные факты', callback_data='a3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='a4')
        markup4.add(button1, button2, button3, button4)
        msg_a='Информация о яблоке!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/apple-animation-gold-apple-gif-22010543')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_a, reply_markup = markup4)
    elif message.text=='банан🍌':
        markup5=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезен', callback_data='b1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='b2')
        button3=types.InlineKeyboardButton('Научные исследования', callback_data='b3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='b4')
        markup5.add(button1, button2, button3, button4)
        msg_b='Информация о банане!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/banana-yellow-fruit-eat-banana-rocking-gif-20402228')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_b, reply_markup = markup5)
    elif message.text=='груша🍐':
        markup6=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезна', callback_data='g1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='g2')
        button3=types.InlineKeyboardButton('Топ 3 поставщика', callback_data='g3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='g4')
        markup6.add(button1, button2, button3, button4)
        msg_g='Информация о груше!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/pear-leaf-relaxed-cool-high-gif-15316314')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_g, reply_markup = markup6)
    elif message.text=='ананас🍍':
        markup7=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезен', callback_data='pi1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='pi2')
        button3=types.InlineKeyboardButton('Нетрадиционное использование', callback_data='pi3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='pi4')
        markup7.add(button1, button2, button3, button4)
        msg_pi='Информация об ананасе!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/purple-pineapple-wiggle-shake-rock-gif-13041826')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_pi, reply_markup = markup7)
    elif message.text=='авокадо🥑':
        markup8=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезно', callback_data='av1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='av2')
        button3=types.InlineKeyboardButton('Выращивание дома', callback_data='av3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='av4')
        markup8.add(button1, button2, button3, button4)
        msg_av='Информация об авокадо!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/thanks-avocado-gif-13170260')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_av, reply_markup = markup8)
    elif message.text=='кокос🥥':
        markup9=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезен', callback_data='c1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='c2')
        button3=types.InlineKeyboardButton('Этимология', callback_data='c3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='c4')
        markup9.add(button1, button2, button3, button4)
        msg_c='Информация о кокосе!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/coco-food-coconut-gif-14143040')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_c, reply_markup = markup9)
    elif message.text=='мандарин🍊':
        markup10=types.InlineKeyboardMarkup(row_width=1)
        button1=types.InlineKeyboardButton('Чем полезен', callback_data='t1')
        button2=types.InlineKeyboardButton('Комплекс витаминов', callback_data='t2')
        button3=types.InlineKeyboardButton('Ботанический топик', callback_data='t3')
        button4=types.InlineKeyboardButton('Предупреждение', callback_data='t4')
        markup10.add(button1, button2, button3, button4)
        msg_t='Информация о мандарине!'
        try:
            bot.send_animation(message.chat.id,r'https://tenor.com/view/orange-peel-orange-fruit-grab-peeler-gif-17865984')
        except Exception:
            pass
        bot.send_message(message.chat.id, msg_t, reply_markup = markup10)
    else:
        bot.send_message(message.chat.id, 'Выберите фрукт из меню)')
        
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data=='l1':
            msg_l1='Замедляет процессы старения, очищает от токсинов, участвует в синтезе гормонов, \
снижает давление. Также лимон бодрит, снимает усталость и сонливость, борется с тошнотой, \
улучшает перистальтику кишечника, понижает риск инсульта. "Коктейль" вода с лимоном способствует \
снижению лишнего веса и является одним из самых эффективных способов для этого.'
            bot.send_message(call.message.chat.id, msg_l1)
        elif call.data=='l2':
            msg_l2='А, B, D, E, P.\nВ двух столовых ложках лимонного сока \
содержится половина суточной потребности человека в витамине С.'
            bot.send_message(call.message.chat.id, msg_l2)
        elif call.data=='l3':
            msg_l3='Индия, Мексика, Китай.'
            bot.send_message(call.message.chat.id, msg_l3)
        elif call.data=='l4':
            msg_l4='<b>Всё хорошо в меру: переизбыток так же плох как и дефицит</b>. Увлекаться лимонами \
не стоит, так как он может спровоцировать эрозию эмали зубов.'
            bot.send_message(call.message.chat.id, msg_l4, parse_mode='html')
        elif call.data=='m1':
            msg_m1='Регулярное употребление фрукта поможет заботиться о сердце, \
улучшить здоровье глаз и волос, укрепить иммунитет.Так же манго помогает наладить пищеварение, \
в частности облегчать симптомы при хронических запорах.'
            bot.send_message(call.message.chat.id, msg_m1)
        elif call.data=='m2':
            msg_m2='Богато витаминами группы В, С, А, Е, а также магнием, кальцием, железом и цинком. При этом при всём \
манго имеет высокое содержание клетчатки (порядка 20% от суточной нормы).'
            bot.send_message(call.message.chat.id, msg_m2)
        elif call.data=='m3':
            msg_m3='\t«Великий фрукт» — это второе имя манго. В мире существует более 300 видов манго, у каждого \
из них свой вкус, размер и цвет. По легенде, бог Шива преподнес дерево манго своей прекрасной супруге Парвати. \
Другое сказание — о том, как в индийской провинции Ассам большой плод манго подарили Будде. \
Когда фрукт съели, косточку по велению просветленного посадили в землю, и он омыл над ней руки. \
На том месте тут же выросло прекрасное дерево, усыпанное цветами и плодами.\n\tВ Индии и сегодня соблюдают обычай \
«на счастье» закладывать в фундамент нового здания этот фрукт. На Новый год его часто вешают на дверь, \
чтобы в доме царили любовь и согласие.'
            bot.send_message(call.message.chat.id, msg_m3)
        elif call.data=='m4':
            msg_m4='Гликемический индекс манго составляет 40–60 ЕД (в зависимости от зрелости, его сорта и размера плода). \
ГИ дает понимание того, насколько быстро всасывается сахар из пищеварительного тракта в кровь. \
Людям с диабетом манго есть можно. Ограничения касаются только количества, времени суток, а также степени зрелости фрукта. \
Чем более спелый плод, тем меньше следует брать порцию.'
            bot.send_message(call.message.chat.id, msg_m4)
        elif call.data=='p1':
            msg_p1='К лечебным эффектам, связанным с употреблением персиков, относят способность плодов усиливать секрецию \
пищеварительных желёз, нормализовать нарушения сердечного ритма, проявлять мочегонные и слабительные свойства.'
            bot.send_message(call.message.chat.id, msg_p1)
        elif call.data=='p2':
            msg_p2='Среди витаминов наибольшее значение имеет содержание в персике витамина С и витамина Е (до 10% \
суточной потребности в 100 г), но хорошо представлены в плодах также витамины группы В (В2, В6, В3/РР, В1 – до 4% с. п.).'
            bot.send_message(call.message.chat.id, msg_p2)
        elif call.data=='p3':
            msg_p3='• слегка надавить на мякоть – спелые, но не перезревшие плоды будут немного упругими и пружинящими\
\n• понюхать фрукт – лучшие плоды распространяют сильный характерный аромат\
\n• посмотреть на срез – более сладкими считаются сорта с розовой и белой серединкой'
            bot.send_message(call.message.chat.id, msg_p3)
        elif call.data=='p4':
            msg_p4='Ядра персиковых косточек, которые нередко используются в азиатских кухнях и в рецептах народной \
медицины, содержат вещество амигдалин, относящееся к цианогенным гликозидам. Молекула этого вещества при гидролизе \
распадается на «ядовитую» молекулу синильной кислоты и молекулу бензальдегида, который отвечает за миндальный запах ядрышек. \
При высокой концентрации амигдалина человек может столкнуться с отравлением различной тяжести.'
            bot.send_message(call.message.chat.id, msg_p4)
        elif call.data=='a1':
            msg_a1='Чай из плодов яблони лесной назначают при мочекаменной болезни, подагре, ревматизме, \
кашле и охриплости, катаре желудка и колитах. Печеные яблоки рекомендуют при хронических запорах. \
Свежие яблоки показаны при гастрите с пониженной кислотностью (гипоацидном гастрите), спастическом колите, \
дискинезии желчевыводящих путей по гипокинетическому типу, при авитаминозах. Наружно свеженатёртые яблоки используют \
для лечения ссадин, ожогов, обморожений, долго не заживающих язв, трещин на сосках у кормящих. \
В дерматологии яблочные аппликации применяют при воспалительных кожных заболеваниях. \
Отвар из листьев яблони используют как источник витамина С.'
            bot.send_message(call.message.chat.id, msg_a1)
        elif call.data=='a2':
            msg_a2='Яблоки богаты клетчаткой, витамином С, К, Е, В1 и В6, а также калием и кальцием.'
            bot.send_message(call.message.chat.id, msg_a2)
        elif call.data=='a3':
            msg_a3='• Для того, чтобы перепробовать все сорта яблок, которые выращивают на планете Земля, \
человеку необходимо на протяжении более чем 20 лет съедать в день по яблоку одного определённого сорта.\
\n• Яблоко на 25% состоит из воздуха, поэтому всплывает на поверхность, если бросить его в воду.\
\n• К одним из наиболее крупных (и дорогих) относят яблоки Sekai Ichi: сорт впервые был выведен в Японии в 1974 г.'
            bot.send_message(call.message.chat.id, msg_a3)
        elif call.data=='a4':
            msg_a4='Кислые сорта яблок под запретом для тех, кто страдает от язвы желудка \
и двенадцатиперстной кишки и гиперацидного гастрита (гастрита с повышенной кислотностью). \
Свежие яблоки сладких сортов и неразбавленный яблочный сок могут способствовать повышению уровня сахара в крови. \
Поэтому с особой осторожностью их следует употреблять тем, у кого диагностирован диабет.'
            bot.send_message(call.message.chat.id, msg_a4)
        elif call.data=='b1':
            msg_b1='Этот тропический фрукт помогает организму поддерживать здоровье сердца и почек, \
а также усиливает внимание и активизирует работу мозга. Учёные утверждают, что достаточное количество \
этого минерала в организме предупреждает образование камней в почках, способствует нормализации артериального \
давления и на 27% снижает риск сердечного приступа.'
            bot.send_message(call.message.chat.id, msg_b1)
        elif call.data=='b2':
            msg_b2='Банан на 75% состоит из воды, однако всё же, он очень питателен и в \
первую очередь богат калием. Среди витаминов больше всего содержит B4 и C.'
            bot.send_message(call.message.chat.id, msg_b2)
        elif call.data=='b3':
            msg_b3='Недавно с успехом завершился 10-ти летний гуманитарный проект \
группы австралийских исследователей, целью которого было вывести бананы, богатые провитамином А. \
Такую задачу перед учёными поставили в связи с тем, что в Уганде и ряде других африканских стран сотни тысяч \
детей умирают или становятся слепыми из-за нехватки этого витамина в организме. Теперь проблему отчасти удастся \
решить, благодаря будущим урожаям «золотых» бананов.'
            bot.send_message(call.message.chat.id, msg_b3)
        elif call.data=='b4':
            msg_b4='Банан активно выводит из организма жидкость, вследствие чего происходит \
сгущение крови и уменьшение её притока к органам и частям тела. Поэтому людям, страдающим варикозным \
расширением вен, мужчинам, имеющим проблемы с эрекций, и больным тромбофлебитом не следует увлекаться поеданием бананов.'
            bot.send_message(call.message.chat.id, msg_b4)
        elif call.data=='g1':
            msg_g1='Груша полезна пищевыми волоконами, улучшающих работу кишечника, отвечающих за \
выведение вредных веществ и токсинов, снижающих уровень холестерина; калием, полезным для сердца минералом; \
арбутином (до 60 мг/ 100 г в некоторых сортах), способного предупреждать развитие патологий почек и мочевого пузыря.'
            bot.send_message(call.message.chat.id, msg_g1)
        elif call.data=='g2':
            msg_g2='Среди витаминов больше всего содержит B4 и C. Следует учитывать, что концентрация всех минералов \
и некоторых витаминов увеличивается (часто в 4-5 раз) в сушёных плодах груши. Однако вместе с тем в те же 4-5 раз растёт \
и калорийность фрукта за счёт заметного увеличения количества сахара.'
            bot.send_message(call.message.chat.id, msg_g2)
        elif call.data=='g3':
            msg_g3='Китай, Италия, США.'
            bot.send_message(call.message.chat.id, msg_g3)
        elif call.data=='g4':
            msg_g4='<b>Всё хорошо в меру: переизбыток так же плох как и дефицит</b>. Из-за каменистых клеток \
избыток груш считается «тяжёлой» пищей даже для людей со здоровым желудочно-кишечным трактом. \
Ну а при остром и хроническом панкреатите(воспалении поджелудочной железы) вообще желательно избегать употребления груш в пищу.'
            bot.send_message(call.message.chat.id, msg_g4, parse_mode='html')
        elif call.data=='pi1':
            msg_pi1='Ананас зачастую ценят не за стандартный набор полезных веществ, которые можно найти и в любом другом \
фрукте, а за бромелайн, сосредоточенный в основном в сердцевине плода. Протеолитический фермент бромелайн способствует \
расщеплению белков. Таким образом, ананас может помочь лучше усвоиться белковой пище (мясо, рыба, кисломолочные продукты).\
\nПомимо участия в процессе расщепления белков, бромелайн также оказывает противовоспалительное воздействие и борется\
с отёками. Вместе с содержащейся в ананасе клетчаткой, этот фермент способствует нормализации перистальтики кишечника, \
благотворно влияет на пищеварение и помогает избавиться от запоров. Учёные утверждают, что бромелайн предупреждает \
образование тромбов, поскольку проявляет антикоагулянтную активность.'
            bot.send_message(call.message.chat.id, msg_pi1)
        elif call.data=='pi2':
            msg_pi2='Что касается витаминного коктейля, содержащегося в ананасе, \
то наибольшей концентрацией отличается витамин С. Будучи сильным антиоксидантом, он помогает защищать здоровые клетки, \
подвергающиеся атакам свободных радикалов, вносит свой вклад в защиту организма от бактериальных и вирусных инфекций, \
а также помогает усваиваться железу. Так же ананас обогащён всеми витаминами группы В.'
            bot.send_message(call.message.chat.id, msg_pi2)
        elif call.data=='pi3':
            msg_pi3='Учёные ищут применение биомассе, которая остаётся после выращивания ананасов, поскольку волокна \
стеблей и листьев растения очень прочны. Так, одна испанская исследовательница разработала метод производства кожи из \
ананасовых листьев. Получился очень качественный материал, из которого можно шить сумки, обувь и использовать его \
в мебельной индустрии. Такая кожа легче и на 30% дешевле натуральной.'
            bot.send_message(call.message.chat.id, msg_pi3)
        elif call.data=='pi4':
            msg_pi4='<b>Всё хорошо в меру: переизбыток так же плох как и дефицит</b>. Увлекаться поеданием этого фрукта \
не стоит, ведь его потребление в больших количествах сопровождается попаданием в организм кислоты и чревато раздражением \
слизистых оболочек желудка и ротовой полости. По этой причине свежий ананас нельзя есть при язвенной болезни и гастрите.'
            bot.send_message(call.message.chat.id, msg_pi4, parse_mode='html')
        elif call.data=='av1':
            msg_av1='О лечебных свойствах авокадо знали ещё ацтеки, которые начали культивировать это растение порядка \
5 тысяч лет назад на территории современной Мексики. Они называли авокадо «лесным маслом» и использовали составляющие \
плода для устранения чесотки и избавления от перхоти. Сегодня знания о лечебных свойствах авокадо заметно расширились, \
и теперь различные части этого растения рассматриваются в качестве лекарственной основы для борьбы с такими заболеваниями \
как атеросклероз, остеоартрит, сахарный диабет 2-го типа, а также для профилактики гипертонии, малокровия, болезней ЖКТ, \
обусловленных повышенной кислотностью.'
            bot.send_message(call.message.chat.id, msg_av1)
        elif call.data=='av2':
            msg_av2='Авокадо насыщен витаминами группы B4, A, E, C и B3.'
            bot.send_message(call.message.chat.id, msg_av2)
        elif call.data=='av3':
            msg_av3='Косточка очень аккуратно очищается от внешней кожицы и опускается тупым концом на дно узкой рюмки \
так, чтобы оказаться наполовину в воде. Узкий сосуд нужен для того, чтобы удерживать косточку в вертикальном положении. \
Пересадка в землю производится, когда корень прорастает в этом временном сосуде на 3 см. Обычно на это уходит 2-3 недели.'
            bot.send_message(call.message.chat.id, msg_av3)
        elif call.data=='av4':
            msg_av4='В группе риска среди любителей авокадо оказываются кормящие матери, беременные женщины, представители \
возрастной категории от 65 лет, а также люди с ослабленной иммунной системой. Причина заключается в активности бактерии \
Listeria monocytogenes, которую федеральные следователи американского санитарного надзора FDA выявили на кожуре каждого \
пятого авокадо. В тестировании 2014-2016 гг. заражёнными оказались почти 18% плодов. Листерии относятся к внутриклеточным \
паразитам и при попадании в организм человека или животного могут, помимо диареи, вызвать тошноту, боль в животе, \
сильную головную боль, скованность мышц, заметное повышение температуры до 39°С и некоторые другие признаки листериоза. \
У беременных высока опасность выкидыша, при этом сами женщины переносят заболевание сравнительно легко. \
Примерно в 15% случаев листериоз у человека заканчивается смертью больного.\nДля того, чтобы избежать распространение \
бактерии с кожуры на мякоть авокадо, плод рекомендуют сначала мыть с помощью щётки, а затем после разрезания, выедать \
съедобную мякоть ложкой, а оставшиеся части плода выбрасывать. Кипячение продукта при 100°С убивает бактерию в течение 3 минут.'
            bot.send_message(call.message.chat.id, msg_av4)
        elif call.data=='c1':
            msg_c1='Мякоть кокоса улучшает пищеварение и зрение, восстанавливает силы, повышает иммунитет, \
препятствует возникновению сердечно-сосудистых и онкологических заболеваний. Кокос обладает противовоспалительным, \
антимикробным действием.\nКокосовое молоко имеет приятный запах и сладкий вкус, оно очень полезно для кожи и содержит около \
27% жира, 6% углеводов и 4% белка. Молочко прекрасно освежает и тонизирует кожу, восстанавливает упругость стареющей и \
вялой кожи. Особенно успешно с его помощью можно лечить угревую сыпь и аллергические высыпания, успокаивать и \
подсушивать воспаленную кожу.'
            bot.send_message(call.message.chat.id, msg_c1)
        elif call.data=='c2':
            msg_c2='Наибольшее количество витаминов в кокосе из групп B1, C, B3, а из минералов преобладает \
фосфор, магний и калий.'
            bot.send_message(call.message.chat.id, msg_c2)
        elif call.data=='c3':
            msg_c3='Название кокос происходит от португальского слова 16-го века coco, означающего "голова" или "череп" \
после трех углублений на скорлупе кокоса, которые напоминают черты лица. Кокос и кокосовый орех, по-видимому, появились \
в результате встреч 1521 года португальскими и испанскими исследователями у жителей Тихоокеанских островов: скорлупа \
кокосового ореха напоминает им о привидении или ведьме из португальского фольклора по имени коко (также кока). \
На Западе он первоначально назывался nux indica, название, использованное Марко Поло в 1280 году во время пребывания на \
Суматре. Он позаимствовал этот термин у арабов, которые называли его "джавз хинди", что переводится как "индийский орех". \
Тенга, его тамильское / малаяламское название, использовалось в подробном описании кокоса, найденного в "Итеринарио" \
Людовико ди Вартема, опубликованном в 1510 году, а также в более позднем Hortus Indicus Malabaricus. \
Видовое название nucifera происходит от латинских слов nux (орех) и fera (подшипник), что означает "орехоносный".'
            bot.send_message(call.message.chat.id, msg_c3)
        elif call.data=='c4':
            msg_c4='Кокос противопоказан людям со склонностью к лишнему весу и диарее. Кокосы противопоказаны \
в случае индивидуальной непереносимости, а также при гиперфункции щитовидной железы, так как они влияют на работу \
этого органа.'
            bot.send_message(call.message.chat.id, msg_c4)  
        elif call.data=='t1':
            msg_t1='В традиционных терапевтических системах плоды мандарина использовались, главным образом, \
как регуляторы работы ЖКТ (при умеренном употреблении), а мандариновая кожура – ещё и как спазмолитическое, \
стимулирующее и противовоспалительное средство.\nЖёлтый пигмент лютеин в составе мандарина вместе с прочими \
лютеиносодержащими продуктами может помочь восстанавливать зрительную функцию.\nИз плодов и губчатой части вяленых \
корок мандарина получают гесперидин – естественное соединение (источник гесперитина в организме), которое характеризуется \
комплексным воздействием на сердечно-сосудистую систему.'
            bot.send_message(call.message.chat.id, msg_t1)
        elif call.data=='t2':
            msg_t2='Мандарин в себе наиболее богат витамином С (порядка 27 мг/100 г, а в некоторых сортах его может быть \
в 2 раза больше) и витаминами из группы B.'
            bot.send_message(call.message.chat.id, msg_t2)
        elif call.data=='t3':
            msg_t3='Наружный слой мандарина (который из-за жёлто-оранжевой окраски зрелых плодов называют флаведо — от лат. \
flavus «жёлтый») содержит большое количество крупных просвечивающих шаровидных желёзок, содержащих эфирное масло. \
Внутренний слой из-за белого цвета, характерного для зрелых плодов, называется альбедо — от лат. albus «белый»; \
у мандарина альбедо рыхлое, так что мякоть легко отделяется от кожуры. Этот слой на ранних этапах развития плода \
служит водоносным слоем, но после формирования соковых мешочков он постепенно атрофируется, обретая губчатую структуру. \
Сильный аромат плодов мандарина отличает его от других цитрусовых, а мякоть обычно слаще мякоти апельсина.'
            bot.send_message(call.message.chat.id, msg_t3)
        elif call.data=='t4':
            msg_t4='• Мандарин, как и большинство других цитрусовых, может вызвать аллергические реакции.\
\n• Мандарины повышают уровень кислотности желудочного сока. По этой причине они могут навредить людям с язвенной болезнью \
и гастритом, обусловленным повышенной кислотностью.\n• Как продукт, богатый глюкозой, мандарин (плод) повышает \
концентрацию сахара в крови, что его употребление становится нежелательным при диабете.'
            bot.send_message(call.message.chat.id, msg_t4)   
            
if __name__ == '__main__':            
    bot.polling(none_stop=True)