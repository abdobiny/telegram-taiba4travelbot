import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# إعدادات التسجيل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# أمر البدء
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت حجز الطيران والفنادق. كيف يمكنني مساعدتك اليوم؟')

# أمر لحجز تذكرة طيران
def flight_booking(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('من فضلك، أرسل لي تفاصيل الرحلة، مثل: المدينة المغادرة، الوجهة، وتاريخ الرحلة.')

# أمر لحجز فندق
def hotel_booking(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('من فضلك، أرسل لي تفاصيل الفندق، مثل: المدينة، تواريخ الوصول والمغادرة.')

# الخط الرئيسي
def main():
    # استبدل "YOUR_API_TOKEN" بالتوكن الخاص بك من @BotFather
    updater = Updater("YOUR_API_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    # إضافة الأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("flight", flight_booking))
    dispatcher.add_handler(CommandHandler("hotel", hotel_booking))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

