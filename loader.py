from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from database.db_api import Database

TOKEN = "7975310823:AAGm1TCXpFeG1e59kyWf8zM4tR27FOmoCwM"

dp = Dispatcher()
baza = Database('database/main.db')
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
ADMIN = 5028235049
