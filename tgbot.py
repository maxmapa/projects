import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from FlightRadar24 import FlightRadar24API  
from requests.exceptions import RequestException

# Налаштування логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Ваша функція для конвертації часу
def convert_unix_to_hms(seconds):
    is_negative = seconds < 0
    seconds = abs(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    hms_format = f"{int(hours):02}:{int(minutes):02}:{int(remaining_seconds):02}"
    if is_negative:
        hms_format = "-" + hms_format
    return hms_format

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Введіть номер рейсу для слідкування.')

async def flight_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        flight_tracker = update.message.text.strip().upper()
        fr_api = FlightRadar24API()
        airport_code = 'FAO'
        airport_details = fr_api.get_airport_details(airport_code)
        arrivals_data = airport_details['airport']['pluginData']['schedule']['arrivals']['data']
        
        for arrival in arrivals_data:
            flight_number = arrival['flight']['identification']['number']['default']
            scheduled_arrival = arrival['flight']['time']['scheduled']['arrival']
            estimated_arrival = arrival['flight']['time']['estimated']['arrival']
            
            if flight_number == flight_tracker:
                if estimated_arrival is not None:            
                    await update.message.reply_text(f"{flight_number} прибуде через {convert_unix_to_hms(estimated_arrival-scheduled_arrival)} від розкладу")
                else:
                    await update.message.reply_text(f"{flight_number} ще не вилетів.")
                return
        await update.message.reply_text(f"Рейс {flight_tracker} не знайдено.")
    
    except RequestException as e:
        logging.error(f"Помилка при запиті до FlightRadar24: {e}")
        await update.message.reply_text("Виникла помилка при спробі отримати дані про рейс. Спробуйте ще раз пізніше.")
    
    except Exception as e:
        logging.error(f"Непередбачувана помилка: {e}")
        await update.message.reply_text("Виникла непередбачувана помилка. Будь ласка, спробуйте ще раз.")

# Responses
def main() -> None:
    # Токен, який ви отримали від BotFather
    token = '7151568511:AAFm-R9IskQwQUufbXOMvxVRu_1W0BCsfBs'
    
    # Створення application
    app = Application.builder().token(token).build()

    # Реєстрація обробників команд 
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("flight", flight_command))
    # Реєстрація обробників повідомлень
    app.add_handler(MessageHandler(filters.TEXT, flight_command))

    # Запуск бота
    app.run_polling(poll_interval=30)

if __name__ == '__main__':
    main()
