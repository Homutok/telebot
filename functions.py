import telebot
import datetime
import pandas as pd
import json
from data import timeSchedule,evenNotEven,weekDays

bot = telebot.TeleBot('1725064514:AAE06_z5wpqGJ9fBz0dHpwU_r0_jVQtX81A')
def classScheduleView(message,subGroupID,purpose):
    if(datetime.datetime.now().isocalendar()[2]==7):
        photo = open('.\image\Sunday2.png', 'rb')
        bot.send_photo(message.chat.id, photo, )
        return
    data = pd.read_excel('.\source\classSchedule.xls', sheet_name='schedule')
    datalinks= pd.read_excel('.\source\classSchedule.xls', sheet_name='link')
    datenow=datetime.datetime.now().strftime("%H:%M")
    bufferOFweek=evenNotEven+subGroupID
    iterate=1
    for timehour in timeSchedule:
        iterate += 1

        if (timehour[0].strftime('%H:%M') <= datenow) and (timehour[1].strftime('%H:%M') >= datenow):
            if(bufferOFweek==0):
                try:
                    if(purpose==1):
                        isScheduleBuf = json.loads(data.to_json(orient='records'))[iterate+1][weekDays[datetime.datetime.now().isocalendar()[2] - 1]]
                        ifelseforScheuld(isScheduleBuf, message, datalinks)
                    else:
                        isScheduleBuf=json.loads(data.to_json(orient='records'))[iterate][weekDays[datetime.datetime.now().isocalendar()[2]-1]]
                        ifelseforScheuld(isScheduleBuf, message,datalinks)
                except:
                    bot.send_message(message.chat.id, 'Пар нет')
            else:
                try:
                    if (purpose == 1):
                        isScheduleBuf = json.loads(data.to_json(orient='records'))[iterate+1][weekDays[datetime.datetime.now().isocalendar()[2]-1]+'.'+str(bufferOFweek)]
                        ifelseforScheuld(isScheduleBuf, message,datalinks)
                    else:
                        isScheduleBuf = json.loads(data.to_json(orient='records'))[iterate][weekDays[datetime.datetime.now().isocalendar()[2] - 1] + '.' + str(bufferOFweek)]
                        ifelseforScheuld(isScheduleBuf, message, datalinks)
                except:
                    bot.send_message(message.chat.id, 'Пар нет')
            break
    if iterate >= 9:
        NoneView(message)

    return

def linksView(message):
    data = pd.read_excel('.\source\classSchedule.xls', sheet_name='links')
    indx=0
    while indx<len(data.columns.ravel()):
        bufferString=str(data[data.columns.ravel()[indx]].tolist())[2:(len(data[data.columns.ravel()[indx]].tolist())-3)]
        bot.send_message(message.chat.id, ''+str(data.columns.ravel()[indx])+'\n'+bufferString)
        indx = indx + 1;
    return
def NoneView(message):
    bot.send_message(message.chat.id, 'Никакая пара не идет, потому отдыхай ')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICOGBU9B7XzIfEtmWe1mHpmzjZvogTAAKLAgACVp29Cve0YiYNjzvzHgQ')
    return
def ifelseforScheuld(isScheduleBuf,message,datalinks):
    if (isScheduleBuf == None):
        NoneView(message)
    else:
        bot.send_message(message.chat.id, 'Сейчас идет ' + str(isScheduleBuf))
        bot.send_message(message.chat.id,json.loads(datalinks.to_json(orient='records'))[0][str(isScheduleBuf)])
    return
def labView(message):
    bot.send_message(message.chat.id, 'В общем ситуация такая... ')
    return
def thx(message,hideboard,keyboardHelper):
    bot.send_message(message.chat.id, 'Понял', reply_markup=hideboard)
    bot.send_message(message.chat.id, 'Хорошо. Что ты хочешь узнать ?', reply_markup=keyboardHelper)
    return
def allClassScheduleView(message):
    if (datetime.datetime.today().isoweekday() == 1):
        photo = open('.\image\Monday.png', 'rb')
    if (datetime.datetime.today().isoweekday() == 2):
        photo = open('.\image\Tuesday.png', 'rb')
    if (datetime.datetime.today().isoweekday() == 3):
        photo = open('.\image\Wednesday.png', 'rb')
    if (datetime.datetime.today().isoweekday() == 4):
        photo = open('.\image\Thursday.png', 'rb')
    if (datetime.datetime.today().isoweekday() == 5):
        photo = open('.\image\Friday.png', 'rb')
    if (datetime.datetime.today().isoweekday() == 6):
        photo = open('.\image\Saturday.png', 'rb')
    if (datetime.datetime.today().isoweekday() == 7):
        photo = open('.\image\Sunday.png', 'rb')
    bot.send_photo(message.chat.id, photo, )
    return