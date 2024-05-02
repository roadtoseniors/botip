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
        elif call.data == 'tochka':
        filee_path = "photobd/tochka.jpg"
        filee_path2 = "photobd/tochka2.jpg"
        filee_path3 = "photobd/tochka3.jpg"
        photo1 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path), caption="")
        photo2 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path2))
        photo3 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path3))
        media = [photo1, photo2, photo3]
        await call.bot.send_media_group(call.message.chat.id, media)
    elif call.data == 'double':
        await call.bot.send_photo(call.message.chat.id,
                                  photo=types.FSInputFile(
                                      path="photobd/double.jpg"
                                  ))
    elif call.data == 'tire':
        await call.bot.send_photo(call.message.chat.id,
                                  photo=types.FSInputFile(
                                      path='photobd/tire.jpg'
                                  ))
    elif call.data == 'prost':
        file_path1 = 'photobd/prost.jpg'
        file_path2 = 'photobd/prost2.jpg'
        photo1 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path1), caption='')
        photo2 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path2))
        media = [photo1, photo2]
        await call.bot.send_media_group(call.message.chat.id, media)
        elif call.data == "opred":
        file_path1 = 'photobd/opred.jpg'
        file_path2 = 'photobd/opred2.jpg'
        file_path3 = 'photobd/opred3.jpg'
        file_path4 = 'photobd/opred4.jpg'
        photo1 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path1), caption='')
        photo2 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path2))
        photo3 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path3))
        photo4 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path4))
        media = [photo1, photo2, photo3, photo4]
        await call.bot.send_media_group(call.sage.chat.id, media)
    elif call.data == 'obsto':
        await call.bot.send_photo(call.message.chat.id,
                                  photo=types.FSInputFile(
                                      path='photobd/obsto.jpg'
                                  ))
    elif call.data == "vvod":
        file_path1 = 'photobd/vvod.jpg'
        file_path2 = 'photobd/vvod2.jpg'
        file_path3 = 'photobd/vvod3.jpg'
        file_path4 = 'photobd/vvod4.jpg'
        file_path5 = 'photobd/vvod5.jpg'
        photo1 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path1), caption='')
        photo2 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path2))
        photo3 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path3))
        photo4 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path4))
        photo5 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path5))
        media = [photo1, photo2, photo3, photo4, photo5]
        await call.bot.send_media_group(call.message.chat.id, media)
        elif call.data == 'obrash':
        file_path1 = 'photobd/obrash.jpg'
        file_path2 = 'photobd/obrash2.jpg'
        file_path3 = 'photobd/obrash3.jpg'
        file_path4 = 'photobd/obrash4.jpg'
        photo1 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path1), caption='')
        photo2 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path2))
        photo3 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path3))
        photo4 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path4))
        media = [photo1, photo2, photo3, photo4]
        await call.bot.send_media_group(call.message.chat.id, media)
    elif call.data == 'sbp':
        filee_path = "photobd/sbp.jpg"
        filee_path2 = "photobd/sbp2.jpg"
        filee_path3 = "photobd/sbp3.jpg"
        photo1 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path), caption="")
        photo2 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path2))
        photo3 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path3))
        media = [photo1, photo2, photo3]
        await call.bot.send_media_group(call.message.chat.id, media)
    elif call.data == 'sintaks':
        await call.bot.send_photo(call.message.chat.id,
                                  photo=types.FSInputFile(
                                      path='photobd/sintaks.jpg'
                                  ))
        elif call.data == 'spp':
        filee_path = "photobd/spp.jpg"
        filee_path2 = "photobd/spp2.jpg"
        filee_path3 = "photobd/spp3.jpg"
        photo1 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path), caption="")
        photo2 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path2))
        photo3 = InputMediaPhoto(type="photo", media=types.FSInputFile(path=filee_path3))
        media = [photo1, photo2, photo3]
        await call.bot.send_media_group(call.message.chat.id, media)
    elif call.data == 'sravn':
        file_path1 = 'photobd/sravn.jpg'
        file_path2 = 'photobd/sravn2.jpg'
        photo1 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path1), caption='')
        photo2 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path2))
        media = [photo1, photo2]
        await call.bot.send_media_group(call.message.chat.id, media)
    elif call.data == 'ssp':
        file_path1 = 'photobd/ssp.jpg'
        file_path2 = 'photobd/ssp2.jpg'
        photo1 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path1), caption='')
        photo2 = InputMediaPhoto(type='photo', media=types.FSInputFile(path=file_path2))
        media = [photo1, photo2]
        await call.bot.send_media_group(call.message.chat.id, media)


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


