from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def Menyu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Python")
    button2 = KeyboardButton(text="Lavash")
    button4 = KeyboardButton(text="Tandir lavash")
    button3 = KeyboardButton(text="Mahsulotlar")
    rkm.add(button, button2, button3, button4)
    return rkm