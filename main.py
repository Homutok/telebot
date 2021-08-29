import telebot
import functions
import token
#разная инициаизация
bot = telebot.TeleBot(token)
keyboardHelper =  telebot.types.ReplyKeyboardMarkup(True, True)
keyboardSubgroup= telebot.types.ReplyKeyboardMarkup(True, True)
keyboardFiles= telebot.types.ReplyKeyboardMarkup(True, True)
keyboardContinueСouple= telebot.types.ReplyKeyboardMarkup(True, True)
hideboard=telebot.types.ReplyKeyboardRemove()

#переменные которые не поместил в файл
keyboardHelper.row('Что за пара ?','Учебный материал','Расписание на сегодня')
keyboardFiles.row('Лабы','Лекции','Ссылки')
keyboardSubgroup.row('1 Подгруппа','2 Подгруппа')
keyboardContinueСouple.row('Следующая пара ?','Спасибо')
subGroupIDs=0
#получение даты
@bot.message_handler(commands=['start'])
def start_message(message):
                bot.send_message(message.chat.id, 'Привет, '+message.from_user.first_name+', какая подгруппа ? ',reply_markup=keyboardSubgroup)
@bot.message_handler(commands=['help'])
def start_message(message):
        bot.send_message(message.chat.id, 'Я помогаю тебе в учебе, в плане того, что облегчаю чуть-чуть ее \nЯ помогу понять, что за пара сейчас идет \nУзнать методический материал и т.д. \nЧто бы начать, введи /start')
@bot.message_handler(content_types=['text'])
def send_text(message):
        global subGroupIDs
        if message.text.lower() == 'что за пара ?':
                functions.classScheduleView(message,subGroupIDs,0);
                bot.send_message(message.chat.id, 'Воть', reply_markup=hideboard)
                bot.send_message(message.chat.id, '...', reply_markup=keyboardContinueСouple)
        elif message.text.lower() == 'расписание на сегодня': functions.allClassScheduleView(message)
        elif message.text.lower() == '1 подгруппа':
                subGroupIDs = 0
                functions.thx(message, hideboard, keyboardHelper)
        elif message.text.lower() == '2 подгруппа':
                subGroupIDs = 2
                functions.thx(message, hideboard, keyboardHelper)
        elif message.text.lower() == 'ссылки':functions.linksView(message);functions.thx(message, hideboard, keyboardHelper)
        elif message.text.lower() == 'следующая пара ?':
                functions.classScheduleView(message,subGroupIDs,1);
                functions.thx(message, hideboard, keyboardHelper)
        elif message.text.lower() == 'спасибо':
                functions.thx(message, hideboard, keyboardHelper)
        elif message.text.lower() == 'учебный материал':
                bot.send_message(message.chat.id, 'Понял', reply_markup=hideboard)
                bot.send_message(message.chat.id,'Вот, смотри: ', reply_markup=keyboardFiles)
        elif message.text.lower() == 'лабы' or message.text.lower() == 'лекции':
                bot.send_message(message.chat.id,'Сорян, мне пока лень( \nЕсли надо то мб сделаю, когда нибудь)\nНо ты можешь посмотреть тут: \nhttps://t.me/ivt1318')
                functions.thx(message, hideboard, keyboardHelper)
        else: bot.send_message(message.chat.id, 'Я тебя не понимаю( ')
@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
        sticker_id = message.sticker.file_id
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAOIYFIBbOWqqjky7PCsg0SZiu5zaOkAAgkAA_-Csh7FNgcIzGYNLB4E')
        bot.send_message(message.chat.id, 'Я тоже так могу))) ')
        bot.send_sticker(message.chat.id, sticker_id)

bot.polling()


