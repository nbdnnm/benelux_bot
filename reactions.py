BENELUX_MAIN = 1186369530
BOTNAME = "beneluxbot"

# Storing last 'welcome' message ids
PRIOR_WELCOME_MESSAGE_ID = {
    BENELUX_MAIN: 0
}


def new_member_greating(bot, update):
    """ Welcomes new chat member """

    user_id = update.message.from_user.id
    message_id = update.message.message_id
    chat_id = update.message.chat.id
    new_user = update.message._new_chat_member
    name = get_name(new_user)

    # Bot was added to a group chat
    if new_user.username == BOTNAME:
        return False
    # Another user joined the chat
    else:
        try:
            if PRIOR_WELCOME_MESSAGE_ID[chat_id] > 0:
                bot.delete_message(chat_id=chat_id, message_id=PRIOR_WELCOME_MESSAGE_ID[chat_id])
        except:
            pass

        msg = """Здравствуйте {}!
Рады приветствовать Вас в нашем чате.
Будем благодарны если вы представитесь.
У нас уже собрано очень много информации по переезду и жизни в странах Бенелюкс.
Пожалуйста, воспользуйтесь поиском по чату, а так же ознакомьтесь с нашими ресурсами:
https://rabotaem.nl
https://goo.gl/5IdCbk
http://telegra.ph/Benelux-ru-chats-05-22

Со мной вы можете пообщаться в личном чате.
После перехода в него введите слэш (/) в текстовое поле и выберите команду из выпавшего списка.
""".format(name)

        message = bot.sendMessage(chat_id=chat_id, reply_to_message_id=message_id, text=msg)

        PRIOR_WELCOME_MESSAGE_ID[chat_id] = int(message.message_id)


# Resolve message data to a readable name
def get_name(new_user):
    try:
        name = new_user.first_name
    except (NameError, AttributeError):
        try:
            name = new_user.username
        except (NameError, AttributeError):
            return ""
    return name
