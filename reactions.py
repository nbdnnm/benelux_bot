BENELUX_MAIN = 1186369530
BOTNAME = "beneluxbot"

# Storing last 'welcome' message ids
PRIOR_WELCOME_MESSAGE_ID = {
    BENELUX_MAIN: 0
}


def new_member_greeting(bot, update):
    message_id = update.message.message_id
    chat_id = update.message.chat.id
    new_user = update.message.new_chat_members[0]
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

Ссылки на остальные полезные ресурсы https://telegra.ph/RU-Benelux-07-15

Со мной вы можете пообщаться в личном чате @beneluxbot
""".format(name)

        message = bot.send_message(chat_id=chat_id, reply_to_message_id=message_id, text=msg)

        PRIOR_WELCOME_MESSAGE_ID[chat_id] = int(message.message_id)


# Resolve message data to a readable name
def get_name(user):
    try:
        name = "@" + user.username
    except:
        try:
            name = user.first_name
        except:
            return ""
    return name
