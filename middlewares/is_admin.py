from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message, Update


class IsAdmin(BaseMiddleware):
    def __init__(self):
        super(IsAdmin, self).__init__()

    async def __call__(self, handler, event: Message, data):
        print(event.from_user.id)

