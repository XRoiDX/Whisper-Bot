from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

I am the Master of Whisperers (like Varys in Game of Thrones).

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

To see how to use me press 'How to Use' below.

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@WhisperStarkBot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
╭╾ꕀ╾ꕀ╾ꕀ╾ꕀ╾ꕀ╾ꕀ╾ꕀ╾╯
╰╮ 
   ╳ 𝑴𝒀 𝑵𝑨𝑴𝑬 :- 𝑊ℎ𝑖𝑧𝑝𝑒𝑟 𝐵𝑜𝑡
╭╯
╳   𝑽𝑬𝑹𝑰𝑺𝑰𝑶𝑵 :- 3.9.6
╰╮
   ╳  𝑭𝑹𝑨𝑴𝑬𝑾𝑶𝑹𝑲 :- 𝑃𝑦𝑟𝑜𝑔𝑟𝑎𝑚
╭╯
╰═╍═╍═╍═╍═╍╤╍‌ ‌═‌ ‌╍‌ ‌═‌ ‌╍‌ ‌═‌ ‌╮
    """
