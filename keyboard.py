from aiogram.types import(
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram import Bot, Dispatcher, types




main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Помощь', callback_data='help'),
            InlineKeyboardButton(text='Команды', callback_data='command'),
        ],
        [
            InlineKeyboardButton(text='Темы', callback_data='tema'),
            InlineKeyboardButton(text='Источник', callback_data="istochnik")
        ],
        [
            InlineKeyboardButton(text="Команды", callback_data="command")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

pravila_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Орфография',callback_data='orfografia'),
            InlineKeyboardButton(text='Пунктуация', callback_data='pynktyacia')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
istochnik_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Учебник по русскому', callback_data='istochnik')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
orfogra_fia = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text='Лесика', callback_data='leksika'),
            InlineKeyboardButton(text='Орфография и приставки', callback_data='orfografia')
        ],
        [
            InlineKeyboardButton(text='Имя существительное', callback_data='syh'),
            InlineKeyboardButton(text='Имя прилагательное', callback_data='prilagatelnoe')
        ],
        [
            InlineKeyboardButton(text='Имя числительное',callback_data='chisl'),
            InlineKeyboardButton(text='Глагол', callback_data='glagol')
        ],
        [
            InlineKeyboardButton(text='Местоимение', callback_data='mest'),
            InlineKeyboardButton(text='Причастие и деепричастие', callback_data='prich')
        ],
        [
            InlineKeyboardButton(text='Наречие' ,callback_data='nar')
        ]
    ],

    resize_keyboard=True,
    one_time_keyboard=True
)
pynktyaci_a = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Знаки законченности', callback_data='tochka'),
            InlineKeyboardButton(text='Знаки незаконченности', callback_data='zapatie')
        ],
        [
            InlineKeyboardButton(text='Двойные знаки', callback_data='two'),
            InlineKeyboardButton(text='Простое предложение', callback_data='prost')
        ],
        [
            InlineKeyboardButton(text='Пунктуация при обращении', callback_data='obrsh'),
            InlineKeyboardButton(text='Сравнительные обороты', callback_data='')
        ],
        [
            InlineKeyboardButton(text='Прямая речь', callback_data='pram'),
            InlineKeyboardButton(text='Цитирование', callback_data='citirov')
        ],
        [
            InlineKeyboardButton(text='ССП', callback_data='ssp'),
            InlineKeyboardButton(text='СПП', callback_data='spp')
        ],
        [
            InlineKeyboardButton(text='СБП', callback_data='sbp'),
            InlineKeyboardButton(text='Виды синтаксической связи', callback_data='sintaks')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
