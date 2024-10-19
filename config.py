from operator import add
import os
import logging
import random
import string
from pymongo import MongoClient
from logging.handlers import RotatingFileHandler

# Load environment variables here if needed (e.g., using dotenv)
# from dotenv import load_dotenv
# load_dotenv()

# Force user to join your backup channel; leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002042137942"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002206552452"))

if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2 
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp

# Bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>BOT UPTIME </b>\n{uptime}")
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "Don't send me messages directly I'm only a File Share bot!")

# Your bot token and other credentials
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8018142187:AAECnUlFxysBtTMN7jzkLN62h0LAPsox1zQ") 
APP_ID = int(os.environ.get("APP_ID", "26590590"))
API_HASH = os.environ.get("API_HASH", "4805ee1d57b1be7f5135e736c816a2d1")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001992443365"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5904478052"))
PORT = os.environ.get("PORT", "6666")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://zuuvou:XNWdDOsGFprx7Cnw@clusterop.pnyvj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "filestorabot")

# Database initialization
client = MongoClient(DB_URL)
db = client[DB_NAME]
users_collection = db['users']  # Assuming you're using a collection named 'users'

# Bot settings
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in a specified channel and other users can access them from a special link.")
OWNER_TAG = os.environ.get("OWNER_TAG", "POWERMODOWNER")
TIME = int(os.environ.get("TIME", "0"))

# Referral system variables
def generate_referral_code(user_id):
    # Create a simple referral code (e.g., last 4 digits of user ID + random letters)
    return str(user_id)[-4:] + ''.join(random.choices(string.ascii_letters, k=4))

async def register_user(user_id, first_name, referral_code=None):
    user = users_collection.find_one({"user_id": user_id})
    if not user:
        referral_count = 0
        # Check if referral_code is provided
        if referral_code:
            referrer = users_collection.find_one({"referral_code": referral_code})
            if referrer:
                referral_count = referrer.get("referral_count", 0) + 1
                users_collection.update_one({"user_id": referrer["user_id"]}, {"$set": {"referral_count": referral_count}})
        referral_code = generate_referral_code(user_id)
        users_collection.insert_one({
            "user_id": user_id,
            "first_name": first_name,
            "referral_code": referral_code,
            "referral_count": 0,
            # Add other user fields as necessary
        })

@bot.on_message(filters.command('start'))
async def start_command(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    referral_code = message.text.split()[1] if len(message.text.split()) > 1 else None
    await register_user(user_id, first_name, referral_code)
    await message.reply_text(START_MSG.format(first=first_name))

@bot.on_message(filters.command('referral'))
async def referral_command(client, message):
    user_id = message.from_user.id
    user = users_collection.find_one({"user_id": user_id})
    if user:
        referral_code = user.get("referral_code")
        await message.reply_text(f"Your referral code: `{referral_code}`. Share it with your friends!")

@bot.on_message(filters.command('myreferrals'))
async def my_referrals_command(client, message):
    user_id = message.from_user.id
    user = users_collection.find_one({"user_id": user_id})
    if user:
        referral_count = user.get("referral_count", 0)
        await message.reply_text(f"You have referred {referral_count} users.")

# Set up logging
LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Admins list
try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "5904478052").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
