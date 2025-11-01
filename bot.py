import logging
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не знайдено!")
    sys.exit(1)

# Текст для описания бота (будет показан при запуске)
BOT_DESCRIPTION = """Ласкаво просимо до нашого магазину, де ви знайдете тільки найкращу техніку Apple — нову та б/у за вигідними цінами! 😊

Відчуйте якість Apple з нашим асортиментом нових та сертифікованих пристроїв! 🍏

Шукаєте надійну техніку Apple? У нас є нові моделі та перевірені пристрої, що задовольнять навіть найвибагливих покупців! 📱

Обирайте нові та сертифіковані продукти Apple — якість і інновації за доступною ціною тільки в нашому магазині! 💻"""

# Текст приветствия с эмодзи
WELCOME_TEXT = """🎉 Ласкаво просимо до нашого магазину!

🌟 Вітаємо вас у нашому магазині — місці, де зручність і вигода завжди поруч!

Ми раді, що ви завітали до нас. Тут ви знайдете великий вибір продукції за привабливими цінами, а також швидкий сервіс і надійну підтримку.

🛍️ **Щоб відкрити магазин**, просто натисніть кнопку "Магазин" нижче. Він відкриється у зручному міні-додатку прямо в Telegram!

🔹 Для вашої зручності ми додали меню, яке відкривається у нижньому кутку чату. Завдяки цьому ви з легкістю знайдете інформацію про оплату, доставку та гарантії.

🔹 Якщо у вас є питання або потрібна допомога у виборі — пишіть нам у Instagram! Посилання на нашу сторінку є в меню.

💬 Ми завжди готові допомогти вам знайти саме те, що вам потрібно!

Дякуємо за ваш вибір та бажаємо приємних покупок! 💛"""

# Ссылка на гифку
GIF_URL = "https://i.gifer.com/3P0Ho.gif"

# URL для Web App
WEB_APP_URL = "https://itconcerent.github.io/markesell/"

def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start"""
    try:
        keyboard = [[
            InlineKeyboardButton(
                "🛍️ Відкрити магазин", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        update.message.reply_animation(
            animation=GIF_URL,
            caption=WELCOME_TEXT,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        logger.info(f"Відправлено повідомлення користувачу {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Помилка: {e}")

def shop_command(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /shop для прямого открытия магазина"""
    try:
        keyboard = [[
            InlineKeyboardButton(
                "🛍️ Відкрити магазин", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        update.message.reply_text(
            "🛍️ Натисніть кнопку нижче, щоб відкрити магазин у міні-додатку:",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Помилка: {e}")

def menu_command(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /menu для показа основного меню"""
    try:
        keyboard = [
            [InlineKeyboardButton("🛍️ Магазин", web_app=WebAppInfo(url=WEB_APP_URL))],
            [InlineKeyboardButton("📞 Підтримка", url="https://instagram.com")],
            [InlineKeyboardButton("ℹ️ Про нас", callback_data="about")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        update.message.reply_text(
            "🏪 **Головне меню**\n\nОберіть опцію:",
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    except Exception as e:
        logger.error(f"Помилка: {e}")

def main() -> None:
    """Запуск бота"""
    try:
        updater = Updater(BOT_TOKEN)
        dispatcher = updater.dispatcher
        
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("shop", shop_command))
        dispatcher.add_handler(CommandHandler("menu", menu_command))
        
        logger.info("🤖 Бот запускається...")
        print("🤖 Бот запускається...")
        
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        logger.error(f"❌ Помилка запуску: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
