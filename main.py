from telethon.sync import TelegramClient, events
import asyncio
import base64
import os

# استخراج ملف الجلسة من المتغير البيئي SESSION_DATA
session_data = os.getenv("SESSION_DATA")

if session_data:
    with open("session_name.session", "wb") as f:
        f.write(base64.b64decode(session_data))

# إعداد بيانات API
api_id = 26283926  
api_hash = 'fcd8c080125fad9062c9bc7d9cb2ca2d'  
source_channel = -1002279845213  
destination_bot = -1002304519486

# إنشاء عميل Telethon باستخدام الجلسة المخزنة
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    print(f"Received Message: {event.message.text}")  
    try:
        await client.send_message(destination_bot, event.message.text)  
    except Exception as e:
        print(f"Error sending message: {e}")

async def restart_client():
    while True:
        try:
            print("إعادة الاتصال بتليغرام...")
            await client.connect()
            if not await client.is_user_authorized():
                print("الجلسة غير مصرح بها، تأكد من تسجيل الدخول.")
                return
            print("تم الاتصال بنجاح!")
            await client.run_until_disconnected()
        except Exception as e:
            print(f"فشل الاتصال، إعادة المحاولة بعد 5 ثوانٍ... {e}")
            await asyncio.sleep(5)

print("البوت يعمل الآن...")
client.loop.run_until_complete(restart_client())