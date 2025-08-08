import logging
import openai
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def handle_message(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": message.text}
            ],
            max_tokens=1000,
            temperature=0.7,
        )

        reply = response.choices[0].message['content']
        await message.reply(reply)

    except Exception as e:
        import traceback
        traceback_text = ''.join(traceback.format_exception(None, e, e.__traceback__))
        await message.reply(f"Произошла ошибка:\n{traceback_text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

