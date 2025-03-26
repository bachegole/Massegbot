from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توکن ربات را اینجا بگذارید
TOKEN = "7924601378:AAEk3KuqLTxpje7WOfxF_jDdQelkVV__ijU"
ADMIN_ID = 7993271989  # آیدی عددی تلگرام شما

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! پیام خود را ارسال کنید.")

async def forward_to_admin(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = f"📩 پیام جدید از {user.first_name} (@{user.username}):\n\n{update.message.text}"
    await context.bot.send_message(chat_id=ADMIN_ID, text=message)
    await update.message.reply_text("پیام شما ارسال شد!")

async def reply_to_user(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        user_info = update.message.reply_to_message.text.split("\n")[0]
        user_id = int(user_info.split()[3].strip("()"))
        await context.bot.send_message(chat_id=user_id, text=update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
app.add_handler(MessageHandler(filters.REPLY & filters.TEXT, reply_to_user))

print("ربات اجرا شد...")
app.run_polling()
