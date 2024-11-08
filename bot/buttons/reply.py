from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.i18n import gettext as _


def main_button():
    design = [
        [
            KeyboardButton(text=_('📚 Books'))
        ],
        [
            KeyboardButton(text=_('🛒 My Orders'))
        ],
        [
            KeyboardButton(text=_('🌐 Our Net Work')),
            KeyboardButton(text=_('📞 Connect with Us'))
        ],
        [
            KeyboardButton(text=_('🇺🇿/🇺🇸 Language'))
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)