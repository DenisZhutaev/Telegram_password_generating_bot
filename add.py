import telebot
import secrets
import string

# 1. telebot - это библиотека для создания Telegram-ботов на языке Python. Она предоставляет удобный
# интерфейс для работы с API Telegram и позволяет легко создавать и настраивать ботов.
#
# 2. secrets - это модуль Python, который предоставляет функции для генерации криптографически безопасных
# случайных чисел, строк и токенов. В этом коде он используется для генерации случайных паролей.
#
# 3. string - это модуль Python, который предоставляет константы и функции для работы со строками. В этом коде
# он используется для определения алфавита, из которого будут генерироваться случайные пароли.


# Укажите здесь токен вашего бота
# TOKEN = 'YOUR_TOKEN_HERE'
TOKEN = "5640107001:AAETbZtZyHaeeTzeRe4l4Q6bAOlTkZJaqis"

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Обработчик команды /start.

    Отправляет приветственное сообщение пользователю.

    :param message: Объект сообщения от пользователя.
    """
    bot.reply_to(message, "Привет! Я бот для генерации паролей /generate.")


# Обработчик команды /generate
@bot.message_handler(commands=['generate'])
def generate_password(message):
    """
    Обработчик команды /generate.

    Запрашивает у пользователя длину пароля и генерирует случайный пароль заданной длины.

    :param message: Объект сообщения от пользователя.
    """
    # Запрашиваем у пользователя длину пароля
    msg = bot.reply_to(message, "Введите длину пароля:")
    bot.register_next_step_handler(msg, process_password_length)


def process_password_length(message):
    """
    Обработчик длины пароля.

    Получает длину пароля от пользователя и генерирует случайный пароль заданной длины.

    :param message: Объект сообщения от пользователя.
    """
    try:
        # Получаем длину пароля от пользователя
        password_length = int(message.text)

        # Проверяем, что длина пароля больше 0
        if password_length < 1:
            raise ValueError

        # Генерируем случайный пароль
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))

        # Отправляем пароль пользователю
        bot.reply_to(message, f"Вот твой новый пароль: {password}")

    except ValueError:
        # Если пользователь ввел некорректную длину пароля, сообщаем об этом и просим ввести корректное значение
        bot.reply_to(message, "Некорректная длина пароля.nВведите целое число от 1.")
        generate_password(message)


# Запускаем бота
bot.polling()
