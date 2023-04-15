from aiogram import executor

from loader import dp
from utils.default_bot_command import set_default_commands


async def on_startup(dp):
    await set_default_commands(dp)


if __name__ == '__main__':
    from handlers import start, upload_file

    start.register_nandlers_start(dp)
    upload_file.register_nandlers_start(dp)

    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
