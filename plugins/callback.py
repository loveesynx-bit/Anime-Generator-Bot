from pyrogram import Client as SynaxBots
from modules.enums import PicCategory, PicType
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto
from translation import INLINE, TEXT
from utils.api import generate_pic


@SynaxBots.on_callback_query()
async def handle_callback(client: SynaxBots, query: CallbackQuery):
    data: str = query.data
    message: Message = query.message
    """Not adding any condition coz it has only one type of callback"""
    type = data.split("_")[0]
    category = data.split("_")[1]
    category_enum = PicCategory[category.upper()]
    type_enum = PicType[type.upper()]
    while True:
        try:
            await message.reply_photo(
                photo=generate_pic(type_enum, category_enum),
                caption=TEXT.START,
                reply_markup=INLINE.START_BOARD(),
            )
            break
        except Exception as e:
            print(e)
            continue
