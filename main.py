from telegram.ext import *
from telegram import *
import requests

url = "https://newsapi.org/v2/everything?"

# Create a callback to receive the data from the user.

#Start the conversation /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

#Topic for the discussion /topic
async def topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

# Category for the news
async def category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

# Source from which you want to get the news. BBC, CNN
async def source(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

#The user will be able to choose the language in which they want to receive the news.
async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

# This is the function that send the actual news to the user.
async def receive_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass