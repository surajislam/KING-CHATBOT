import asyncio
import importlib

from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from nexichat import LOGGER, nexichat
from nexichat.modules import ALL_MODULES


async def anony_boot():
    try:
        await nexichat.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("nexichat.modules." + all_module)
        LOGGER.info(f"Successfully imported : {all_module}")

    # Set bot commands
    try:
        await nexichat.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Get the help menu"),
                BotCommand("ping", "Check if the bot is alive or dead"),
            ]
        )
        LOGGER.info("Bot commands set successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")

    LOGGER.info(f"@{nexichat.username} Started.")
    try:
        await nexichat.send_message(int(OWNER_ID), f"{nexichat.mention} has started")
    except Exception as ex:
        LOGGER.info(f"@{nexichat.first_name} Started, please start the bot from owner id.")
    
    await idle()


if __name__ == "__main__":
    asyncio.get
