from note import Note
from file_writer import FileWriter
from selection_notes_by_date import SelectionNotesByDate


class ManagerNotes(FileWriter, SelectionNotesByDate):
    """Управляет заметками"""
    _notes = []

    def __init__(self):
        FileWriter.__init__(self)
        SelectionNotesByDate.__init__(self, self._notes)

    def __getitem__(self, id_number):
        """Ищет заметку в списке"""
        try:
            return self._notes[id_number - 1], f'Запись c id {id_number} найдена!'
        except IndexError:
            return f'Запись не найдена! Такого id {id_number} не существует!'

    def add(self, header, body):
        """Добавляет заметки в список"""
        self._notes.append(Note(header, body))

        return 'Запись успешно добавлена!'

    def edit_note(self, id_number, body):
        """Изменяет запись по id"""
        try:
            self._notes[id_number - 1].edit(body)
        except IndexError:
            return f'Запись не добавлена! Такого id {id_number} не существует!'

        return 'Запись успешно изменена!'

    def remove_note(self, id_number):
        """Удаляет заметку из списка"""
        try:
            self._notes.pop(id_number - 1)
        except IndexError:
            return f'Запись не возможно удалить! Такого id {id_number} не существует!'

        return f'Запись успешно удалена!'

    def get_notes(self):
        """Возвращает весь список заметок"""
        return self._notes, 'Заметки выведены на экран!' if len(self._notes) > 0 else 'Заметок в данный момент нет!'


if __name__ == '__main__':
    manager = ManagerNotes()
    manager.add('Завтрак', 'Каша манная, 200г воды')
    manager.add('Купить книгу', 'Книга по паттернам проектирования')
    manager.add('Сходить в кино', 'Вышел в прокат Аватар 2')

    # Проверка записи и чтения
    manager.write()
    manager.read()
