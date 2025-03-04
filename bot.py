import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command handlers
async def start(update: Update, context: CallbackContext) -> None:
    """Send welcome message when /start is issued"""
    await update.message.reply_text('مرحبًا! أنا بوت حجز الطيران والفنادق. كيف يمكنني مساعدتك اليوم؟')

async def flight_booking(update: Update, context: CallbackContext) -> None:
    """Handle /flight command"""
    await update.message.reply_text('من فضلك، أرسل لي تفاصيل الرحلة، مثل: المدينة المغادرة، الوجهة، وتاريخ الرحلة.')

async def hotel_booking(update: Update, context: CallbackContext) -> None:
    """Handle /hotel command"""
    await update.message.reply_text('من فضلك، أرسل لي تفاصيل الفندق، مثل: المدينة، تواريخ الوصول والمغادرة.')

async def main() -> None:
    """Start the bot"""
   application = Application.builder().token("7630764937:AAFX-4OhLzTf0tGv7w8E5VXWIyBMYa-g33g").build()

    # Register commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("flight", flight_booking))
    application.add_handler(CommandHandler("hotel", hotel_booking))

    # Run bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
