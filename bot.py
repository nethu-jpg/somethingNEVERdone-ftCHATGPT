import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR, AUTH_CHANNEL
from utils import temp, get_poster

# Initialize Pyrogram client
app = Client("my_bot")

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1

    async def handle_group_message(self, message):
        if "cars" in message.text.lower():
            # Fetch IMDb poster for "cars"
            imdb_poster_url = await get_poster("cars")
            # Send IMDb poster and button
            await message.reply_photo(
                photo=imdb_poster_url['poster'],
                caption="Click the button to continue.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Continue", callback_data="pm_request_cars")]])
            )

    @app.on_message(filters.group & ~filters.edited)
    async def group_message_handler(self, message):
        # Extract the query from the incoming message
        query = message.text.lower()  # Assuming the query is in the text of the message
    
        # Retrieve the IMDb poster based on the query
        poster_data = await get_poster(query)
    
        # Create a button for initiating a private message
        private_message_button = InlineKeyboardButton(
            text="Send Message",
            url=f"t.me/{self.username}?start=send_pm&query={query}"  # Modify this URL as needed
        )
    
        # Create an inline keyboard with the private message button
        inline_keyboard = InlineKeyboardMarkup([[private_message_button]])
    
        # Send the IMDb poster along with the inline keyboard as a reply to the group message
        if poster_data:
            await message.reply_photo(
                photo=poster_data['poster'],
                caption=f"IMDb Poster for '{query}':",
                reply_markup=inline_keyboard
            )
        else:
            await message.reply_text("Sorry, no IMDb poster found for that query.")

app = Bot()
app.run()
