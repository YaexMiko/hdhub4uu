from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    
    # About callback action
    if data == "about":
        await query.message.edit_text(
            text=(
                f"<b>○ Creator : <a href='tg://user?id=6768137528'>Alya_x_Yuki</a>\n"
                f"○ Language : <code>Python3</code>\n"
                f"○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n"
                f"○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/+MhcwQJ-zeOUyZGQ9'>ᴄʏʙᴇʀᴍᴀᴛʀɪxᴛᴍ</a></b>"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🔒 𝐂𝐥𝐨𝐬𝐞", callback_data="close")]
                ]
            )
        )

    # Close callback action
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass

    # Buy Premium callback action
    elif data == "buy_prem":
        await query.message.edit_text(
            text=(
                f"👋 {query.from_user.username}\n\n"
                f"🎖️ Available Plans :\n\n"
                f"● {PRICE1} rs For 7 Days Prime Membership\n\n"
                f"● {PRICE2} rs For 1 Month Prime Membership\n\n"
                f"● {PRICE3} rs For 3 Months Prime Membership\n\n"
                f"● {PRICE4} rs For 6 Months Prime Membership\n\n"
                f"● {PRICE5} rs For 1 Year Prime Membership\n\n\n"
                f"💵 UPI ID -  <code>{UPI_ID}</code>\n\n"
                f"📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n"
                f"♻️ If payment is not getting sent on the above given QR code, "
                f"inform the admin for a new QR code\n\n"
                f"‼️ Must Send Screenshot after payment"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Send Payment Screenshot(ADMIN) 📸", url=(SCREENSHOT_URL))],
                    [InlineKeyboardButton("🔒 𝐂𝐥𝐨𝐬𝐞", callback_data="close")]
                ]
            )
        )
