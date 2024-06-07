from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.models import Category, Book


def categories_btn(categories: list[Category]):
    ikb = InlineKeyboardBuilder() # noqa
    btns = [InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}") for category in categories] # noqa
    btns.append(InlineKeyboardButton(text="🔎 search", switch_inline_query_current_chat=''))  # noqa
    ikb.add(*btns)
    ikb.adjust(2, repeat=True)
    return ikb.as_markup()


def books_btn(books: list[Book]):
    ikb = InlineKeyboardBuilder() # noqa
    btns = [InlineKeyboardButton(text=book.title, callback_data=f"book_{book.id}") for book in books] # noqa
    btns.append(InlineKeyboardButton(text="🔎 search", switch_inline_query_current_chat=''))
    btns.append(InlineKeyboardButton(text="🔙 Back", callback_data='book_back'))
    ikb.add(*btns)
    ikb.adjust(2, repeat=True)
    return ikb.as_markup()