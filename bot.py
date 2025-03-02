from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram Bot Token
TOKEN = "7938292244:AAFLHrgypxqyIxyKayzphmYCJQMYQxLnXOE"

# /start komutu için fonksiyon
def start(update: Update, context: CallbackContext):
    mesaj = (
        "🌙 Merhaba! Ben Namaz Vakitleri Botuyum. \n\n"
        "📌 Kullanabileceğin komutlar:\n"
        "➡ /imsak Şehir\n"
        "➡ /sabah Şehir\n"
        "➡ /öğle Şehir\n"
        "➡ /ikindi Şehir\n"
        "➡ /akşam Şehir\n"
        "➡ /yatsı Şehir\n"
        "➡ /iftar Şehir\n"
        "➡ /sahur Şehir\n\n"
        "Örnek kullanım: `/akşam İstanbul`\n"
        "Hangi şehrin namaz vakitlerini öğrenmek istiyorsan, yukarıdaki komutları kullanabilirsin! 🕌"
    )
    update.message.reply_text(mesaj)

# Botu başlatma fonksiyonu
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))  # /start komutu için
    dp.add_handler(CommandHandler(["imsak", "sabah", "öğle", "ikindi", "akşam", "yatsı", "iftar", "sahur"], handle_namaz, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
