import logging
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters

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

# Текст для описания бота
BOT_DESCRIPTION = """Ласкаво просимо до нашого магазину, де ви знайдете тільки найкращу техніку Apple — нову та б/у за вигідними цінами! 😊

Відчуйте якість Apple з нашим асортиментом нових та сертифікованих пристроїв! 🍏

Шукаєте надійну техніку Apple? У нас є нові моделі та перевірені пристрої, що задовольнять навіть найвибагливих покупців! 📱

Обирайте нові та сертифіковані продукти Apple — якість і інновації за доступною ціною тільки в нашому магазині! 💻"""

# Текст приветствия
WELCOME_TEXT = """🎉 Ласкаво просимо до нашого магазину!

🌟 Вітаємо вас у нашому магазині — місці, де зручність і вигода завжди поруч!

🛍️ **Щоб відкрити магазин**, просто натисніть кнопку "Магазин" нижче."""

# Ссылка на гифку
GIF_URL = "https://i.gifer.com/3P0Ho.gif"

# URL для Web App
WEB_APP_URL = "https://itconcerent.github.io/markesell/"

async def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start"""
    try:
        keyboard = [[
            InlineKeyboardButton(
                "🛍️ Відкрити магазин", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_animation(
            animation=GIF_URL,
            caption=WELCOME_TEXT,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        logger.info(f"Відправлено повідомлення користувачу {update.effective_user.id}")
    except Exception as e:
        logger.error(f"Помилка: {e}")

async def shop_command(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /shop"""
    try:
        keyboard = [[
            InlineKeyboardButton(
                "🛍️ Відкрити магазин", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🛍️ Натисніть кнопку нижче, щоб відкрити магазин:",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Помилка: {e}")

async def setup_bot_commands(application: Application):
    """Настройка команд бота"""
    commands = [
        ("start", "Запустити бота"),
        ("shop", "Відкрити магазин")
    ]
    await application.bot.set_my_commands(commands)

async def post_init(application: Application) -> None:
    """Функция после инициализации"""
    try:
        await application.bot.set_my_description(BOT_DESCRIPTION)
        await setup_bot_commands(application)
        logger.info("✅ Налаштування бота завершено")
    except Exception as e:
        logger.error(f"Помилка налаштування: {e}")

def main() -> None:
    """Запуск бота"""
    try:
        application = (
            Application.builder()
            .token(BOT_TOKEN)
            .post_init(post_init)
            .build()
        )
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("shop", shop_command))
        
        logger.info("🤖 Бот запускається...")
        print("🤖 Бот запускається...")
        
        # Простой запуск без дополнительных параметров
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ Помилка запуску: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
