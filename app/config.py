import os

from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# AI Model
MODEL_NAME = "openai/gpt-4o-mini"
TEMPERATURE = 0.7
MAX_TOKENS = 512

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing")