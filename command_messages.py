import telegram

from base import Session
from groups_messages_listener import GroupsMessagesListener


def ruling(bot, update):
    update.message.reply_text(
        """1. Рулинг и статус кенис мигранта в общем случае не связаны (хотя в большинсте случаев КМ получают рулинг)
2. Рулинг 30% - это возможность получить необлагаемыми налого ДО 30% зарплаты (может быть меньше)
3. Немного деталей на английском [www.iamsterdam.com](https://www.iamsterdam.com/en/living/take-care-of-official-matters/highly-skilled-migrants/thirty-percent-ruling/30-percent-ruling-indepth)
4. Оригинал всего про рулинг [www.belastingdienst.nl](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/internationaal/werken_wonen/tijdelijk_in_een_ander_land_werken/u_komt_in_nederland_werken/30_procent_regeling/)
5. Рулинг позволяет обменять иностранные права на нидерландские без лишних телодвижений и почти без затрат (суммарно обмен получается до 100 евро)
6. Прикинуть зп с учетом рулинга можно там http://www.thetax.nl  
Еще детали про рулинг: https://rabotaem.nl/info/likbez/chto-takoe-30-ruling/""", parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True)


def driver_license(bot, update):
    update.message.reply_text("""1. Если у вас есть рулинг, ваши прежние права можно обменять. Подробности здесь: http://rabotaem.nl/docs/inostrannye_prava_v_niderlandah/
2. Если рулинга нет, то права нужно получать с нуля в обычном порядке""")


def bank_cards(bot, update):
    update.message.reply_text("""Самые распространенные карты в Нидерландах - дебетные карты Maestro, чаще называемые PIN-kaart (матчасть здесь: 
https://en.wikipedia.org/wiki/Maestro_(debit_card) и https://nl.wikipedia.org/wiki/PIN_(betaalkaart)).
Кредитные карты принимаются в туристических местах; в обычных супермаркетах и магазинах ими расплатиться не получится (но с них всегда можно снять наличные в банкомате). 
Если нужна карта для платы через интернет - то можно заказать в своем банке MasterCard (хотя эти карты выпускаются в Нидерландах по большей части International Card Services (ICS), хоть и запрос вы отправите в свой банк). 
Чтобы получить нормальную кредитную карту, например, в АБН АМРО, как минимум нужно чтоб на счет поступила первая зарплата от работодателя плюс после этого контракт был валиден минимум год. Если условия не позволяют получить кредитную карту, можно запросить prepaid MasterCard.""")


def google_doc(bot, update):
    update.message.reply_text("""Гугл док наполняемый участниками чата
https://goo.gl/5IdCbk""")


def work(bot, update):
    update.message.reply_text("""Статьи о работе, учебе, кеннисмигрантстве:  
[В Голландию: учиться или работать](https://rabotaem.nl/moving/v-gollandiyu-uchitsya-ili-rabotat/)  
[Предпринимательство для КМов, иностранных студентов и ученых](https://rabotaem.nl/finances/predprinimatelstvo-dlya-kmov-inostrannyh-studentov-i-uchenyh/)  
[Увольнение, поиск работы и смена работодателя](https://rabotaem.nl/work/uvolnenie-poisk-raboty-i-smena-rabotodatelya/)  
[Рабочий IT рынок Нидерландов — анализ 2017 года](https://rabotaem.nl/news/rabochij-rynok-niderlandov-analiz-2017-goda/)""",
                              parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)


def pets(bot, update):
    update.message.reply_text("""Как перевезти животное в Нидерланды и что с ним делать здесь в статьях:
https://rabotaem.nl/moving/pereezd-s-zhivotnymi-kak-i-chto/
https://rabotaem.nl/everyday/oteli-dlya-zhivotnyh/""")


def bank_account(bot, update):
    update.message.reply_text(
        """Подробно об открытии счетов можно почитать здесь https://rabotaem.nl/finances/vybor-banka-i-kart/""")


def post_taxes(bot, update):
    update.message.reply_text("""За посылки из-за пределов ЕС нужно оплачивать пошлины.  
Оплата производится сразу при доставке посылки.  
Примерную стоимость можно прикинуть, почитав по ссылкам:  
[postnl.nl...](https://www.postnl.nl/ontvangen/pakket-ontvangen/pakket-uit-het-buitenland/bijkomende-kosten-bij-het-importeren-van-goederen-uit-het-buitenland/)  
[belastingdienst.nl...](https://www.belastingdienst.nl/wps/wcm/connect/nl/internetaankopen/content/hoeveel-betaal-ik-de-douane-als-ik-iets-koop-bij-buitenlandse-webshop)""",
                              parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)


def shops(bot, update):
    update.message.reply_text("""http://rabotaem.nl/everyday/magaziny-pervoj-neobhodimosti/""")


def buy_buckwheat(bot, update):
    update.message.reply_text("""Привычные товары можно найти в русских или польских магазинах (последние надо гуглить по словам polski sklep)
Примеры:
Амстердам: http://minimixamsterdam.com/nl/
http://www.priwetrossia.nl/index.php
Утрехт: http://www.slavjanskidvor.nl
Альмере: http://www.slavyankamarket.com/webshop/nl
Хаарлем: https://www.facebook.com/SmaczekHaarlem/
Кроме того, привычные продукты можно поискать в турецких магазинах""", disable_web_page_preview=True)


def mobile(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/mobilnaya-svyaz-v-niderlandah/""")


def devices(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/poisk-i-pokupka-tehniki-i-prochej-elektroniki/""")


def utilities(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/vybor-postavshhikov-kommunalnyh-uslug/""")


def rassvet(bot, update):
    update.message.reply_text("""Форум со множеством инфы по Нидерландам https://rassvet.com""")


def transport(bot, update):
    update.message.reply_text("""https://rabotaem.nl/transport/obshhestvennyj-transport-v-niderlandah-i-ego-oplata/""")


def bicycle(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/velosiped-pokupka-strahovka-ispolzovanie/""")


def parents_invitation(bot, update):
    update.message.reply_text("""https://rabotaem.nl/docs/sdelat-priglashenie-dlya-roditelej-instruktsiya/""")


def list_my_listeners(bot, update):
    session = Session()
    user = update.message.from_user.username
    user_data = session.query(GroupsMessagesListener).filter_by(username=user).first()
    text = str()
    for chat in user_data.listeners.keys():
        text += "\nCHAT " + chat + ":\n"
        for listener in user_data.listeners[chat]:
            text += listener + "\n"
    update.message.reply_text(text)


def apostil(bot, update):
    update.message.reply_text("""Про апостили ещё не написали. Сложная тема, знаете ли.""")


def start(bot, update):
    update.message.reply_text("""Здравствуйте!
Я бот чатов Бенелюкс.
Вы можете запросить справочную информацию введя слэш (/) и выбрав интересующий пункт.""")


def chats(bot, update):
    update.message.reply_text("""@inBenelux – основной чат
@inBenelux_questions - чат только для вопросов и ответов
@velobenelux – всё о велосипедах
@learning_nederlands – чат про изучение голландского
@ITinBenelux – чат об ИТ
@benelux_foodie – о еде в Бенилюксе
@benelux_events – канал про интересные мероприятия и праздники
@beneluxevents - чат о мероприятиях
@ijburg_ru – чатик русскоязычных жителей Amsterdam-IJburg (Ижбург!) 
@inAlmere – русскоязычные жители Almere - лучшего города приАмстердамья
@BNL вещества – про различные субстанции для изменения сознания, вход по инвайтам, спрашивайте в основном чате
@parentsInBenelux – чатик для родителей
@nlriders – русскоязычные мотобратья и мотосестры Бенилюкса""")
