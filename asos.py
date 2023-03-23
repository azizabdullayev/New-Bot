# from aiogram.types import Message
# from config import dp
# from aiogram import executor
#
#
# @dp.message_handler(commands="start")
# async def start(message: Message):
#     await message.answer(f"Salom {message.from_user.full_name}\n"
#                          f"Xush kelibsiz!")
#
# @dp.message_handler(text="Osha san")
# async def sokma(msg: Message):
#     await msg.answer("O'zing o'shnaqasan!")
#
# @dp.message_handler(commands="help")
# async def help(message: Message):
#     await  message.answer((f"Hurmatli {message.from_user.full_name}\n"
#                                f"Sizga yordam yo'q!"))
#
# @dp.message_handler(state=None)
# async def exo(msg: Message):
#     await msg.reply(msg.text)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
