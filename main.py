import asyncio
import logging
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

from keyboards import builder
import qwest

clbck_dta=1

global_variable=0
vsis1=0
vsis2=0
vsis3=0
vsis4=0
class O(StatesGroup):
    state0 = State()
    state1 = State()
    state2= State()
    state3= State()
    state4= State()
    state5= State()
    state6= State()
    state7= State()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6176106214:AAGcWkXAC9j-bHa1QvtgYpfC_Om8is2U_EM")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message,state: FSMContext):
    builder = InlineKeyboardBuilder()
    global clbck_dta
    builder.add(types.InlineKeyboardButton(text="Начать",callback_data='s'+str(clbck_dta))) 
    await message.answer("Нажмите на кнопку, чтобы начать тест",reply_markup=builder.as_markup())
    await state.set_state(O.state0)
    clbck_dta+=int(1)

@dp.callback_query(F.data == "s1")
async def sist1(callback: types.CallbackQuery,state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Да",callback_data="ans_1"))
    builder.add(types.InlineKeyboardButton(text="Скорее да, чем нет",callback_data="ans_2"))      
    builder.add(types.InlineKeyboardButton(text="Не знаю",callback_data="ans_3"))      
    builder.add(types.InlineKeyboardButton(text="Скорее нет, чем да",callback_data="ans_4"))   
    builder.add(types.InlineKeyboardButton(text="Нет",callback_data="ans_5")) 
    builder.add(types.InlineKeyboardButton(text="Следующий",callback_data='s'+str(clbck_dta))) 
    builder.adjust(2)
    await callback.message.answer(qwest.sis1,reply_markup=builder.as_markup())
    await state.set_state(O.state1)
      

@dp.callback_query(F.data == "ans_1" , O.state1)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis1
    vsis1 += 2
    var1='s2'
    
    await callback.message.answer("1.баллы в категории"+str(vsis1))

    #Скрытие клавы - не вылазит след сообщение

    await callback.message.edit_reply_markup()


@dp.callback_query(F.data == "ans_2" , O.state1)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis1
    vsis1 += 1
    await callback.message.answer("1.баллы в категории"+str(vsis1))    
    

@dp.callback_query(F.data == "ans_4" ,O.state1)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis1
    vsis1 -= 1
    await callback.message.answer("1.баллы в категории"+str(vsis1))  
   

@dp.callback_query(F.data == "ans_5" ,O.state1)   
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis1
    vsis1 -= 2
    await callback.message.answer("1.баллы в категории"+str(vsis1))  
        
 

@dp.callback_query(F.data == "s2")
async def sist2(callback: types.CallbackQuery,state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Да",callback_data="ans_1"))
    builder.add(types.InlineKeyboardButton(text="Скорее да, чем нет",callback_data="ans_2"))      
    builder.add(types.InlineKeyboardButton(text="Не знаю",callback_data="ans_3"))      
    builder.add(types.InlineKeyboardButton(text="Скорее нет, чем да",callback_data="ans_4"))   
    builder.add(types.InlineKeyboardButton(text="Нет",callback_data="ans_5")) 
    builder.add(types.InlineKeyboardButton(text="Следующий",callback_data="s3")) 
    builder.adjust(2)
    await callback.message.answer(qwest.sis2,reply_markup=builder.as_markup())
    await state.set_state(O.state2)

@dp.callback_query(F.data == "ans_1" , O.state2)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis2
    vsis2 += 2
    await callback.message.answer("1.баллы в категории"+str(vsis2))

@dp.callback_query(F.data == "ans_2" , O.state2)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis2
    vsis2 += 1
    await callback.message.answer("1.баллы в категории"+str(vsis2))    

@dp.callback_query(F.data == "ans_4" ,O.state2)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis2
    vsis2 -= 1
    await callback.message.answer("1.баллы в категории"+str(vsis2))      


@dp.callback_query(F.data == "ans_5" ,O.state2)   
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis2
    vsis2 -= 2
    await callback.message.answer("1.баллы в категории"+str(vsis2))       

@dp.callback_query(F.data == "s3")
async def sist3(callback: types.CallbackQuery,state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Да",callback_data="ans_1"))
    builder.add(types.InlineKeyboardButton(text="Скорее да, чем нет",callback_data="ans_2"))      
    builder.add(types.InlineKeyboardButton(text="Не знаю",callback_data="ans_3"))      
    builder.add(types.InlineKeyboardButton(text="Скорее нет, чем да",callback_data="ans_4"))   
    builder.add(types.InlineKeyboardButton(text="Нет",callback_data="ans_5")) 
    builder.add(types.InlineKeyboardButton(text="Следующий",callback_data="s4")) 
    builder.adjust(2)
    await callback.message.answer(qwest.sis3,reply_markup=builder.as_markup())
    await state.set_state(O.state3)   

@dp.callback_query(F.data == "ans_1" , O.state3)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis3
    vsis3 += 2
    await callback.message.answer("1.баллы в категории"+str(vsis2))

@dp.callback_query(F.data == "ans_2" , O.state3)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis3
    vsis3 += 1
    await callback.message.answer("1.баллы в категории"+str(vsis2))    

@dp.callback_query(F.data == "ans_4" ,O.state3)     
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis3
    vsi3 -= 1
    await callback.message.answer("1.баллы в категории"+str(vsis2))      


@dp.callback_query(F.data == "ans_5" ,O.state3)   
async def otv_s1(callback: types.CallbackQuery, state: FSMContext):
    global vsis3
    vsis3 -= 2
    await callback.message.answer("1.баллы в категории"+str(vsis2))  
# @dp.callback_query(F.data == "s4")
# async def sist4(callback: types.CallbackQuery):
  
#     await callback.message.answer("4.Мысль выражаете четко и понятно",reply_markup=keyboards.builder)   

# @dp.callback_query(F.data == "s5")
# async def sist5(callback: types.CallbackQuery):
   
#     await callback.message.answer("5.Во всем должны соблюдаться четкие и понятные правила",reply_markup=keyboards.builder)       

# @dp.callback_query(F.data == "s6")
# async def sist6(callback: types.CallbackQuery):
    
#     await callback.message.answer("6.Вы реалист",reply_markup=keyboards.builder)       

# @dp.callback_query(F.data == "s7")
# async def sist7(callback: types.CallbackQuery):
  
#     await callback.message.answer("7.Мне нравится составлять планы и решать, что и кому делать.",reply_markup=keyboards.builder)       

# @dp.callback_query(F.data == "s8")
# async def sist8(callback: types.CallbackQuery):
   
#     await callback.message.answer("8.Важно иметь управляемые, четко контролируемые бизнес проекты ",reply_markup=keyboards.builder)    

# @dp.callback_query(F.data == "s9")
# async def sist9(callback: types.CallbackQuery):

#     await callback.message.answer("9.Решающие значение имеет точное распределение, и выполнение договоров между людьми",reply_markup=keyboards.builder)

# @dp.callback_query(F.data == "s10")
# async def sist10(callback: types.CallbackQuery):
#     await callback.message.answer("10.Если правила для Вас четко определены, то Вы можете легко управлять несколькими проектами",reply_markup=keyboards.builder)      

@dp.message(Command("var"))
async def cmd_var(message: types.Message):

    await message.answer("переменные"+str(vsis1)+str(vsis2)+str(vsis3))

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())     