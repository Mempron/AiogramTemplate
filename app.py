from loader import bot, storage


async def on_startup(dp):
    # import Filters
    import Middlewares
    # Filters.setup(dp)
    Middlewares.setup(dp)

    from Utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


async def on_shutdown(dp):
    from Utils.notify_admins import on_shutdown_notify
    await on_shutdown_notify(dp)
    await bot.close()
    await storage.close()

if __name__ == '__main__':
    from aiogram import executor
    from Handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)