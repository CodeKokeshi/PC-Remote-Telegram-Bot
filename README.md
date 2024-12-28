# PC Remote Telegram Bot

🚀 **Control Your PC with Telegram!**  
Take screenshots or shut down your PC remotely using Telegram. Perfect for monitoring downloads or tracking progress when you’re away from your PC.

---

## 📖 Quick Start Guide

1. **Install Required Libraries:**  
   Install the following Python libraries:
   ```bash
   pip install pyautogui telebot
   pip install --upgrade Pillow PyAutoGUI
   ```

2. **Setup Your Telegram Bot:**
   - Get a Bot Token from Telegram’s [BotFather](https://core.telegram.org/bots#botfather).
   - Create a group chat and add your bot to the group.
   - Get your **Chat ID**:
     1. Send a message in the group.
     2. Open your browser and go to:
        ```
        https://api.telegram.org/bot<YourBOTToken>/getUpdates
        ```
        Replace `<YourBOTToken>` with your bot’s token. Find the `id` under `"chat"`.

3. **Declare Constants in Your Script:**
   ```python
   TELEGRAM_BOT_TOKEN = 'YourTelegramBotTokenHere'
   TELEGRAM_CHAT_ID = 'YourChatIDHere'
   ```

4. **Import Required Modules:**
   ```python
   import asyncio
   import pyautogui
   import telebot
   import subprocess
   ```

---

## 🛠 Features

### 📸 **Screenshot Commands:**
Control screenshot regions using commands:
- `/c` - Full screen
- `/c_tl` - Top Left
- `/c_tr` - Top Right
- `/c_br` - Bottom Right
- `/c_bl` - Bottom Left

Example:
```python
@bot.message_handler(commands=['c', 'c_tl', 'c_tr', 'c_br', 'c_bl'])
def capture_screenshot(message):
    # Define screenshot regions and capture logic
```

### 🔌 **Shutdown Command:**
Remotely shut down your PC by sending:
```bash
/shutdown -s -t <seconds>
```
Example:
```python
@bot.message_handler(commands=['shutdown'])
def shutdown_pc(message):
    # Parse shutdown time and execute the command
```

---

## ⚙️ Screenshot Logic
- Set regions for custom captures:
  ```python
  def set_region(left, top, width, height):
      # Configure region parameters
  ```
- Use `pyautogui` to capture screenshots.
- Send screenshots to Telegram:
  ```python
  screenshot = pyautogui.screenshot(region=(region_left, region_top, region_width, region_height))
  bot.send_photo(chat_id, open('screenshot.png', 'rb'))
  ```

---

## 🛡 Notes
- **Keep Bot Tokens Secret:** Never share your bot token publicly.
- **Use Responsibly:** Be cautious with remote shutdown commands.

---
