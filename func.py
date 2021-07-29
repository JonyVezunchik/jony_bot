from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from random import randint
from const import *
def start(update,context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    top_button = [InlineKeyboardButton(text='Нажми меня')]
    mid_button = [InlineKeyboardButton(text='Нет.Нажми меня! (Скинуть контакт)', request_contact = True)]
    bot_button = [InlineKeyboardButton(text='Жмяк')]
    lang_button = [InlineKeyboardButton(text ='Русский', callback_data ='rus'), InlineKeyboardButton(text='O`zbek',callback_data='uzb')]
    context.bot.send_message(chat_id= user_id, text=MSG_LST[0].format(name),reply_markup=(ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup([top_button,mid_button,bot_button], resize_keyboard=0)))

def text_answer(update, context):
    user_id = update.message.chat_id
    text = update.message.text
    text = text.lower()
    if text =='Жмяк':
        context.bot.send_message(chat_id=user_id, text= 'Жмяк,жмяк')
    def rus(update, context):
        user_id = update.callback_query,from_user.id
        context.bot.send_message(chat_id=user_id, text='Выбран русский язык')
    def uzb(update, context):
        user_id = update.callback_query, from_user.id
        context.bot.send_message(chat_id=user_id, text='Выбран узбекский язык')
