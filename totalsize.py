from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaDocument, MessageMediaPhoto

# Replace with your API credentials
api_id =   # <-- Replace with your actual API ID XXXXXXXXXX
api_hash = ''  # <-- Replace with your actual API Hash XXXXXXXXXXXXXXXXXXXXXXXXX

# Replace with your target channel ID (with -100 prefix)
channel_id = -100  # <-- Replace with your actual channel ID "-100XXXXXXXXX"

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

total_size = 0
count = 0

async def main():
    global total_size, count

    await client.start()
    print("Logged in successfully.")

    # Resolve the channel entity
    try:
        channel = await client.get_entity(channel_id)
    except Exception as e:
        print(f"Error getting channel entity: {e}")
        return

    print(f"Fetching media from channel: {channel.title}")

    async for message in client.iter_messages(channel):
        if message.media and (isinstance(message.media, MessageMediaDocument) or isinstance(message.media, MessageMediaPhoto)):
            if message.file:
                count += 1
                total_size += message.file.size or 0

    print(f"\nTotal media files: {count}")
    print(f"Total size: {total_size / (1024 * 1024):.2f} MB")

# Run the async function
with client:
    client.loop.run_until_complete(main())

