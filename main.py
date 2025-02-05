from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from keybord import *

API = # api
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Напишите команду для просмотра списка автомобилей /carlist')


@dp.message_handler(commands=['carlist'])
async def car_list(message):
    await message.answer('Выберите марку автомобиля:', reply_markup=brand_car_kb)


@dp.callback_query_handler(lambda callback_query: True)
async def chose_mercedes_model(call):
    select_model = call.data
    if select_model == 'Mercedes-Benz':
        await call.message.answer("Выберите модель автомобиля:", reply_markup=model_ms_benz_kb)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data in model_ms_benz.keys())
async def chose_generations_model(call):
    select_model = call.data
    generations = model_ms_benz[select_model]
    generations_ms_benz_kb = InlineKeyboardMarkup()

    for generation in generations:
        button = InlineKeyboardButton(text=generation, callback_data=generation)
        generations_ms_benz_kb.add(*button)

    await call.message.answer("Выберите поколение автомобиля:", reply_markup=generations_ms_benz_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
