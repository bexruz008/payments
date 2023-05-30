from aiogram import types
from aiogram.types import LabeledPrice

from payment_bot.utils.misc.product import Product

python_kurs = Product(
    title="Python dasturlash tili",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Python',
            amount=50000000 # 500 000.00
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-10000000
        ),
    ],
    start_parameter="create_invoice_python",
    photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW2aXXMTe5oAnph3e-v-D2xv52-pZEAa5SaqQZDwm7DHfoRdwapRcONV0uKNvDUZIKAiI&usqp=CAU",
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)


lavash_food = Product(
    title="Lavash",
    description="Lavashga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Lavash',
            amount=2300000,
        ),
        LabeledPrice(
            label='Yetkazib berish (2 soat)',
            amount=1000000,
        ),
    ],
    start_parameter="create_invoice_lavash",
    photo_url='https://pasta.uz/upload/products/OL%20x%20Pasta%20Pishloqli%20lavash.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (2 soat)",
    prices=[
        LabeledPrice(
            'Ketchup va mayanez', 300000),
        LabeledPrice(
            '2 soatda yetkazish', 1000000),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Super dostavka (yarim soat)',
    prices=[
        LabeledPrice(
            'yarim soatda yetkazish', 2000000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Evosdan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -1000000)
                                       ])



lavash_food2 = Product(
    title="Lavash",
    description="Tandir Lavashga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Lavash',
            amount=30000000,
        ),
        LabeledPrice(
            label='Yetkazib berish (2 soat)',
            amount=1000000,
        ),
    ],
    start_parameter="create_invoice_lavash",
    photo_url='https://www.restoran-shafran.uz/image/cache/catalog/product/lavash-v-tandire-i-s-sirom-1-750x500.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)