from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
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
    new = State()
    last = State()


@router.message(Command(commands='start'))
async def start(message: Message):
    btn1 = KeyboardButton(text="Начать поиск!")
    keyboard = ReplyKeyboardMarkup(keyboard=[[btn1]])
    await message.answer("Привет!\nНажми на кнопку 'Начать поиск', чтобы начать меня использовать!",
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


@router.message(F.text == "Узнать награды актеров")
async def awards(message: Message, state: FSMContext):
    await state.set_state(NameFilm.new)
    await message.answer("Введите имя актера")


@router.message(NameFilm.new)
async def aw(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    a = get_actor(data['name'])
    await message.answer(a)
    await state.clear()


@router.message(F.text == "Получить ссылку на фильм")
async def link(message: Message, state: FSMContext):
    await state.set_state(NameFilm.last)
    await message.answer("Введите название фильма")


@router.message(NameFilm.last)
async def li(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    a = get_film(data)
    await message.answer(a)
    await state.clear()


if __name__ == "__main__":
    dp.run_polling(bot)
