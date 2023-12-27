from aiogram.fsm.state import StatesGroup, StatesGroupMeta,State


class OrderFood(StatesGroup):
    choosing_food_name = State()
    choosing_food_size = State()

available_food_names = ["Суши", "Спагетти", "Хачапури"]
available_food_sizes = ["Маленькую", "Среднюю", "Большую"]