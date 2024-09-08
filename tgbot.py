from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your API ID and Hash
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
source_channel = 'hs_cryptonews'  # Source channel username (without @)
destination_channel = 'cryptonationama'  # Destination channel username (without @)

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    # Prepare the message text by removing the source username
    message_text = event.raw_text.replace(f'@{source_channel}', '') + f'\n\n@{destination_channel}'

    # Forward the message to the destination channel
    await client.send_message(destination_channel, message_text)

    # Check if the message contains media (images, videos, etc.)
    if event.media:
        await client.send_file(destination_channel, event.media)

# Start the client
async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

# Run the bot
import asyncio
asyncio.run(main())
