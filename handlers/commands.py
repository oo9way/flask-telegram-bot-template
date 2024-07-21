import states


def start(update, context):
    message = "Ismizni kiriting"
    update.message.reply_text(message)
    return states.NAME


def help(update, context):
    message = "Bot haqida ma'lumot\n/start - Botni boshlash\n/help - Bu bot haqida xabar\n/subscribe - Obunani boshlash"
    update.message.reply_text(message)


def subscribe(update, context):
    update.message.reply_text("Obuna !")


def info(update, context):
    update.message.reply_text("Salom!")


def error(update, context):
    update.message.reply_text("Botda xatolik vujudga keldi, biz buni ustida ishlayapmiz")