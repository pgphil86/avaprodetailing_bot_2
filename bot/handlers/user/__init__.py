from aiogram import Router

from . import start

user_router = Router(name=__name__)
user_router.include_routers(start.router)