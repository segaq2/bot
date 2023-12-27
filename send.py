import asyncio
import logging
import datetime
import sqlite3

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.state import StatesGroup, StatesGroupMeta,State

clbck_dta=1
current_date=5
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6176106214:AAGcWkXAC9j-bHa1QvtgYpfC_Om8is2U_EM")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message,state: FSMContext):
    await message.answer("Напиши кодовое слово")

#запись в бд после получения ссылки в формате юсернейм-дата, потом отсчет 2 суток и напомининие
@dp.message(F.text == "первый")
async def sist1(message: types.Message,state: FSMContext):
    await message.answer("https://ya.ru/")

@dp.message(F.text == "Первый")
async def sist1(message: types.Message,state: FSMContext):
    await message.answer("https://ya.ru/")

@dp.message(F.text == "второй")
async def sist1(message: types.Message,state: FSMContext):
    await message.answer("https://www.google.com/")

@dp.message(F.text == "Второй")
async def sist1(message: types.Message,state: FSMContext):
   await message.answer("https://www.google.com/")

#текущяя дата     
#    global current_date
 #   current_date = datetime.date.today().isoformat()

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())         