from faker import Faker
import telegram
import asyncio
import time

async def send_telegram_message(chat_id, message):
    bot = telegram.Bot(token='XXXX')
    await bot.send_message(chat_id=chat_id, text=message)

async def send_multiple_messages():
    chat_id = 'XXXX'
    faker = Faker()

    for i in range(3):
        message = faker.word()
        time.sleep(2)
        await send_telegram_message(chat_id, message)


# crea un bucle de eventos asyncio y ejecuta la función send_multiple_messages
loop = asyncio.get_event_loop()
loop.run_until_complete(send_multiple_messages())
