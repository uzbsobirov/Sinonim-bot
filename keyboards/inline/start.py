from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_group(bot_username):
    add_url = f"https://telegram.me/{bot_username}?startgroup=new"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👥 Guruhga qo'shish", url=add_url)
            ]
        ]
    )
