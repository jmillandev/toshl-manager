import os
from dotenv import load_dotenv

load_dotenv()

SEPARATOR = ','
TOSH_SECRET_KEY = os.environ['TOSH_SECRET_KEY']
LOAND_CATEGORY_ID = os.environ['TOSHL_LOAND_CATEGORY_ID']
DEBTOR_TAG_ID = os.environ['TOSHL_DEBTOR_TAG_ID']
UNPAYMENT_TAG_ID = os.environ['TOSHL_UNPAYMENT_TAG_ID']
ROOMIE_TAG_ID = os.environ['TOSHL_ROOMIE_TAG_ID']
BUGGETS_SHARED = os.environ['TOSHL_BUGGETS_SHARED_IDS'].split(SEPARATOR)
BOT_TOKEN = os.environ['TELEGRAM_KEY']
BOT_OWNER = os.environ['TELEGRAM_BOT_OWNER']