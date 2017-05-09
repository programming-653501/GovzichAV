import telebot
from texts import intro
from telebot import types
from find_places import info_about_place, open_hours, address_info, rating_info
from keys import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def instruction_to_bot(message):
    bot.send_message(message.chat.id, text=intro)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    global places
    while 1:
        try:
            places = info_about_place(query.query, query.location.latitude, query.location.longitude)
        except AttributeError:
            pass
        else:
            break
    i = 0
    i_place = []
    for place in places['results']:
        n_id = str(i)
        print(place)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Время работы', callback_data='t'+place['place_id']))
        keyboard.add(types.InlineKeyboardButton('Рейтинг', callback_data='s' + place['place_id']))
        i_place.append(types.InlineQueryResultVenue(
                id=n_id, title=place['name'], latitude=place['geometry']['location']['lat'],
                longitude=place['geometry']['location']['lng'], address=address_info(place['place_id']),
                reply_markup=keyboard
        ))
        i += 1
    bot.answer_inline_query(query.id, i_place)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data[0] == 't':
        bot.send_message(chat_id=call.from_user.id, text=open_hours(call.data))
    if call.data[0] == 's':
        bot.send_message(chat_id=call.from_user.id, text=rating_info(call.data))


if __name__ == '__main__':
    bot.polling(none_stop=True)
