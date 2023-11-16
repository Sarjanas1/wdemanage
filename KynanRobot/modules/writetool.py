import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext
from telegram.ext.dispatcher import run_async

from KynanRobot import dispatcher
from KynanRobot.modules.disable import DisableAbleCommandHandler


@run_async
def handwrite(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = update.effective_message.text.split(None, 1)[1]
    m = message.reply_text("Processing...")
    req = requests.get(f"https://api.sdbots.tk/write?text={text}").url
    message.reply_photo(
        photo=req,
        caption=f"""
I managed to write for you 💘

✏️ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ**: [Zenitsu](https://t.me/zenitsuuuxrobot)
👤 **ʀᴇϙᴜᴇꜱᴛᴇᴅ ʙʏ**: {update.effective_user.first_name}
🔗 **ʟɪɴᴋ ᴛᴇʟᴇɢʀᴀᴘʜ**: `{req}`""",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴛᴇʟᴇɢʀᴀᴘʜ", url=req),
                ],
            ]
        ),
    )
    m.delete()


__help__ = """
──「 ᴡʀɪᴛɪɴɢ 」──

 Membuat Tulisan Otomatis Dibuku 🖊

• /write <teks> *:* Menulis teks yang diberikan.
"""

WRITE_HANDLER = DisableAbleCommandHandler("write", handwrite)

dispatcher.add_handler(WRITE_HANDLER)

__mod_name__ = "ᴡʀɪᴛɪɴɢ"
__command_list__ = ["write"]
__handlers__ = [WRITE_HANDLER]
