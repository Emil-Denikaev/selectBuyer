from aiogram.dispatcher.filters.state import StatesGroup, State

class Mailing(StatesGroup):
    Text = State()
    Send = State()