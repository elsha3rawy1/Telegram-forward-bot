from telethon import TelegramClient, events
import asyncio

api_id = '26283926'
api_hash = 'fcd8c080125fad9062c9bc7d9cb2ca2d'
phone_number = '+201093706011'

source_channel = 'hhahsgsuw6'
target_channel = 'signals_elsha3rawy1'

owner_id = 2065056216

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message_text = event.message.text
    sender_id = event.sender_id
    if sender_id == owner_id and message_text.endswith("pump"):
        await client.forward_messages(target_channel, event.message)

async def main():
    await client.start(phone_number)
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
