from aiogram import types




# Echo bot
from payment_bot.loader import dp


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
