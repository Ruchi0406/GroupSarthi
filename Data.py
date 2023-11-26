from pyrogram.types import InlineKeyboardButton
from Config import BOT_USERNAME

class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} 🥀

➢ ɪ ᴄᴀɴ ғᴏʀᴄᴇ  ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴜsᴇʀ ᴛᴏ ᴊᴏɪɴ  ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ.
➢ ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ɪᴛ ᴄᴀɴ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ.
➢ ꜰᴏʀ ᴀɴʏ ᴛʏᴘᴇ ᴏꜰ Qᴜᴇʀʏ, ᴅᴍ [ᴀᴍᴀɴ](https://t.me/Its_amanz) ᴏʀ ᴊᴏɪɴ [ꜱᴜᴘᴘᴘʀᴛ ɢʀᴏᴜᴘ](https://t.me/offtopic_community)
➢ ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ʙᴀʙʏ !



    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="home")],
    ]

    # Rest Buttons
    buttons =[ [ InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕", url=f"https://t.me/GroupSarthi_bot?startgroup=true")],
    [InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
    InlineKeyboardButton("ᴀʙᴏᴜᴛ ", callback_data="about")
    ]
             ]
   
# Help Message
    HELP = """
➪ ᴀᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴀ ɢʀᴏᴜᴘ. 
➪ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴀs ᴀᴅᴍɪɴ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ғᴏʀᴄᴇ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ. ɪᴛ ᴄᴀɴ ʙᴇ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ, ᴘᴜʙʟɪᴄ ᴏʀ ᴘʀɪᴠᴀᴛᴇ. 
➪ ᴜsᴇ /fsub chat_id /username ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ғᴜɴᴄᴛɪᴏɴᴀʟ. ᴜsᴇ /id ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴄʜᴀᴛ ɪᴅ.
 ᴇxᴀᴍᴘʟᴇ : /fsub -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 ᴏʀ /forcesubsribe -𝟷𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶𝟶 
➪ [ᴏᴘᴛɪᴏɴᴀʟ] ᴜsᴇ /settings ᴛᴏ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs! 
➪ ʏᴏᴜ ᴀʀᴇ ɢᴏᴏᴅ ᴛᴏ ɢᴏ. ʟᴇᴀᴠᴇ ᴛʜᴇ ʀᴇsᴛ ᴛᴏ ᴍᴇ.

 ✨ ᴀᴠᴀɪʟᴀʙᴇ ᴄᴍᴅs ʙᴀʙʏ  ✨ 
/start -  sᴛᴀʀᴛ ғᴏʀᴄᴇ sᴜʙsʀɪʙᴇ ʙᴏᴛ 
/fsub - sᴇᴇ ᴄᴜʀʀᴇɴᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀᴛ 
/fsub chat_id/username- ғᴏʀᴄᴇ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ
/settings - ᴄʜᴀɴɢᴇ ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs 
/id - ɢᴇᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪᴅ ᴏғ ᴀɴʏ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ
/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ 
☞︎︎︎ ɴᴏᴛᴇ - ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ /forcesubsribe ɪɴsᴛᴇᴀᴅ ᴏғ /fsub
"""

# About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ  ғᴏʀᴄᴇ sᴜʙ...

┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛

╰☆☆ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [𝙹εε 𝚂ƭυ∂ყ 𝚁σσɱ](https://t.me/jee_study_room) ☆☆╮


╰☆☆ ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org) ☆☆╮

╰☆☆ ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org) ☆☆╮

╰☆☆ ᴅᴇᴠᴇʟᴏᴘᴇʀ :  [𝐀∂íƭყα](https://t.me/jsruordinators) ☆☆╮

╰☆☆ ᴜᴘᴅᴀᴛᴇ  : [𝗝ᴇᴇ 𝐒ᴛᴜᴅʏ 𝐑ᴏᴏᴍ](https://t.me/jee_study_room) ☆☆╮

╰☆☆ ʀᴇᴘᴏ  : ꜱᴏʀʀʏ, ᴛʜᴇ ʀᴇᴘᴏ ɪꜱ ᴘʀɪᴠᴀᴛᴇ 😌 ☆☆╮
    """
