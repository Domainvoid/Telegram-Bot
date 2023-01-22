
'''    @staticmethod
    def subject_board():
        subject_keyboard = [[InlineKeyboardButton('Fundamentals of Computers', callback_data='sub_foc'),InlineKeyboardButton('C Programming',callback_data='sub_cPro')],[InlineKeyboardButton('Operating Systems',callback_data='sub_os'),InlineKeyboardButton('Multimedia Systems',callback_data='sub_MultiSys')],[InlineKeyboardButton('Understanding Organisational Behaviour',callback_data='sub_uob'),InlineKeyboardButton('Data and Database Management Systems',callback_data='sub_Ddbms')],[InlineKeyboardButton('Web-Based Application Development',callback_data='sub_wbad'),InlineKeyboardButton('Computer Lab and Practical Work',callback_data='sub_clpw')]]
        subjct_reply_markup = InlineKeyboardMarkup(subject_keyboard)
        return subjct_reply_markup

    @staticmethod
    def branch_board():
        branches_keyboard = [[InlineKeyboardButton("Bca", callback_data='Bca')]]
        branches_reply_markup = InlineKeyboardMarkup(branches_keyboard)
        return branches_reply_markup
    @staticmethod
    def option_board():
        option_keyboard = [[InlineKeyboardButton('Regiser Me!', callback_data='register')],[InlineKeyboardButton('Result!',callback_data='result')],[InlineKeyboardButton('Help?',callback_data="help")]]
        option_reply_markup = InlineKeyboardMarkup(option_keyboard)
        return option_reply_markup
    @staticmethod
    def chapter_board():
        chapter_keyboard = [[InlineKeyboardButton('chapter 1', callback_data='ch1')]]
        chapter_reply_markup = InlineKeyboardMarkup(chapter_keyboard)
        return chapter_reply_markup'''