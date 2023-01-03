from aiogram import Dispatcher
from aiogram.types import Message, ContentType

from lexicon.lexicon_en import LEXICON_EN


async def process_start_command(message: Message):
    await message.answer(text=LEXICON_EN['/start'])

# async def process_help_command(message: Message):
#     await message.answer(text=LEXICON_EN['/help'])


async def process_any_text(message: Message):
    await message.answer(text=message.text)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    # dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_any_text,  content_types=ContentType.TEXT)
