import asyncio
from datetime import datetime, timezone, timedelta
from typing import Awaitable, Any
from typing import Tuple


class Task:
    def __init__(self, func: Awaitable, args: list[Any] = None) -> None:
        self.__func = func
        self.__args = args

    async def run(self) -> None:
        if self.__args:
            await self.__func(*self.__args)
        else:
            await self.__func()


class Schedule:
    __tasks: list[Tuple[Task, datetime]] = []

    @classmethod
    def add_task(cls, task: Task, time: datetime) -> None:
        cls.__tasks.append((task, time))

    @staticmethod
    def __get_now_timestamp_with_tz(tz: timezone) -> float:
        return datetime.strptime(
            datetime.now(tz).strftime('%d.%m.%Y_%H:%M'),
            '%d.%m.%Y_%H:%M'
        ).timestamp()

    @classmethod
    async def __check_if_task_now(
            cls, tz: timezone = timezone(timedelta(hours=6.0))
    ) -> None:
        for task, time in cls.__tasks:
            if time.timestamp() <= cls.__get_now_timestamp_with_tz(tz):
                await task.run()
                cls.__tasks.remove((task, time))

    @classmethod
    async def __dispatcher(cls, delay=5) -> None:
        while True:
            await cls.__check_if_task_now()
            await asyncio.sleep(delay)

    @classmethod
    async def on_startup(cls):
        asyncio.create_task(cls.__dispatcher())
