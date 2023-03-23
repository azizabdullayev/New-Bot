from aiogram.types import Message
from  config import dp
from aiogram import executor
import wikipedia

wikipedia.set_lang("uz")
@dp.message_handler()
async def wiki(msg: Message):
    try:
        response = wikipedia.summary(msg.text)
        await msg.answer(response)
    except:
        await msg.answer("Topilmadi!")

if __name__ == '__main__':
    executor.start_polling(dp)