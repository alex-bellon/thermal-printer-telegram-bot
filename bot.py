import os
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def help(update, context):
    
    update.message.reply_text('Send a file or some text to have it printed!')

def log_message(message, sender):

    now = datetime.now()
    time = now.strftime('%Y-%m-%d')
    log = open('logs/log-' + time + '.txt', 'a')
    if sender.last_name:
        sender = sender.first_name + ' ' + sender.last_name + ' (@' + sender.username + ')'
    else:
        sender = sender.first_name + ' (@' + sender.username + ')'

    entry = time + ' ' + sender + ': ' + message
    log.write(entry + '\n')
    print(entry)

def print_text(update, context):
   
    message = update.message
    text = message.text
    sender = message.from_user
    
    os.system('echo "' + text + '" > print.txt')
    success = os.system('lp -d thermal-printer print.txt')

    log_message(text, sender)

    if success == 0:
        update.message.reply_text('Text successfully printed!')
    else:
        update.message.reply_text('Text did not print :(')

def print_image(update, context):
   
    message = update.message
    sender = message.from_user
    image_list = message.photo
    image = image_list[0].get_file().download(custom_path="print")

    log_message('image', sender)
    
    success = os.system('lp -d thermal-printer print')

    if success == 0:
        update.message.reply_text('Image successfully printed!')
    else:
        update.message.reply_text('Image did not print :(')


def main():
    token = str(open('telegram.token', 'r').read().strip('\n'))
    updater = Updater(token, use_context=True)

    disp = updater.dispatcher

    disp.add_handler(CommandHandler('help', help))
    disp.add_handler(MessageHandler(Filters.text, print_text))
    disp.add_handler(MessageHandler(Filters.photo, print_image))

    updater.start_polling()
    updater.idle()

main()
