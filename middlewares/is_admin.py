from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message, Update


class IsAdmin(BaseMiddleware):
    def __init__(self, user_id):
        self.user_id = user_id
        super(IsAdmin, self).__init__()

    async def __call__(self, handler, event: Update, data):
        print(event)

