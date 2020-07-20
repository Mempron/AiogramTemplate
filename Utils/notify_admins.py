import logging

from aiogram import Dispatcher

from Data.config import admin


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(admin, 'Бот Запущен')

    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(admin, 'Бот Выключен')

    except Exception as err:
        logging.exception(err)
