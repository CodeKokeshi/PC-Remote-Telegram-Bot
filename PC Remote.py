import asyncio
import pyautogui
import telebot
import subprocess

TELEGRAM_BOT_TOKEN = 'Your Telegram Bot Token Here.'

TELEGRAM_CHAT_ID = 'Your Chat ID here.'

region_left = 0
region_top = 0
region_width = 1920
region_height = 1080

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['c', 'c_tl', 'c_tr', 'c_br', 'c_bl'])
def capture_screenshot(message):
    command = message.text.split('_')[-1].lower()

    if command == 'tl':
        set_region(0, 0, 930, 560)
    elif command == 'tr':
        set_region(930, 0, 990, 560)
    elif command == 'br':
        set_region(930, 560, 990, 520)
    elif command == 'bl':
        set_region(0, 560, 930, 520)
    else:
        set_region(0, 0, 1920, 1080)

    asyncio.run(take_screenshot_and_send(message.chat.id))


def set_region(left, top, width, height):
    global region_left, region_top, region_width, region_height
    region_left = left
    region_top = top
    region_width = width
    region_height = height


async def take_screenshot_and_send(chat_id):
    for _ in range(3):
        try:
            screenshot = pyautogui.screenshot(region=(region_left, region_top, region_width, region_height))
            screenshot.save('screenshot.png')

            with open('screenshot.png', 'rb') as photo:
                bot.send_photo(chat_id, photo, disable_notification=True)

            break
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(5)


@bot.message_handler(commands=['shutdown'])
def shutdown_pc(message):
    try:
        command_parts = message.text.split(' ')
        if len(command_parts) == 4 and command_parts[1] == '-s' and command_parts[2] == '-t':
            shutdown_time = int(command_parts[3])
            asyncio.run(shutdown_with_timer(shutdown_time, message.chat.id))
        else:
            bot.reply_to(message, "Invalid shutdown command format. Please use: /shutdown -s -t <seconds>")
    except Exception as e:
        print(f"Error: {e}")


def shutdown_with_timer(seconds, chat_id):
    try:
        bot.send_message(chat_id, f"Shutting down PC in {seconds} seconds.")
        asyncio.sleep(seconds)
        subprocess.run(['shutdown', '/s', '/t', str(seconds)])
    except Exception as e:
        print(f"Error during shutdown: {e}")


async def main():
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.get_event_loop().create_task(main())
    bot.polling(none_stop=True, interval=0, timeout=43200)
