# -*- coding: utf-8 -*-?
import telebot


def start():
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("📡Оплата", "💎Партнерам")
    markup.row("🛠Техподдержка", "🏦О нас")
    return markup


def start_admin():
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("📡Оплата", "💎Партнерам")
    markup.row("🛠Техподдержка", "🏦О нас")
    markup.row("Админ-панель")
    return markup


def buy_0():
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("✅Я оплатил")
    #markup.row("Назад")
    return markup


def admin_panel():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    kl_rass = telebot.types.InlineKeyboardButton(text="Рассылка_1", callback_data='Рассылка для клиентов')
    nkl_rass = telebot.types.InlineKeyboardButton(text="Рассылка_0", callback_data='Рассылка не для клиентов')
    users = telebot.types.InlineKeyboardButton(text="Пользователи", callback_data='Пользователи')
    add_client = telebot.types.InlineKeyboardButton(text="Добавить клиента", callback_data='Добавить клиента')
    del_client = telebot.types.InlineKeyboardButton(text="Удалить клиента", callback_data='Удалить клиента')
    markup.row(users)
    markup.row(kl_rass, nkl_rass)
    markup.row(add_client, del_client)
    return markup

