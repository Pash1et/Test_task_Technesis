import os

import requests
import pandas as pd
from aiogram import Dispatcher, types
from lxml import html

from database import models
from database.database import SessionLocal
from loader import bot


async def upload_file(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,
                           "Пришли один файл в формате Excel")
    await callback_query.answer()


async def handle_file(message: types.Message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    file = await bot.get_file(file_id)
    file_path = file.file_path

    await message.answer(f'Файл {file_name} загружен')

    file_name = os.path.join('data', file_name)
    with open(f'{file_name}', 'wb') as file:
        downloaded_file = await bot.download_file(file_path)
        file.write(downloaded_file.getvalue())
    data = pd.read_excel(file_name, names=None)
    for _, row in data.iterrows():

        response = requests.get(row["url"])
        parsed_page = html.fromstring(response.content)
        xpath_price = row["xpath"]
        price = parsed_page.xpath(xpath_price)[0].text_content()

        await message.answer(f'Title - {row["title"]}\n'
                             f'Url - {row["url"]}\n'
                             f'Xpath - {row["xpath"]}\n'
                             f'Price - {price}')

        db = SessionLocal()
        zuzublik = models.Zuzublik(
            title=row['title'],
            url=row['url'],
            xpath=row['xpath'],
        )

        db.add(zuzublik)
        db.commit()
        db.refresh(zuzublik)
        db.close()


def register_nandlers_start(dp: Dispatcher):
    dp.register_callback_query_handler(upload_file,
                                       text='upload_file')
    dp.register_message_handler(handle_file,
                                content_types=types.ContentTypes.DOCUMENT)
