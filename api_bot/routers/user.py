from aiogram import Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from api_bot.utils.api import get_dog_url, get_cat_url

user_router = Router()

@user_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text='Добро пожаловать в API бота.\nВ нашем боте по разным команадам '
                                'можно обращаться к разным API сервисам.\n\n<b>Напишите команду /api для теста</b>')

@user_router.message(Command('dog'))
async def dog_image(message: Message, bot: Bot):
    dog_url = await get_dog_url()

    await bot.send_photo(chat_id=message.chat.id, photo=dog_url)

@user_router.message(Command('cat'))
async def cat_image(message: Message, bot: Bot):
    cat_url = await get_cat_url()

    await bot.send_photo(chat_id=message.chat.id, photo=cat_url)