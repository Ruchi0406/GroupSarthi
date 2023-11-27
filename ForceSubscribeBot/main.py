from pyrogram import Client, filters
import Config
from datetime import datetime, timedelta
from ForceSubscribeBot.database.chats_sql import get_force_chat, get_action, get_ignore_service
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, ChatPermissions
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions

@Client.on_message(filters.group, group=-1)
async def main(bot: Client, msg: Message):
    if not msg.from_user:
        return

    user_id = msg.from_user.id
    if user_id in Config.DEVS:
        return

    chat_id = msg.chat.id
    force_chat = await get_force_chat(chat_id)
    ignore_service = await get_ignore_service(chat_id)

    if ignore_service and msg.service:
        return

    if not force_chat:
        return

    try:
        try:
            await bot.get_chat_member(force_chat, user_id)
        except UserNotParticipant:
            chat_member = await msg.chat.get_member(user_id)

            if chat_member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                return

            chat = await bot.get_chat(force_chat)
            mention = '@' + chat.username if chat.username else f"[{chat.title}]({chat.invite_link})"
            link = chat.invite_link

            try:
                action = await get_action(chat_id)

                # Set the default action to 'warn' if no specific action is configured
                action = action if action else 'warn'

                if action == 'warn':
                    await msg.reply(
                        f"ʜᴇʏ ᴅᴇᴀʀ  {msg.from_user.mention},\n\nʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ {mention} ᴛᴏ ʀᴇᴍᴀɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴛʏᴘᴇ ᴏꜰ ᴡᴀʀɴɪɴɢ (◕‿◕)",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ sᴜʙsᴄʀɪʙᴇ  ᴍʏ ᴄʜᴀɴɴᴇʟ  ✨", url=link)]])
                    )
                    await msg.delete()
                    await msg.stop_propagation()

            except ChatWriteForbidden:
                pass

    except ChatAdminRequired:
        await msg.reply(f"ɪ ʜᴀᴠᴇ ʙᴇᴇɴ ᴅᴇᴍᴏᴛᴇᴅ ɪɴ {force_chat} (force subscribe chat)")

# Define the modified get_action function without the placeholder
async def get_action(chat_id):
    # Replace this with your actual logic to retrieve the desired action for the chat
    # If no specific action is set, return 'warn' by default
    # For example, you might have a database query or some other logic here
    # Replace the following line with your actual logic
    # action = your_actual_logic_to_retrieve_action(chat_id)
    action = 'warn'  # Default to 'warn' if no specific action is configured
    return action
