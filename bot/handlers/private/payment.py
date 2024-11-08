from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, LabeledPrice
from aiogram.utils.i18n import gettext as _

from utils.conf import Config as conf

order_router = Router()


@order_router.message(Command('invoice'))
async def invoice(message: Message):
    prices = [
        LabeledPrice(label='Iphone 15 pro', amount=1_000 * 1 * 100),
        LabeledPrice(label='Iphone 14 pro', amount=800 * 1 * 100)
    ]
    await message.answer_invoice(_('Product'), "Jami 3product order qilindi", '1',
                                 conf.bot.PAYMENT_CLICK_TOKEN,currency="UZS", prices=prices) # noqa

"""
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ixlos23/FactorBookbot.git
git push -u origin main
"""