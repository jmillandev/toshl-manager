import os
from dotenv import load_dotenv

load_dotenv()

TOSH_SECRET_KEY = os.environ['TOSH_SECRET_KEY']
LOAND_CATEGORY_ID = os.environ['TOSHL_LOAND_CATEGORY_ID']
LOAND_TAG_IDS = os.environ['TOSHL_LOAND_TAG_IDS']
