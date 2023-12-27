import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.state import StatesGroup, StatesGroupMeta,State

logging.basicConfig(level=logging.INFO)

class UserState(StatesGroup):
    qs1=State()
    qs2=State()
    qs3=State()
    qs4=State()


bot = Bot(token="6176106214:AAGcWkXAC9j-bHa1QvtgYpfC_Om8is2U_EM")
dp = Dispatcher()

# Словарь для отслеживания состояний кнопок
button_states = {}
global_variable = 0

# #Обработка проверки по пересланному callback_data кнопки
# @dp.callback_query(F.data=="ans_1")
# async def process_callback_button(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     button_id = callback_query.data

#     # Если кнопка уже была нажата, игнорируем
#     if button_states.get(user_id, {}).get(button_id):
#         await bot.answer_callback_query(callback_query.id, text="Вы уже нажали эту кнопку", show_alert=True)
#     else:
#         # Обработка действий при нажатии кнопки
#         await bot.answer_callback_query(callback_query.id, text=f"Вы нажали кнопку {button_id}")

#         # Устанавливаем состояние кнопки в True, чтобы запретить повторное нажатие
#         button_states.setdefault(user_id, {})[button_id] = True




@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Начать",callback_data="s1")) 
    await message.answer("Нажмите на кнопку, чтобы начать тест",reply_markup=builder.as_markup())
    await UserState.qs1.set()



@dp.message(State=UserState.qs1)
async def sist1(message: types.Message, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Да",callback_data="ans_1"))
    builder.add(types.InlineKeyboardButton(text="Скорее да, чем нет",callback_data="ans_2"))      
    builder.add(types.InlineKeyboardButton(text="Не знаю",callback_data="ans_3"))      
    builder.add(types.InlineKeyboardButton(text="Скорее нет, чем да",callback_data="ans_4"))   
    builder.add(types.InlineKeyboardButton(text="Нет",callback_data="ans_5")) 
    builder.add(types.InlineKeyboardButton(text="Следующий",callback_data="s2")) 
    builder.adjust(2)
    global global_variable
    global_variable += 1
    await message.answer("Введите своё имя",reply_markup=builder.as_markup())
    await UserState.qs2.set()

# @dp.message(State=UserState.qs1)
# async def 


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  