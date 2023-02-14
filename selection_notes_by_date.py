from datetime import timedelta, datetime


class SelectionNotesByDate:
    """Выбирка из диапазона дат"""
    def __init__(self, notes):
        self._notes = notes
        self.range_dates = []
        self.__notes_between_dates = []

    def __fill_list_range_dates(self, start_date, end_date):
        """Запоняет список подходящих дат для выборки"""
        # приводим строку к дате
        start = datetime.strptime(start_date, "%d-%m-%Y")
        end = datetime.strptime(end_date, "%d-%m-%Y")
        # Добавляем в спискок диапазон дат для выборки
        self.range_dates = [(start + timedelta(days=x)).date() for x in range(0, (end - start).days + 1)]

    def get_notes_in_between_dates(self, start_date, end_date):
        """Получает заметки из диапазона дат"""
        try:
            datetime.strptime(start_date, '%d-%m-%Y')
            datetime.strptime(end_date, '%d-%m-%Y')
        except:
            raise ValueError('Дата введена не коректна')

        self.__fill_list_range_dates(start_date, end_date)
        self.__notes_between_dates = [note for note in self._notes if note.get_date_create() in self.range_dates]

        return self.__notes_between_dates, \
            f'Сформированы заметки с {start_date} по {end_date} '\
            f'Всего записей: {len(self.__notes_between_dates)}'
