'''
Main project file. Entry point.
'''

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers.user_handlers import register_user_handlers


__version__ = "{{ cookiecutter.version }}"

# Initialize logger
logger = logging.getLogger(__name__)


# Registering all handlers
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)


# Function to configure and launch bot
async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Print in console about starting bot
    logger.info('Starting bot...')

    # Getting all config into variable
    config: Config = load_config(r'.\.env')

    # Initializing bot and dispatcher
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot=bot)

    # Start polling
    try:
        # Uncomment if want skip all updates from bot.
        #dp.skip_updates()
        await dp.start_polling()
    except:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot has been stopped!')
