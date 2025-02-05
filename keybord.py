from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pars_site.pars import *

brands = main()
brand_car_kb = InlineKeyboardMarkup(row_width=4)

for i in range(0, min(40, len(brands)), 4):
    row_buttons = [InlineKeyboardButton(text=brand, callback_data=brand[:64]) for brand in brands[i:i + 4]]
    brand_car_kb.add(*row_buttons)

from pars_site.mercedes.ms_benz_model_generations import *

model_ms_benz = models_generations()
model_ms_benz_kb = InlineKeyboardMarkup()
for model in model_ms_benz.keys():
    button = InlineKeyboardButton(text=model, callback_data=model)
    model_ms_benz_kb.add(button)

# generations = models_generations()
# generations_ms_benz_kb = InlineKeyboardMarkup()
# for generation in generations.values():
#     button = InlineKeyboardButton(text=generation, callback_data=generation)
#     generations_ms_benz_kb.add(*button)

