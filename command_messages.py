import telegram

from base import Session
from groups_messages_listener import GroupsMessagesListener


def delete_message(bot, update):
    bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)


def ruling(bot, update):
    update.message.reply_text(
        """ 
        1. Рулинг и статус кенис мигранта в общем случае не связаны (хотя в большинсте случаев КМ получают рулинг)
2. Рулинг 30% - это возможность получить необлагаемыми налого ДО 30% зарплаты (может быть меньше)
3. Немного деталей на английском [www.iamsterdam.com](https://www.iamsterdam.com/en/living/take-care-of-official-matters/highly-skilled-migrants/thirty-percent-ruling/30-percent-ruling-indepth)
4. Оригинал всего про рулинг [www.belastingdienst.nl](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/internationaal/werken_wonen/tijdelijk_in_een_ander_land_werken/u_komt_in_nederland_werken/30_procent_regeling/)
5. Рулинг позволяет обменять иностранные права на нидерландские без лишних телодвижений и почти без затрат (суммарно обмен получается до 100 евро)
6. Прикинуть зп с учетом рулинга можно там http://www.thetax.nl  
Еще детали про рулинг: https://rabotaem.nl/info/likbez/chto-takoe-30-ruling/""", parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True)
    delete_message(bot, update)


def driver_license(bot, update):
    update.message.reply_text("""1. Если у вас есть рулинг, ваши прежние права можно обменять. Подробности здесь: https://rabotaem.nl/docs/inostrannye_prava_v_niderlandah/
2. Если рулинга нет, то права нужно получать с нуля в обычном порядке""")
    delete_message(bot, update)


def bank_cards(bot, update):
    update.message.reply_text("""Самые распространенные карты в Нидерландах - дебетные карты Maestro, чаще называемые PIN-kaart (матчасть здесь: 
https://en.wikipedia.org/wiki/Maestro_(debit_card) и https://nl.wikipedia.org/wiki/PIN_(betaalkaart)).
Кредитные карты принимаются в туристических местах; в обычных супермаркетах и магазинах ими расплатиться не получится (но с них всегда можно снять наличные в банкомате). 
Если нужна карта для платы через интернет - то можно заказать в своем банке MasterCard (хотя эти карты выпускаются в Нидерландах по большей части International Card Services (ICS), хоть и запрос вы отправите в свой банк). 
Чтобы получить нормальную кредитную карту, например, в АБН АМРО, как минимум нужно чтоб на счет поступила первая зарплата от работодателя плюс после этого контракт был валиден минимум год. Если условия не позволяют получить кредитную карту, можно запросить prepaid MasterCard.""")
    delete_message(bot, update)


def google_doc(bot, update):
    update.message.reply_text("""Гугл док наполняемый участниками чата
https://goo.gl/5IdCbk""")
    delete_message(bot, update)


def work(bot, update):
    update.message.reply_text("""Статьи о работе, учебе, кеннисмигрантстве:  
[В Голландию: учиться или работать](https://rabotaem.nl/moving/v-gollandiyu-uchitsya-ili-rabotat/)  
[Предпринимательство для КМов, иностранных студентов и ученых](https://rabotaem.nl/finances/predprinimatelstvo-dlya-kmov-inostrannyh-studentov-i-uchenyh/)  
[Увольнение, поиск работы и смена работодателя](https://rabotaem.nl/work/uvolnenie-poisk-raboty-i-smena-rabotodatelya/)  
[Рабочий IT рынок Нидерландов — анализ 2017 года](https://rabotaem.nl/news/rabochij-rynok-niderlandov-analiz-2017-goda/)""",
                              parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    delete_message(bot, update)


def pets(bot, update):
    update.message.reply_text("""Как перевезти животное в Нидерланды и что с ним делать здесь в статьях:
https://rabotaem.nl/moving/pereezd-s-zhivotnymi-kak-i-chto/
https://rabotaem.nl/everyday/oteli-dlya-zhivotnyh/""")
    delete_message(bot, update)


def bank_account(bot, update):
    update.message.reply_text(
        """Подробно об открытии счетов можно почитать здесь https://rabotaem.nl/finances/vybor-banka-i-kart/""")
    delete_message(bot, update)


def post_taxes(bot, update):
    update.message.reply_text("""За посылки из-за пределов ЕС нужно оплачивать пошлины.  
Оплата производится сразу при доставке посылки.  
Примерную стоимость можно прикинуть, почитав по ссылкам:  
[postnl.nl...](https://www.postnl.nl/ontvangen/pakket-ontvangen/pakket-uit-het-buitenland/bijkomende-kosten-bij-het-importeren-van-goederen-uit-het-buitenland/)  
[belastingdienst.nl...](https://www.belastingdienst.nl/wps/wcm/connect/nl/internetaankopen/content/hoeveel-betaal-ik-de-douane-als-ik-iets-koop-bij-buitenlandse-webshop)""",
                              parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)
    delete_message(bot, update)


def shops(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/magaziny-pervoj-neobhodimosti/""")
    delete_message(bot, update)


def buy_buckwheat(bot, update):
    update.message.reply_text("""Привычные товары можно найти в русских или польских магазинах (последние надо гуглить по словам polski sklep)
Примеры:
Амстердам: http://minimixamsterdam.com/nl/
http://www.priwetrossia.nl/index.php
Утрехт: http://www.slavjanskidvor.nl
Альмере: http://www.slavyankamarket.com/webshop/nl
Хаарлем: https://www.facebook.com/SmaczekHaarlem/
Кроме того, привычные продукты можно поискать в турецких магазинах""", disable_web_page_preview=True)
    delete_message(bot, update)


def mobile(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/mobilnaya-svyaz-v-niderlandah/""")
    delete_message(bot, update)


def devices(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/poisk-i-pokupka-tehniki-i-prochej-elektroniki/""")
    delete_message(bot, update)


def utilities(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/vybor-postavshhikov-kommunalnyh-uslug/""")
    delete_message(bot, update)


def rassvet(bot, update):
    update.message.reply_text("""Форум со множеством инфы по Нидерландам https://rassvet.com""")
    delete_message(bot, update)


def transport(bot, update):
    update.message.reply_text("""https://rabotaem.nl/transport/obshhestvennyj-transport-v-niderlandah-i-ego-oplata/""")
    delete_message(bot, update)


def bicycle(bot, update):
    update.message.reply_text("""https://rabotaem.nl/everyday/velosiped-pokupka-strahovka-ispolzovanie/""")
    delete_message(bot, update)


def parents_invitation(bot, update):
    update.message.reply_text("""https://rabotaem.nl/docs/sdelat-priglashenie-dlya-roditelej-instruktsiya/""")
    delete_message(bot, update)


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
    delete_message(bot, update)


def start(bot, update):
    update.message.reply_text("""Здравствуйте!
Я бот чатов Бенелюкс.
Вы можете запросить справочную информацию введя слэш (/) и выбрав интересующий пункт.""")

