from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '7915844491:AAFoePo3pFzCmLnyuhY9iDPWB_d2bwO2HkE'
application = ApplicationBuilder().token(TOKEN).build()

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Received /start command")
    await update.message.reply_text("Hello!, I'm your bot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Received /help command")
    await update.message.reply_text(
        "Here's how I can help you:\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "/task - Automate a task\n"
        "/status - Check status\n"
        "/reminder - Set a reminder"
    )

async def task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Received /task command")
    await update.message.reply_text("Automating task...")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Received /status command")
    await update.message.reply_text("Current status: All systems operational.")

async def reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Received /reminder command")
    await update.message.reply_text("Setting a reminder...")

# Enhanced message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower()  # Convert to lowercase for easier comparison
    logger.info("Received a message: %s", user_message)
    
    if "hello" in user_message:
        await update.message.reply_text("Hi there! How can I assist you?")
    elif "bye" in user_message:
        await update.message.reply_text("Goodbye! Have a great day!")
    elif "task" in user_message:
        await update.message.reply_text("Would you like me to automate a specific task?")
    else:
        await update.message.reply_text("I'm here to help! Please use /help to see what I can do.")

# Adding command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('task', task))
application.add_handler(CommandHandler('status', status))
application.add_handler(CommandHandler('reminder', reminder))

# Adding message handler for non-command messages
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Start the bot
if __name__ == '__main__':
    logger.info("Starting the bot")
    application.run_polling()
