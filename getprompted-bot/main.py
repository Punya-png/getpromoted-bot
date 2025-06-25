from telegram.ext import Updater, CommandHandler

TOKEN = "YOUR_BOT_TOKEN_HERE"

def start(update, context):
    update.message.reply_text("👋 Welcome to GetPrompted!\nPool SOL. Pump Tokens. Get Rewarded.")

def contribute(update, context):
    update.message.reply_text("💸 Send 0.02 SOL to:\n`GBEScjuVndm4JzCBzTLudbvaAae9RZpQg2JuZTYPSNGy`", parse_mode='Markdown')

def help_command(update, context):
    update.message.reply_text("⚙️ *How it works:*\n1. Contribute 0.02 SOL\n2. When pool hits 10 SOL, we buy a token\n3. You get your share of pumped tokens!", parse_mode='Markdown')

def pool(update, context):
    update.message.reply_text("📊 Pool Progress:\nCurrently 7.4 / 10 SOL collected.")

def submitwallet(update, context):
    args = context.args
    if args:
        wallet = args[0]
        update.message.reply_text(f"✅ Wallet `{wallet}` received! You’ll be rewarded after the next pump.", parse_mode='Markdown')
    else:
        update.message.reply_text("❗ Please submit like this:\n`/submitwallet YOUR_WALLET_ADDRESS`", parse_mode='Markdown')

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("contribute", contribute))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("pool", pool))
dp.add_handler(CommandHandler("submitwallet", submitwallet, pass_args=True))

updater.start_polling()
updater.idle()