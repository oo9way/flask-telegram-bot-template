from telegram import ReplyKeyboardRemove

import states
from keyboards.replies import get_gender_keyboard


def get_name(update, context):
    text = update.message.text

    if len(text.split()) < 2:
        message = "Iltimos, ism va familiyangizni kiriting"
        update.message.reply_text(message)
        return states.NAME

    first_name, last_name, *_ = text.split()

    if len(first_name) < 5 or len(last_name) < 5:
        message = "Xato malumot,iltimos, ism va familiyangizni kiriting"
        update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
        return states.NAME

    context.user_data["name"] = text
    update.message.reply_text("Yoshizni kiriting", reply_markup=ReplyKeyboardRemove())
    return states.AGE


def invalid_name(update, context):
    update.message.reply_text("Iltimos, ismizni matn sifatida kiriting", reply_markup=ReplyKeyboardRemove())
    return states.NAME


def get_age(update, context):
    text = update.message.text

    # Validators
    if len(text.split()) != 1:
        message = "Iltimos, faqat yoshizni son sifatida kiriting"
        update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
        return states.AGE

    try:
        age = int(text)
    except ValueError:
        message = "Iltimos, faqat yoshizni son sifatida kiriting"
        update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
        return states.AGE

    if age < 18 or age > 60:
        message = "Xatolik, yosh chegarasi 18 va 60 yosh"
        update.message.reply_text(message, reply_markup=ReplyKeyboardRemove())
        return states.AGE
    # End validators
    context.user_data["age"] = age
    update.message.reply_text("Iltimos, jinsingizni tanlang.", reply_markup=get_gender_keyboard())
    return states.GENDER


def get_gender(update, context):
    text = update.message.text
    if text == "Ortga":
        update.message.reply_text("Yoshizni kiriting", reply_markup=ReplyKeyboardRemove())
        return states.AGE

    if text != "Male" and text != "Female":
        update.message.reply_text("Iltimos, jinsingizni tugma orqali tanlang", reply_markup=get_gender_keyboard())
        return states.GENDER

    context.user_data["gender"] = text
    update.message.reply_text("Manzilni kiriting", reply_markup=ReplyKeyboardRemove())
    return states.ADDRESS


def invalid_gender(update, context):
    update.message.reply_text("Iltimos, jinsingizni tugma orqali tanlang")
    return states.GENDER


def invalid_age(update, context):
    update.message.reply_text("Iltimos, yoshizni matn sifatida kiriting")
    return states.AGE


def get_address(update, context):
    from dispatcher import bot

    text = update.message.text
    context.user_data["address"] = text
    update.message.reply_text("Siz muvaffaqiyatli ro'yxatdan o'tdingiz", reply_markup=ReplyKeyboardRemove())
    message = "Malumotlaringiz\n"
    message += f"Ism: {context.user_data.get('name', 'Topilmadi')}\n"
    message += f"Yosh: {context.user_data.get('age', 'Topilmadi')}\n"
    message += f"Manzil: {context.user_data.get('address', 'Topilmadi')}\n"
    message += f"Jins: {context.user_data.get('gender', 'Topilmadi')}\n"
    update.message.reply_text(message)
    bot.send_message(chat_id=1921103181, text=message)
    return states.END


def invalid_address(update, context):
    update.message.reply_text("Iltimos, manzilni matn sifatida kiriting")
    return states.ADDRESS


def echo(update, context):
    update.message.reply_text(update.message.text)
