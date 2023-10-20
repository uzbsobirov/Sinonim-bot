from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMINS
from utils.extra_datas import make_title
from keyboards.inline.start import add_group

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    get_bot = await bot.get_me()
    bot_username = get_bot.username
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    user = None

    try:
        user = await db.add_user(user_id=user_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    if user:
        count = await db.count_users()
        msg = (f"[{make_title(user['full_name'])}](tg://user?id={user['user_id']}) bazaga qo'shildi\.\nBazada {count} ta foydalanuvchi bor\.")
    else:
        msg = f"[{make_title(full_name)}](tg://user?id={user_id}) bazaga oldin qo'shilgan"
    for admin in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin,
                text=msg,
                parse_mode=ParseMode.MARKDOWN_V2
            )
        except Exception as error:
            logger.info(f"Data did not send to admin: {admin}. Error: {error}")
    await message.answer("<b>Bu bot guruhlarda so'z o'yini o'ynash uchun ishlatiladi.</b>",
                         reply_markup=add_group(bot_username))
