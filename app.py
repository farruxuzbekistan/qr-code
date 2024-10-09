# 7529842582:AAFemCiuWkmVlSJKXww1iUjaI0aaV9EBKpA
# ctrl + p
import qrcode
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = "7529842582:AAFemCiuWkmVlSJKXww1iUjaI0aaV9EBKpA"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# handle start command
@dp.message_handler(commands=["start"])
async def welcome_message(message: types.Message):
    await message.reply(
        "Assalom alaykum, bizga istalgan link yoki text yuboring, biz uni QR shaklida qilib beramiz!!!"
    )


# handle help message


@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    await message.reply(
        "Assalom alaykum, bizga istalgan link yoki text yuboring, biz uni QR shaklida qilib beramiz!!!"
    )


@dp.message_handler()
async def generate_qr(message: types.Message):

    text = message.text

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # save image
    image_file = f"qr_code_{message.from_user.id}.png"
    img.save(image_file)

    # send image
    await message.reply_photo(
        photo=open(image_file, "rb"), caption="Mana sizning QR code giz"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
