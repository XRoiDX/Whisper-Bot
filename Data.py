from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

**I am the Master of Whisperers (like Varys in Game of Thrones)**.

**You can use me to send whispers to your friend in groups and channels (even if I'm not there)**.
**Only that friend and you will be able to read the message even though others are in same group**. 

`To see how to use me press 'How to Use' below.`

𝑩𝒚 :- 𝑿𝒓𝒐𝒊𝑫 𝑩𝒐𝒕𝒁
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 𝑺𝒆𝒏𝒅 𝑨 𝑾𝒉𝒊𝒔𝒑𝒆𝒓 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 𝑹𝒆𝒕𝒖𝒓𝒏 𝑯𝒐𝒎𝒆 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 𝑺𝒆𝒏𝒅 𝑨 𝑾𝒉𝒊𝒔𝒑𝒆𝒓 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("𝑯𝒐𝒘 𝑻𝒐 𝑼𝒔𝒆 ❔", callback_data="help"),
            InlineKeyboardButton("🎪 𝑨𝒃𝒐𝒖𝒕 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ 𝑩𝒐𝒕𝒛 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 ♥", url="https://t.me/XRoid_BotZ")],
        [InlineKeyboardButton("🎨 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 🎨", url="https://t.me/XRoid_Support")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@thisbotusername your_message friend_username/id`
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
