import aioschedule
import pandas
from datetime import date
from aiogram import Bot, Dispatcher
import logging
from aiogram.utils import executor
import asyncio

from get_file import get_file

API_TOKEN = 'bot token'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

number_of_row = None
current_person_data = []


def convert_time(date):
    return pandas.to_datetime(date)


async def work_procces():
    get_file(
        'link of exel')  # exel link
    global number_of_row
    global current_person_data
    book = pandas.read_excel("Daily_checklist.xlsx", sheet_name='Sheet3', converters={'Date': convert_time})  # 1) file name
    book_dict = book.to_dict()

    for i in book_dict['Date']:
        if str(book_dict['Date'][i])[0:10] == str(date.today().strftime("%Y-%m-%d")):
            number_of_row = i
            current_person_data.append(book_dict['Date'][i])  # the row from which the row number is taken
    try:
        current_person_data.append(book_dict['Person'][number_of_row])  # name of raw
        current_person_data.append(book_dict['Checked/Enabled'][number_of_row])  # name of second raw

        if current_person_data[1] != current_person_data[1] or current_person_data[2] != current_person_data[2]:
            await send_message('CAACAgIAAxkBAAEF9OljNgi83xhhV3DtkvPJ2xQLmMBHyQACewEAAsFGhhtYD8mbVUkgJSoE', 'sticker')  # sticker and type of message
            await send_message('some line of the current date is not filled!')
        else:
            await send_message('CAACAgIAAxkBAAEF9OtjNgjDaRlMKWP_1nbpco1WeC78tgACegEAAsFGhhu4NJiihthNaioE', 'sticker')  # sticker and type of message
            await send_message(f'all okay Person: {current_person_data[1]}\nchecked:  {current_person_data[2]}!')

    except KeyError:
        print('current date not found')


async def send_message(data, type='message', chatId='here must be chat_id'):  # fill in the chat id with your chat id
    if type == 'sticker':
        await bot.send_sticker(chatId, data)
    elif type == 'message':
        await bot.send_message(chatId, data)


async def scheduler():
    aioschedule.every().day.at("18:00").do(work_procces)
    aioschedule.every().day.at("18:30").do(work_procces)
    aioschedule.every().day.at("19:00").do(work_procces)
    aioschedule.every().day.at("19:30").do(work_procces)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
