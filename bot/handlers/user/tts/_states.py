from aiogram.filters.state import StatesGroup, State


class _TTSFSM(StatesGroup):
    send_speach = State()
    finish = State()


FSM = _TTSFSM
