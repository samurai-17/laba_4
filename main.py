from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, BotCommand, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from config import load_config


config = load_config('.env')
bot_token = config.token  # Сохраняем токен в переменную bot_token

bot = Bot(token=bot_token)
dp = Dispatcher()

if __name__ == "__main__":
    dp.run_polling(bot)