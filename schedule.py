import asyncio
from bot_config import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram
import manage
import datetime

data = ['test1', 'test2']


class Schedule:
    def __init__(self):
        self.tasks = []

    def add_task(self, func):
        self.tasks.append(func)

    async def scheduler(self):
        while True:
            print(datetime.datetime.now())
            for text in data:
                await bot.send_message(manage.admins[0], text)
            await asyncio.sleep(5)

    async def on_startup(self, dp):
        asyncio.create_task(self.scheduler())

    def start(self):
        pass


# bot handlers
async def init(message: aiogram.types.Message):
    await message.answer('Write your remind name')
    bot.add_state_handler(FSM.get_name, get_name)
    await FSM.get_name.set()


async def get_name(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    data.append(message.text)
    await message.answer('Updated')


class FSM(StatesGroup):
    get_name = State()


if __name__ == '__main__':
    sch = Schedule()
    bot.add_command_handler('set', init)
    bot.start(on_startup=sch.on_startup)
