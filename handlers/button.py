from packages.aiogram import types


def btn(state):
    btn_yes = types.InlineKeyboardButton(text='Да',callback_data=f'yes_{state}')
    btn_no = types.InlineKeyboardButton(text='Нет',callback_data=f'no_{state}')
    btn_dont_know = types.InlineKeyboardButton(text='Незнаю',callback_data=f'dont_know_{state}')
    return btn_yes,btn_no,btn_dont_know
def markup_generate(btns,row_width=1):
    markup = types.InlineKeyboardMarkup(row_width=row_width)
    markup.add(*btns)
    return markup

btn_my_workers = types.InlineKeyboardButton(text='Мои сотрудники',callback_data='my_workers')
btn_add_worker = types.InlineKeyboardButton(text='Добавить',callback_data='add_worker')

btn_start_for_worker = types.InlineKeyboardButton(text='Начать',callback_data='questions_for_worker')
btn_start_for_chief = types.InlineKeyboardButton(text='Начать',callback_data='questions_for_chief')