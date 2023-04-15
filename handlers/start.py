from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import main_menu_keyboard


async def cmd_start(message: types.Message):
    user_fisrt_name = message.from_user.first_name
    await message.answer(f'Привет, {user_fisrt_name}!',
                         reply_markup=main_menu_keyboard)


def register_nandlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start,
                                CommandStart())
