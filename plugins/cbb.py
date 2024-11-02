from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
                        text = f"<b>○ Creator : <a>『𝒀𝒂𝒆 𝑴𝒊𝒌𝒐•』❋𝄗⃝🦋 ⌞Wᴀʀʟᴏʀᴅ⌝ ㊋</a>\n○ 𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎 : <code>Python3</code>\n○ 𝙻𝚒𝚋𝚛𝚊𝚛𝚢 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Team_Originals'>𝙼𝚊𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 </a></a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝙲𝚕𝚘𝚜𝚎", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 {query.from_user.username}\n\n🎖️ 𝙰𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝙿𝚕𝚊𝚗𝚜 :\n\n● {PRICE1} 𝚁𝚜 𝙵𝚘𝚛 7 𝙳𝚊𝚢𝚜 𝙿𝚛𝚒𝚖𝚎 𝙼𝚎𝚖𝚋𝚎𝚛𝚜𝚑𝚒𝚙.\n\n● {PRICE2} 𝚁𝚜 𝙵𝚘𝚛 1 𝙼𝚘𝚗𝚝𝚑 𝙿𝚛𝚒𝚖𝚎 𝙼𝚎𝚖𝚋𝚎𝚛𝚜𝚑𝚒𝚙.\n\n● {PRICE3} 𝚁𝚜 𝙵𝚘𝚛 3 𝙼𝚘𝚗𝚝𝚑𝚜 𝙿𝚛𝚒𝚖𝚎 𝙼𝚎𝚖𝚋𝚎𝚛𝚜𝚑𝚒𝚙.\n\n● {PRICE4} 𝚁𝚜 𝙵𝚘𝚛 6 𝙼𝚘𝚗𝚝𝚑𝚜 𝙿𝚛𝚒𝚖𝚎 𝙼𝚎𝚖𝚋𝚎𝚛𝚜𝚑𝚒𝚙.\n\n● {PRICE5} 𝚁𝚜 𝙵𝚘𝚛 1 𝚈𝚎𝚊𝚛 𝙿𝚛𝚒𝚖𝚎 𝙼𝚎𝚖𝚋𝚎𝚛𝚜𝚑𝚒𝚙.\n\n\n💵 𝚄𝙿𝙸 𝙸𝙳 -  <code>{UPI_ID}</code>\n\n\n📸 𝚀𝚁 - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n♻️ 𝙸𝚏 𝙿𝚊𝚢𝚖𝚎𝚗𝚝 𝙸𝚜 𝙽𝚘𝚝 𝙶𝚎𝚝𝚝𝚒𝚗𝚐 𝚂𝚎𝚗𝚝 𝙾𝚗 𝙰𝚋𝚘𝚟𝚎 𝙶𝚒𝚟𝚎𝚗 𝚀𝚛 𝙲𝚘𝚍𝚎 𝚃𝚑𝚎𝚗 𝙸𝚗𝚏𝚘𝚛𝚖 𝙰𝚍𝚖𝚒𝚗, 𝙷𝚎 𝚆𝚒𝚕𝚕 𝙶𝚒𝚟𝚎 𝚈𝚘𝚞 𝙽𝚎𝚠 𝚀𝚁 𝙲𝚘𝚍𝚎.\n\n\n‼️ 𝙼𝚞𝚜𝚝 𝚂𝚎𝚗𝚍 𝚂𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝 𝙰𝚏𝚝𝚎𝚛 𝙿𝚊𝚢𝚖𝚎𝚗𝚝.",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("𝚂𝚎𝚗𝚍 𝙿𝚊𝚢𝚖𝚎𝚗𝚝 𝚂𝚌𝚛𝚎𝚎𝚗𝚜𝚑𝚘𝚝(𝙰𝙳𝙼𝙸𝙽) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 𝙲𝚕𝚘𝚜𝚎", callback_data = "close")
                    ]
                ]
            )
            )
