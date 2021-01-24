import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def help(update, context):
    
    update.message.reply_text('Send a file or some text to have it printed!')


def print_text(update, context):
    
    text = update.message.text
    
    os.system('echo "' + text + '" > print.txt')
    success = os.system('lp -d thermal-printer print.txt')

    if success == 0:
        update.message.reply_text('Text successfully printed!')
    else:
        update.message.reply_text('Text did not print :(')

def print_image(update, context):
    
    image_list = update.message.photo
    image = image_list[0].get_file().download(custom_path="print")

    success = os.system('lp -d thermal-printer print')

    if success == 0:
        update.message.reply_text('Image successfully printed!')
    else:
        update.message.reply_text('Image did not print :(')


def main():
    token = open('telegram.token', 'r').read()
    updater = Updater(token, use_context=True)

    disp = updater.dispatcher

    disp.add_handler(CommandHandler('help', help))
    disp.add_handler(MessageHandler(Filters.text, print_text))
    disp.add_handler(MessageHandler(Filters.photo, print_image))

    updater.start_polling()
    updater.idle()

main()
