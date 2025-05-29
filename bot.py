import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 把这里替换成你的真实密钥
TELEGRAM_BOT_TOKEN = 'OPENAI_API_KEY'
OPENAI_API_KEY = 'TELEGRAM_BOT_TOKEN'

openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

# /start 指令处理器
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("你好！我是 ChatGPT Bot，有什么我可以帮你的吗？")

# 普通消息处理器
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response['choices'][0]['message']['content']
    await update.message.reply_text(reply)

# 程序入口
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot 已启动，等待消息中...")
    app.run_polling()
