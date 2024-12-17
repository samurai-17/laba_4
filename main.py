"""
описание фильма и узнать рейтинг фильма
получить инфо по актерам
получить ссылку на фильм
?фильмы по жанрам?
"""

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

import films_funk
from config import load_config
from films_funk import *
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


config = load_config('.env')
bot_token = config.token  # Сохраняем токен в переменную bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()
router = Router()
dp.include_router(router)


class NameFilm(StatesGroup):
    name = State()

@router.message(Command(commands='start'))
async def start(message: Message):
    btn1 = KeyboardButton(text="Начать поиск!")
    keyboard = ReplyKeyboardMarkup(keyboard=[[btn1]])
    await message.answer("Привет!\nНажми на кнопку 'Начать поиск', чтобы начать меня абьюзить!",
                         reply_markup=keyboard)


@router.message(F.text == "Начать поиск!")
async def search(message: Message):
    btn1 = KeyboardButton(text="Получить описание и рейтинг")
    btn2 = KeyboardButton(text="Узнать награды актеров")
    btn3 = KeyboardButton(text="Получить ссылку на фильм")
    keyboard = ReplyKeyboardMarkup(keyboard=[[btn1, btn2, btn3]])
    await message.answer("Выбери действие!",
                         reply_markup=keyboard)


@router.message(F.text == "Получить описание и рейтинг")
async def describe(message: Message, state: FSMContext):
    await state.set_state(NameFilm.name)
    await message.answer("Введите название фильма")


@router.message(NameFilm.name)
async def desc(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    des, kp = get_describe(data['name'])
    await message.answer(f"Описание: {des}\nРейтинг кинопоиска: {kp}")
    await state.clear()


if __name__ == "__main__":
    dp.run_polling(bot)
