from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import  types

builder = InlineKeyboardBuilder()
builder.add(types.InlineKeyboardButton(text="Да",callback_data="ans_1"))
builder.add(types.InlineKeyboardButton(text="Скорее да, чем нет",callback_data="ans_2"))      
builder.add(types.InlineKeyboardButton(text="Не знаю",callback_data="ans_3"))      
builder.add(types.InlineKeyboardButton(text="Скорее нет, чем да",callback_data="ans_4"))   
builder.add(types.InlineKeyboardButton(text="Нет",callback_data="ans_5")) 
builder.add(types.InlineKeyboardButton(text="Следующий",callback_data="s2")) 
builder.adjust(2)