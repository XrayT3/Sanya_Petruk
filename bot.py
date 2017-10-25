# -*- coding: utf-8 -*-?
import telebot
import time

import requests.exceptions as r_exceptions
from requests import ConnectionError

import const, markups, config, base

bot = telebot.TeleBot(const.token)


# Обработка /start команды - выдача клавиатуры
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['FAQ']])
    text = message.text.split(" ")
    if len(text) == 2:
        if text[1].isdigit():
            initial_id = text[1]
            base.addInvitation(initial_id, int(message.chat.id))
    base.add_user(message)
    if not base.is_admin(message.chat.id):
        bot.send_message(message.chat.id, const.welcome, parse_mode='HTML', reply_markup=markups.start())
        bot.send_message(message.chat.id, "<i>CryptoInsideBot Info<i/>", parse_mode='HTML', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, const.welcome, parse_mode='HTML', reply_markup=markups.start_admin())
        bot.send_message(message.chat.id, "<i>CryptoInsideBot Info</i>", parse_mode='HTML', reply_markup=keyboard)


@bot.message_handler(regexp="Админ-панель")
def admin(message):
    if not base.is_admin(message.chat.id):
        bot.send_message(message.chat.id, const.access)
    else:
        bot.send_message(message.chat.id, "Админ-панель", reply_markup=markups.admin_panel())


# Выдача пакетов
@bot.message_handler(regexp='Оплата')
def client_panel(message):
    keyboard4 = telebot.types.InlineKeyboardMarkup()
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅Test Drive']])
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅VIP']])
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅VIP + ПАМПЫ']])
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅Обучение']])
    bot.send_message(message.chat.id, const.paket_0, reply_markup=keyboard4)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    markup1 = telebot.types.InlineKeyboardMarkup()
    btn_back = telebot.types.InlineKeyboardButton(text="Получить реквизиты", callback_data='buy_1')
    markup1.add(btn_back)

    markup2 = telebot.types.InlineKeyboardMarkup()
    btn_back = telebot.types.InlineKeyboardButton(text="Получить реквизиты", callback_data='buy_2')
    markup2.add(btn_back)

    markup3 = telebot.types.InlineKeyboardMarkup()
    btn_back = telebot.types.InlineKeyboardButton(text="Получить реквизиты", callback_data='buy_3')
    markup3.add(btn_back)

    markup4 = telebot.types.InlineKeyboardMarkup()
    btn_back = telebot.types.InlineKeyboardButton(text="Получить реквизиты", callback_data='buy_4')
    markup4.add(btn_back)

    keyboard2 = telebot.types.InlineKeyboardMarkup()
    keyboard2.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['FAQ']])

    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Скрыть']])

    keyboard4 = telebot.types.InlineKeyboardMarkup()
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅Test Drive']])
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅VIP']])
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅VIP + ПАМПЫ']])
    keyboard4.add(*[telebot.types.InlineKeyboardButton(text=name, callback_data=name) for name in ['✅Обучение']])
    if c.data == 'FAQ':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                              text=const.FAQ, parse_mode='html', reply_markup=keyboard1)

    if c.data == '✅Test Drive':
        bot.edit_message_text(const.paket_1, chat_id=c.message.chat.id, message_id=c.message.message_id,
                              reply_markup=markup1)

    if c.data == '✅VIP':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                                  text=const.paket_2, reply_markup=markup2)

    if c.data == '✅VIP + ПАМПЫ':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                                  text=const.paket_3, reply_markup=markup3)

    if c.data == '✅Обучение':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                                  text=const.paket_4, reply_markup=markup4)

    if c.data == 'Назад':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                                  text='Выберите пакет', reply_markup=keyboard4)

    if c.data == 'buy_1':
        bot.send_message(c.message.chat.id, "✅Отправьте мне точно 0.012 BTC (без учета комиссии) "
                          "на кошелек 🔹1LZwYT81XJvKxk48utNEKqgAxkBH913t37 🔹  \n"
                          "❗️Если я получу сумму меньшую или большую чем 0.012 BTC - активацию нужно будет проводить в ручном порядке. \n"
                          "✅Ваша подписка будет автоматически активирована после одного подтверждения в сети BitCoin, "
                          "я Вас уведомлю об этом. Скорость получения подписки зависит от установленной Вами комиссии "
                          "транзакции. При возникновении длительных задержек, проблем или вопросов, свяжитесь "
                          "с технической поддержкой.", reply_markup=markups.buy_0())

    if c.data == 'buy_2':
        bot.send_message(c.message.chat.id, "✅Отправьте мне точно 0.02 BTC (без учета комиссии) "
                          "на кошелек 🔹1LZwYT81XJvKxk48utNEKqgAxkBH913t37 🔹  \n"
                          "❗️Если я получу сумму меньшую или большую чем 0.02 BTC - активацию нужно будет проводить в ручном порядке. \n"
                          "✅Ваша подписка будет автоматически активирована после одного подтверждения в сети BitCoin, "
                          "я Вас уведомлю об этом. Скорость получения подписки зависит от установленной Вами комиссии "
                          "транзакции. При возникновении длительных задержек, проблем или вопросов, свяжитесь "
                          "с технической поддержкой.", reply_markup=markups.buy_0())

    if c.data == 'buy_3':
        bot.send_message(c.message.chat.id, "✅Отправьте мне точно 0.04 BTC (без учета комиссии) "
                          "на кошелек 🔹1LZwYT81XJvKxk48utNEKqgAxkBH913t37 🔹  \n"
                          "❗️Если я получу сумму меньшую или большую чем 0.04 BTC - активацию нужно будет проводить в ручном порядке. \n"
                          "✅Ваша подписка будет автоматически активирована после одного подтверждения в сети BitCoin, "
                          "я Вас уведомлю об этом. Скорость получения подписки зависит от установленной Вами комиссии "
                          "транзакции. При возникновении длительных задержек, проблем или вопросов, свяжитесь "
                          "с технической поддержкой.", reply_markup=markups.buy_0())

    if c.data == 'buy_4':
        bot.send_message(c.message.chat.id, "✅Отправьте мне точно 0.01 BTC (без учета комиссии) "
                          "на кошелек 🔹1LZwYT81XJvKxk48utNEKqgAxkBH913t37 🔹  \n"
                          "❗️Если я получу сумму меньшую или большую чем 0.01 BTC - активацию нужно будет проводить в ручном порядке. \n"
                          "✅Ваша подписка будет автоматически активирована после одного подтверждения в сети BitCoin, "
                          "я Вас уведомлю об этом. Скорость получения подписки зависит от установленной Вами комиссии "
                          "транзакции. При возникновении длительных задержек, проблем или вопросов, свяжитесь "
                          "с технической поддержкой.", reply_markup=markups.buy_0())

    if c.data == 'Скрыть':
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,
                                  text='<i>CryptoInsideBot Info</i>', parse_mode='html', reply_markup=keyboard2)

    if c.data == 'Рассылка для клиентов':
        msg = bot.send_message(c.message.chat.id, "Введите текст, который хотите отправить всем клиентам")
        bot.register_next_step_handler(msg, send_to_clients)

    if c.data == "Рассылка не для клиентов":
        msg = bot.send_message(c.message.chat.id, "Введите текст, который хотите отправить всем не клиентам")
        bot.register_next_step_handler(msg, send_to_non_clients)

    if c.data == 'Пользователи':
        users = base.get_all_users()
        txt = 'Админ-панель\n\n'
        for user in users:
            who_inv = base.who_invited(user[1])
            txt = txt + "{n}. @{username}\n".format(n=user[0], username=user[4])
            if who_inv:
                txt = txt + "    Приглашен пользователем: {who_inv}\n".format(who_inv=who_inv)
            if user[8] == "TRUE":
                txt = txt + "    Статус: ОПЛАТИЛ\n\n"
            else:
                txt = txt + "    Статус: НЕ ОПЛАТИЛ\n\n"
        bot.edit_message_text(txt, c.message.chat.id, c.message.message_id, reply_markup=markups.admin_panel())

    if c.data == 'Добавить клиента':
        bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id,
                                      reply_markup=telebot.types.ReplyKeyboardMarkup())
        msg = bot.send_message(c.message.chat.id, "Введите username клиента, которого нужно добавить")
        bot.register_next_step_handler(msg, add_client)

    if c.data == 'Удалить клиента':
        bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id,
                                      reply_markup=telebot.types.ReplyKeyboardMarkup())
        msg = bot.send_message(c.message.chat.id, "Введите username клиента, которого нужно удалить")
        bot.register_next_step_handler(msg, del_client)

    if c.data == 'welcome':
        if not base.is_admin(c.message.chat.id):
            bot.send_message(c.message.chat.id, const.welcome, reply_markup=markups.start())
        else:
            bot.send_message(c.message.chat.id, const.welcome, reply_markup=markups.start_admin())


def send_to_clients(message):
    count = 0
    for user in base.get_all_users():
        if user[8] == 'TRUE':
            count += 1
            if user[1] == const.admin_id:
                continue
            if count % 20 == 0:
                time.sleep(1)
            markup = telebot.types.InlineKeyboardMarkup()
            back = telebot.types.InlineKeyboardButton(text="Назад в меню", callback_data="welcome")
            text = "Вернуться"
            markup.add(back)
            try:
                bot.send_message(user[1], message.text)
                #bot.send_message(user[1], "<b>%s</b>" % text, reply_markup=markup, parse_mode="html")

                print("message sent to %s count = %s" % (user[1], count))
            except Exception as e:
                continue
    print(count)
    bot.send_message(message.chat.id, "Сообщение успешно отправлено всем клиентам!",
                     reply_markup=markups.admin_panel())


def send_to_non_clients(message):
    count = 0
    for user in base.get_all_users():
        if user[8] == 'FALSE':
            count += 1
            print(count)
            if user[1] == const.admin_id:
                continue
            if count % 20 == 0:
                time.sleep(1)
            markup = telebot.types.InlineKeyboardMarkup()
            back = telebot.types.InlineKeyboardButton(text="Назад в меню", callback_data="welcome")
            text = "Вернуться"
            markup.add(back)
            try:
                bot.send_message(user[1], message.text)
                #bot.send_message(user[1], "<b>%s</b>" % text, reply_markup=markup, parse_mode="html")

                print("message sent to %s count = %s" % (user[4], count))
            except Exception as e:
                continue
    bot.send_message(message.chat.id, "Сообщение успешно отправлено всем тем, кто не является клиентами!",
                     reply_markup=markups.admin_panel())


def add_client(c):
    status = base.true_pay(c.text)
    if status:
        bot.send_message(c.chat.id, "Готово!")
    else:
        print("ERR : client not in DB")
        bot.send_message(c.chat.id, "Такого клиента нет в базе данных")
    bot.send_message(c.chat.id, "Админ-панель", reply_markup=markups.admin_panel())


def del_client(c):
    status = base.false_pay(c.text)
    if status:
        bot.send_message(c.chat.id, "Готово!")
    else:
        print("ERR : client not in DB")
        bot.send_message(c.chat.id, "Такого клиента нет в базе данных")
    bot.send_message(c.chat.id, "Админ-панель", reply_markup=markups.admin_panel())


@bot.message_handler(regexp="✅Я оплатил")
def buy(message):
    if not base.is_admin(message.chat.id):
        bot.send_message(message.chat.id, "Отлично ❗️\n"
                                          "✅ Напишите в личные сообщения @Crypto_Boss и укажите id траназакции ТЕКСТОМ, "
                                          "после чего вы будете добавлены в канал.",
                         reply_markup=markups.start())
    else:
        bot.send_message(message.chat.id, "Отлично ❗️\n"
                                      "✅ Напишите в личные сообщения @Crypto_Boss и укажите id траназакции ТЕКСТОМ, "
                                      "после чего вы будете добавлены в канал.",
                         reply_markup=markups.start_admin())


# Партнерская программа
@bot.message_handler(regexp="💎Партнерам")
def referalka(message):
    bot.send_message(message.chat.id, const.partnerka + 'У вас рефералов: {0}\n'
                                      'Ваша реферальная ссылка:'
                                      ' https://t.me/Client_Test_bot?start={1}'.format(*base.getValuesPartnership(message.chat.id)))


# Выдача всей необходимой информации
@bot.message_handler(regexp='О нас')
def about_us(message):
    bot.send_message(message.chat.id, const.about, parse_mode='html')


# Прием писем в тех. поддержку
@bot.message_handler(regexp='🛠Техподдержка')
def settings(message):
    sent = bot.send_message(message.chat.id, 'Опиши свою проблему')
    bot.register_next_step_handler(sent, help)


def help(message):
    if (message.text != "📡Оплата") and (message.text != "💎Партнерам") and (message.text != "🛠Техподдержка") and \
            (message.text != "🏦О нас") and (message.text != "Админ-панель"):
        bot.send_message(const.help_id, '{name}'.format(name=message.text))
        bot.send_message(const.help_id, 'Никнейм: @' + str(message.from_user.username))
        bot.send_message(message.chat.id, 'Ваше письмо принято')


# Запуск бота
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except ConnectionError as expt:
        config.log(Exception='HTTP_CONNECTION_ERROR', text=expt)
        print('Connection lost..')
        time.sleep(30)
        continue
    except r_exceptions.Timeout as exptn:
        config.log(Exception='HTTP_REQUEST_TIMEOUT_ERROR', text=exptn)
        time.sleep(5)
        continue
