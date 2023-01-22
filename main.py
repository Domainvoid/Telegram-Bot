import telegram
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler
from bot_token import Token
import keyboard as ky
import sql_database as sql
import logging
import os
import teleclass as tcl
bot = telegram.Bot(token=Token)
logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
image ='/home/abhinav/Documents/telegram_bot/pic.png'
path=''
file_path=[]
directory = "branches/Bca/"
subdirectories = os.listdir(directory)
def start(update, context):
    sql.checkbd()
    logging.debug("Start function called")
    user_id = update.message.from_user.id
    user_details = sql.check_user_details(user_id)
    if user_details is not None:

        if bool(user_details[2]):
            message = bot.send_photo(chat_id=user_id,photo=open(image,'rb'),caption="Choose Your Subject!",reply_markup=ky.create_keyboard(data=f'branches/{user_details[1]}/'))
            logging.debug(f"registered user-{user_details[0]} found!,sending branch!")
        else:
            message=bot.send_photo(chat_id=user_id, photo=open(image,'rb'), reply_markup=ky.option_board())
    else:
        message=bot.send_photo(chat_id=user_id, photo=open(image,'rb'), reply_markup=ky.option_board())
    context.user_data["message_id"] = message.message_id



def register(update,context):
    print("register block start !")
    path='branches/'
    query = update.callback_query
    message_id = context.user_data["message_id"]
    chat_id = query.message.chat_id
    bot.delete_message(chat_id=chat_id, message_id=message_id)
    message = bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'), caption=f"Choose Your Branch!",reply_markup=ky.create_keyboard(data=path))
    context.user_data["message_id"] = message.message_id
    print("register blockended!")


def branch(update,context):
    print("branch block active")
    query = update.callback_query
    print("query")

    context.user_data["message_id"] =query.message.message_id


    message_id = context.user_data["message_id"]
    print(message_id)

    chat_id = query.message.chat_id
    print("chat id")
    user_details = sql.check_user_details(chat_id)
    print("user det")
    if user_details is not None:
        path = f'branches/{user_details[1]}'
        print(path)
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        message = bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'), caption=f"Choose Your Subject!",reply_markup=ky.create_keyboard(data=path))
        context.user_data["message_id"] = message.message_id

    else:
        print("user not found !")
        path = f'branches/{query.data}'
        print("SUB :", path)
        sql.add_user(chat_id, query.data)
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        message = bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'), caption=f"Choose Your Subject!",
                                 reply_markup=ky.create_keyboard(data=path))
        context.user_data["message_id"] = message.message_id

def subject(update,context):
    print("sub block started")
    query = update.callback_query

    context.user_data["message_id"] = query.message.message_id
    user_details = sql.check_user_details(query.message.chat_id)
    path = f'branches/{user_details[1]}/{query.data}'
    print("SUB :",path)

    file_path=tcl.file_path_va(path=path)
    print(file_path)
    print("done")
    message_id = context.user_data["message_id"]
    chat_id = query.message.chat_id
    bot.delete_message(chat_id=chat_id, message_id=message_id)
    message = bot.send_photo(chat_id=chat_id,photo=open(image,'rb'),caption=f"Choose Your File!", reply_markup=ky.create_keyboard(data=path))
    context.user_data["message_id"] = message.message_id
    print("sub block ended!")

def file_download(update,context):
    print("filedown start")
    query=update.callback_query
    print(query.data)
    context.user_data["message_id"] = query.message.message_id
    chat_id=query.message.chat_id
    file_path=tcl.file_path_va(path=query.data)
    if os.path.isfile(file_path):
        try:
            message=bot.send_document(chat_id=chat_id, document=open(file_path,'rb'))
            context.user_data["message_id"]=message.message_id
        except Exception as e:
            bot.send_message(chat_id=chat_id, text=f"{e}\nError Occured while sending the file")
            logging.error(str(e))
    else:
        bot.send_message(chat_id=chat_id, text="File Not Found")
    tcl.file_path_va_cl(path=query.data)
    subject(update,context)
    print("file down stop")


def button_press(update, context):
    print("button press start")
    query = update.callback_query
    user_details=sql.check_user_details(query.message.chat_id)
    print(query.data)
    path=f'branches/{user_details[1]}/{query.data}'
    if query.data =='register':
        print("c0 active")
        register(update,context)




    elif query.data in list(map(lambda x: x, [branch_var for branch_var in sorted(os.listdir("branches"))])):

        print("c1 active")

        print(query.data)

        branch(update, context)



    elif [query.data] in [[sub_var] for sub_var in sorted(os.listdir(f"branches/{user_details[1]}"))]:

        print("c2 active")

        subject(update, context)

    elif [query.data]in[[file_var] for file_var in sorted(os.listdir(tcl.file_path_va(path='')))]:

        print("c3 active!")

        file_download(update, context)

    else:
            print("c4 active")

            bot.answerCallbackQuery(chat_id=query.message.chat_id,text="Error!")
    print("button p end")
def main():
    updater = Updater(Token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CallbackQueryHandler(button_press))
    dp.add_handler(CommandHandler('start', start))
    logging.debug("Updater created")
    updater.start_polling()
    logging.debug("Started polling")
    updater.idle()
if __name__ == '__main__':
    main()
