def ruling(bot, update):
    update.message.reply_text(
        """1. Рулинг и статус кенис мигранта в общем случае не связаны (хотя в большинсте случаев КМ получают рулинг
2. Рулинг 30% - это возможность получить необлагаемыми налого ДО 30% зарплаты (может быть меньше)
3. Немного деталей на английском здесь: https://www.iamsterdam.com/en/living/take-care-of-official-matters/highly-skilled-migrants/thirty-percent-ruling/30-percent-ruling-indepth
4. Оригинал всего про рулинг здесь: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/internationaal/werken_wonen/tijdelijk_in_een_ander_land_werken/u_komt_in_nederland_werken/30_procent_regeling/
5. Рулинг позволяет обменять иностранные права на нидерландские без лишних телодвижений и почти без затрат (суммарно обмен получается до 100 евро)
6. Прикинуть зп с учетом рулинга можно здесь: http://www.thetax.nl """)


def driver_license(bot, update):
    update.message.reply_text("""1. Если у вас есть рулинг, ваши прежние права можно обменять. Подробности здесь: http://rabotaem.nl/docs/inostrannye_prava_v_niderlandah/
2. Если рулинга нет, то права нужно получать с нуля в обычном порядке""")


def bank_cards(bot, update):
    update.message.reply_text("""Самые распространенные карты в Нидерландах - дебетные карты Maestro, чаще называемые PIN-caards (матчасть здесь: 
https://en.wikipedia.org/wiki/Maestro_(debit_card) и https://nl.wikipedia.org/wiki/PIN_(betaalkaart)).
Кредитные карты принимаются в туристических местах; в обычных супермаркетах и магазинах ими расплатиться не получится (но с них всегда можно снять наличные в банкомате). 
Если нужна карта для платы через интернет - то можно заказать в своем банке MasterCard (хотя эти карты выпускаются в Нидерландах по большей части International Card Services (ICS), хоть и запрос вы отправите в свой банк). 
Чтобы получить нормальную кредитную карту, например, в АБН АМРО, как минимум нужно чтоб на счет поступила первая зарплата от работодателя плюс после этого контракт был валиден минимум год. Если условия не позволяют получить кредитную карту, можно запросить prepaid MasterCard.""")


def google_doc(bot, update):
    update.message.reply_text('https://goo.gl/5IdCbk')


def bank_account(bot, update):
    update.message.reply_text(
        """Подробно об открытии счетов можно почитать здесь https://rabotaem.nl/finances/vybor-banka-i-kart/""")


def post_taxes(bot, update):
    update.message.reply_text("""За посылки из-за пределов ЕС нужно оплачивать пошлины.
Оплата производится сразу при доставке посылки/
Примерную стоимость можно прикинуть, почитав по ссылкам:
https://www.postnl.nl/ontvangen/pakket-ontvangen/pakket-uit-het-buitenland/bijkomende-kosten-bij-het-importeren-van-goederen-uit-het-buitenland/
https://www.belastingdienst.nl/wps/wcm/connect/nl/internetaankopen/content/hoeveel-betaal-ik-de-douane-als-ik-iets-koop-bij-buitenlandse-webshop""")


def shops(bot, update):
    update.message.reply_text("""http://rabotaem.nl/everyday/magaziny-pervoj-neobhodimosti/""")


def rassvet(bot, update):
    update.message.reply_text('Форум со множеством инфы по Нидерландам https://rassvet.com')


def transport(bot, update):
    update.message.reply_text('https://rabotaem.nl/transport/obshhestvennyj-transport-v-niderlandah-i-ego-oplata/')


def bicycle(bot, update):
    update.message.reply_text('https://rabotaem.nl/everyday/velosiped-pokupka-strahovka-ispolzovanie/')


def apostil(bot, update):
    update.message.reply_text('Про апостили ещё не написали. Сложная тема, знаете ли.')
