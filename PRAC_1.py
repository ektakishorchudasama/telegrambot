import telepot
token = '1233151914:AAEE_4KEwt7Dyg0pBG6rpGlqj1Znc9BlFPM'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe()) 
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle) 
