from settings import mng  # FIXME


class StartMarkup:
    @staticmethod
    def commands():
        mng.add_keyboard('f', [['test']])
        return mng.keyboards['f']

# [ ] add lib.keyboard_builder


class RemindMarkup:
    @staticmethod
    def date():
        mng.add_keyboard('date', [['Сегодня', 'Завтра']],
                         placeholder='04.07.2022')
        return mng.keyboards['date']
