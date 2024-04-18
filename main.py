import asyncio
import logging


from aiogram import Bot, Dispatcher, types
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
import stategroup
from aiogram.fsm.context import FSMContext


import keyboard
#from  stategroup import StepsForm

from database import prisma_client

from dotenv import dotenv_values

config = dotenv_values('.env')


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config['BOT_TOKEN'])
dp = Dispatcher()


class SourceBookForm(StatesGroup):
    title = State()
    description = State()

class BookForm(StatesGroup):
    #TODO book form and theme form states


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


@dp.message(Command('auth'))
async def auth(message: types.Message, bot: Bot):
    checked_user = await prisma_client.user.find_unique(
        where={
            'telegram_id': message.from_user.id
        }
    )

    if not checked_user:
        user = await prisma_client.user.create(
            data={
                'username': message.from_user.username,
                'telegram_id': message.from_user.id,
            }
        )

        if user:
            await message.answer('Вы успешно зарегистрировались!')
        else:
            await message.answer('Что-то пошло не так, обратитсь в поддержку бота или оппробуйте снова!')

    else:
        await message.answer(f'Вы уже зарегистрированы!\nUserInfo:\nusername={checked_user.username}\ntelegram_id={checked_user.telegram_id}')
@dp.message(Command('add_new_source_book'))
async def add_new_source_book(message: types.Message, bot: Bot):
    checked_user = await prisma_client.user.find_unique(
        where={
            'telegram_id': message.from_user.id
        }
    )

    if not checked_user or checked_user.role != 'ADMIN':
        await message.answer('У вас недостаточно прав для совершения данной операции!')
        return
    else:
        await message.answer('Пожалуйста, введите название желаемой коллекции!')


async def main():
    await prisma_client.connect()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


