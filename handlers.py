from telegram import Update, ParseMode, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    update.message.reply_text(
        text=f'Assalomu alaykum {user.first_name}',
        # parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("Buyurtmalar berish", web_app=WebAppInfo("https://kun.uz"))
                ],
                [KeyboardButton("Buyurtmalarim"), KeyboardButton("Sozlamalar")],
                [KeyboardButton("Biz haqimizda"), KeyboardButton("Fikr qoldirish")],
                [
                    KeyboardButton("Contact Yuborish", request_contact=True),
                    KeyboardButton("Lokatsiya Yuborish", request_location=True)
                ]
            ],
            resize_keyboard=True,
            # one_time_keyboard=True
        )
    )


def order(update: Update, context: CallbackContext):
    update.message.reply_text("Sizda hali birorta ham buyurtma yo`q")


def settings(update: Update, context: CallbackContext):
    update.message.reply_text(
        "⚙️ Sozlamalar",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Tilni o'zgartish")],
                [KeyboardButton("Telefon raqingizni ozgartish")],
                [KeyboardButton("Orqaga")],
            ]
        ),
        reply_to_message_id=update.message.message_id
    )


def contact(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Telefon raqamni ozgartish",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mening raqamim", request_contact=True)],
                [KeyboardButton("Orqaga")],
            ]
        )
    )


def back(update: Update, context: CallbackContext):
    start(update, context)


def set_language(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Tilni tanlang",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton("Uzbek", callback_data="language:uz")],
                [InlineKeyboardButton("English", callback_data="language:en")],
                [InlineKeyboardButton("kanalga azo boling", url="https://t.me/+G-MNQt28Fek2MzFi")]
            ]
        )
    )


def choose_language(update: Update, context: CallbackContext):
    data = update.callback_query.data

    langs = {
        'uz': "O'zbek",
        'en': "ingliz"
    }

    _, lan = data.split(":")

    update.callback_query.message.reply_text(f"siz {langs[lan]} tilini tanladingiz")

def about_us(update: Update, context: CallbackContext):
    update.message.reply_text("📍 Biz shu yerda joylashganmiz")
    update.message.reply_text(
        text='📧 Email yozish uchun <a href="mailto:example@gmail.com">bu yerga bosing</a>',
        parse_mode=ParseMode.MARKDOWN
    )

def comment(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""*Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning*.

Biz sizning fikr-mulohazalaringizni juda qadrlaymiz! Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin""",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga")]
            ],
            resize_keyboard=True
        )   
    )