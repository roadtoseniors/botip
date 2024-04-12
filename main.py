import asyncio
import logging


from aiogram import Bot, Dispatcher, types
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
import stategroup
from aiogram.fsm.context import FSMContext


import keyboard
#from  stategroup import StepsForm


logging.basicConfig(level=logging.INFO)
bot = Bot(token='6961486369:AAF14quNlNE8xurAd243y1H6qUQBFQfMc3g')
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text='Привет это справочник по русскому для студентов КИПФИН. Здесь собраны все изучаемые темы'
                         ' на первом курсе колледжа',reply_markup=keyboard.main_kb)

@dp.message(Command('command'))
async def command(message: types.Message):
    await message.answer(text='Список команд бота:\n'
                              '/start-сам запуск бота\n'
                              '/help-для найденных ошибок\n'
                              '/istochnik-учебник, который всегда под рукой\n'
                              '/tema-все собранные темы для 1 курса\n'
                              '/orfografia-все темы раздела орфография\n'
                              '/pynktyacia-все темы раздела пунктуация\n')

@dp.message(Command('help'))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Если вы нашли ошибку в каком-либо разделе, то передайте её сюда, мы все исправим.")
    await state.set_state(stategroup.HelpForm.Text)

@dp.message(Command('tema'))
async def tem_a(message: types.Message):
    await message.answer(text="Выберете раздел, который вам нужен", reply_markup=keyboard.pravila_kb)


@dp.callback_query()
async def cmd_callback(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    if call.data == 'help':
        await call.message.answer("Если вы нашли ошибку в каком-либо разделе, то передайте её сюда, мы все исправим.")
        await state.set_state(stategroup.HelpForm.Text)
    elif call.data == 'command':
        await call.message.answer(text='Список команд бота:\n'
                                       '/start-сам запуск бота\n'
                                       '/help-для найденных ошибок\n'
                                       '/istochnik-учебник, который всегда под рукой\n'
                                       '/tema-все собранные темы для 1 курса', reply_markup=keyboard.main_kb)
    elif call.data == 'istochnik':
        await call.message.answer(text="https://clck.ru/39fv4H")
    elif call.data == 'orfografia':
        await call.message.answer(text='Выберете тему орфографии:', reply_markup=keyboard.orfogra_fia)
    elif call.data == 'pynktyac':
        await call.message.answer(text='Выберете тему пунктуации:', reply_markup=keyboard.pynktyac_ia)
    elif call.data == 'tema':
        await call.message.answer(text="Выберете раздел, который вам нужен", reply_markup=keyboard.pravila_kb)


@dp.message(Command("istochnik"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    # builder = InlineKeyboardBuilder()
    # builder.row(types.InlineKeyboardButton(
    #     text="Учебник по русскому", url='https://clck.ru/39fv4H')
    # )
    await message.answer(
        "Источник, где можно удостовериться в правильности информации",
        reply_markup=keyboard.istochnik_kb
    )



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


