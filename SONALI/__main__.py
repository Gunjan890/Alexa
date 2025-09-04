import asyncio
import importlib
from pyrogram import idle

import config
from SONALI import LOGGER, app, userbot
from SONALI.core.call import RAUSHAN
from SONALI.misc import sudo
from SONALI.plugins import ALL_MODULES
from SONALI.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# Import and start keep-alive server
from keep_alive import keep_alive


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(name).error(
            "ð’ð­ð«ð¢ð§ð  ð’ðžð¬ð¬ð¢ð¨ð§ ðð¨ð­ ð…ð¢ð¥ð¥ðžð, ðð¥ðžðšð¬ðž ð…ð¢ð¥ð¥ ð€ ðð²ð«ð¨ð ð«ðšð¦ V2 ð’ðžð¬ð¬ð¢ð¨ð§ðŸ¤¬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SONALI.plugins" + all_module)
    LOGGER("SONALI.plugins").info("ð€ð¥ð¥ ð…ðžðšð­ð®ð«ðžð¬ ð‹ð¨ðšððžð ððšð›ð²ðŸ¥³...")
    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()
    LOGGER("SONALI").info("â•”â•â•â•â•â•à®œÛ©ÛžÛ©à®œâ•â•â•â•â•—\n  â™¨ï¸ð— ð—”ð——ð—˜ ð—•ð—¬ ð—”ð—Ÿð—£ð—›ð—”â™¨ï¸\nâ•šâ•â•â•â•â•à®œÛ©ÛžÛ©à®œâ•â•â•â•â•")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SONALI").info("â•”â•â•â•â•â•à®œÛ©ÛžÛ©à®œâ•â•â•â•â•—\n  â™¨ï¸ð— ð—”ð——ð—˜ ð—•ð—¬ ð—”ð—Ÿð—£ð—›ð—”â™¨ï¸\nâ•šâ•â•â•â•â•à®œÛ©ÛžÛ©à®œâ•â•â•â•â•")


if __name__ == "__main__":
    keep_alive()  # Start the web server for Render
    asyncio.get_event_loop().run_until_complete(init())
