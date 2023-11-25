from aiogram.dispatcher.filters.state import StatesGroup,State

class StateForChief(StatesGroup):
    username = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    result = State()

class StateForWorker(StatesGroup):
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    result = State()