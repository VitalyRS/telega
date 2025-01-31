import telebot
import os

# Replace 'YOUR_API_TOKEN' with the token you received from BotFather
# API_TOKEN = 'YOUR_API_TOKEN'
# Получение API-токена из переменной окружения
API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)


# Define a message handler to respond to any text message
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # Print the received message to the console
    print(f"Received message from {message.chat.id}: {message.text}")

    # Optionally, send the same message back to the user
    # bot.reply_to(message, message.text)


if __name__ == '__main__':
    print("Starting the bot...")
    # port = int(os.environ.get('PORT', 5000))  # Используйте порт из переменной окружения
    print(f"Server is running on port {port}")
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"An error occurred: {e}")
