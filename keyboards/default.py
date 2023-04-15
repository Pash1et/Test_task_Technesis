from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Загрузить файл',
                             callback_data='upload_file'),
    ]
])
