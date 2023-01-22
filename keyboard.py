from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os


def create_keyboard(data):
    chapter_keyboard = [[InlineKeyboardButton(chapter, callback_data=chapter)] for chapter in sorted(os.listdir(data))]
    chapter_reply_markup = InlineKeyboardMarkup(chapter_keyboard)
    return chapter_reply_markup
def option_board():
    option_keyboard = [[InlineKeyboardButton('Regiser Me!', callback_data='register')],
                       [InlineKeyboardButton('Result!', callback_data='result')],
                       [InlineKeyboardButton('Help?', callback_data="help")]]
    option_reply_markup = InlineKeyboardMarkup(option_keyboard)
    return option_reply_markup
def directory():
    directory_list = [[directory_list] for directory_list in sorted(os.listdir("branches/"))]
    return directory_list
def subject(path):
    subject_list=[[directory_list]for directory_list in sorted(os.listdir(f"branches/{path}"))]
    return subject_list
def file_list(path):
    file_list=[[file_list]for file_list in sorted(os.listdir(f"branches/bca/maths/{path}"))]
    return file_list