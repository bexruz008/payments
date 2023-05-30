from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, Message

from payment_bot.data.config import ADMINS
from payment_bot.data.products import lavash_food, FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING, python_kurs, \
    lavash_food2
from payment_bot.keyboards.inline.product_keyboard import build_keyboard
from payment_bot.loader import dp, bot


@dp.message_handler(Text(equals="Python"))
async def show_invoices(message: types.Message):
    caption = "<b>Python dasturlash tili</b> online.\n\n"
    caption += "9 oyda junior dasturchi bo'ling.\n\n"
    caption += "Kurs tarkibi:\n"
    caption += "✅ Python Dasturlash Asoslar (4 hafta)\n"
    caption += "✅ OOP tamoyillari (4 hafta)\n"
    caption += "✅ Telegram bot (4 hafta)\n"
    caption += "✅ Database, malumotlar ombori (4 hafta)\n"
    caption += "✅ Frameworklar (8 hafta)\n"
    caption += "Narxi: <b>4.5mln so'm</b>"

    await message.answer_photo(photo="https://media.licdn.com/dms/image/C4D03AQEI43jKPEHGww/profile-displayphoto-shrink_800_800/0/1661104443533?e=2147483647&v=beta&t=hIBmeXdvyspJNTYahA7B330STgKC99lTEVZkPCBea_s",
                         caption=caption, reply_markup=build_keyboard("python"))


@dp.message_handler(Text(equals="Lavash"))
async def show_invoices(message: types.Message):
    caption = "<b>Lavash mahsuloti</b> online.\n\n"
    caption += "Mister kafeni lavashi.\n\n"
    caption += "Zo'r lavash:\n"
    caption += "Narxi: <b>23.000 so'm</b>"

    await message.answer_photo(photo="https://pasta.uz/upload/products/OL%20x%20Pasta%20Pishloqli%20lavash.jpg",
                         caption=caption, reply_markup=build_keyboard("lavash"))



@dp.message_handler(Text(equals="Tandir lavash"))
async def show_invoices(message: types.Message):
    caption = "<b>Lavash mahsuloti</b> online.\n\n"
    caption += "Mister kafeni lavashi.\n\n"
    caption += "Zo'r lavash:\n"
    caption += "Narxi: <b>30.000 so'm</b>"

    await message.answer_photo(photo="https://www.restoran-shafran.uz/image/cache/catalog/product/lavash-v-tandire-i-s-sirom-1-750x500.jpg",
                         caption=caption, reply_markup=build_keyboard("Tandir lavash"))


@dp.message_handler(Text(equals="Mahsulotlar"))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_kurs.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **lavash_food.generate_invoice(),
                           payload="123457")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **lavash_food2.generate_invoice(),
                           payload="1234567")


@dp.callback_query_handler(text="product:python")
async def book_invoice(callback: CallbackQuery):
    await bot.send_invoice(chat_id=callback.from_user.id,
                           **python_kurs.generate_invoice(),
                           payload="payload:python")
    await callback.answer()


@dp.callback_query_handler(text="product:lavash")
async def praktikum_invoice(callback: CallbackQuery):
    await bot.send_invoice(chat_id=callback.from_user.id,
                           **lavash_food.generate_invoice(),
                           payload="payload:lavash")
    await callback.answer()


@dp.callback_query_handler(text="product:Tandir lavash")
async def tandir_lavash(callback: CallbackQuery):
    await bot.send_invoice(chat_id=callback.from_user.id,
                           **lavash_food2.generate_invoice(),
                           payload="payload:Tandir lavash")
    await callback.answer()

@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    # elif query.shipping_address.city.lower() == "karshi":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    # elif query.shipping_address.city.lower() != "karshi":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        error_message="Boshqa shaharlarga yetkazib bera olmaymiz",
                                        ok=False)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")