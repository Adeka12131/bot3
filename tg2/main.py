from config import *
from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import InputFile

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    await dp.bot.send_message(chat_id=OWNER_ID, text='Здравствуйте, чтобы продолжить и начать, нажмите /start')

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_quest3 = types.KeyboardButton('gold')
tg = types.KeyboardButton('Наши отзывы')
bust = types.KeyboardButton('Буст')
main_keyboard.row(b_quest3).add(tg).add(bust)

back_kb = types.InlineKeyboardMarkup()
back1 = types.InlineKeyboardButton(text="Вернуться назад",callback_data="back")
back_kb.add(back1)

question1_kb = types.InlineKeyboardMarkup()
question1 = types.InlineKeyboardButton(text="100 голды",callback_data="100 голды")
question3 = types.InlineKeyboardButton(text="300 голды",callback_data="300 голды")
question4 = types.InlineKeyboardButton(text="500 голды",callback_data="500 голды")
question6 = types.InlineKeyboardButton(text="1000 голды",callback_data="1000 голды")
question8 = types.InlineKeyboardButton(text="3000 голды",callback_data="3000 голды")
question1_kb.add(question1,question3).add(question4,question6).add(question8)

tg1_kb = types.InlineKeyboardMarkup()
tg1 = types.InlineKeyboardButton(text="Наши отзывы",url = "https://t.me/kosti")
tg1_kb.add(tg1)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    photo_path = (r"C:\Users\adeka\OneDrive\Рабочий стол\tg2\msg6748020683-3421.jpg")
    await bot.send_photo(message.chat.id, InputFile(photo_path), caption='''Приветствуем, это официальный бот, где вы можете приобрести голду,  скины на оружия или аккаунты для игры Standoff.
Наши цены ниже рыночных, что является нашим преимуществом.''', reply_markup=main_keyboard)
    
@dp.callback_query_handler(lambda callback_query: True)
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == "100 голды":
        await bot.send_message(callback_query.from_user.id, '''
100 голды - 100 руб
8383838 - карта
при оплате,скидывайте чек сюда @paff''')
    elif callback_query.data == "300 голды":
        await bot.send_message(callback_query.from_user.id,'''
300 голды - 300 руб
8383838 - карта
при оплате,скидывайте чек сюда @paff''')
    elif callback_query.data == "500 голды":
        await bot.send_message(callback_query.from_user.id,'''
500 голды - 500 руб
8383838 - карта
при оплате,скидывайте чек сюда @paff''')
    elif callback_query.data == "1000 голды":
        await bot.send_message(callback_query.from_user.id,'''
1000 голды - 1000 руб
8383838 - карта
при оплате,скидывайте чек сюда @paff''')
    elif callback_query.data == "3000 голды":
        await bot.send_message(callback_query.from_user.id,'''
3000 голды - 3000 руб
8383838 - карта
при оплате,скидывайте чек сюда @paff''')


@dp.message_handler()
async def main_message(message: types.Message):
    if message.text == 'gold':
        await message.answer('Наша команда продает голду по цене, которая ниже, чем в Standoff:', reply_markup=question1_kb)
    elif message.text == 'Наши отзывы':
        await message.answer('Канал с нашими отзывами',reply_markup=tg1_kb)
    elif message.text == 'Буст':
        await message.answer('''Выберите интересующий Вас вариант:
Буст до Голда 1 - 200р
Буст до Феникса - 400р 
Буст до Рейнджера - 500р

92929293 - карта
чек скидывайте сюда @paff1''')
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)