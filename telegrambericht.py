from telegram import Bot
import asyncio

def telegramMessage(inputstring, telegram_token, telegram_chat_id):
    bot = Bot(token=telegram_token)

    try:
        async def verstuurBericht():
            await bot.send_message(chat_id=telegram_chat_id, text=inputstring)
    
        asyncio.run(verstuurBericht())
        print("Telegrambericht verstuurd: " + inputstring)

    except:
        print("Er is een fout opgetreden bij het versturen van het telegrambericht: " + inputstring)

# telegramMessage("Dikke vette test", telegram_token, telegram_chat_id)