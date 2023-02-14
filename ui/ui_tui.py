from .ui_view import commands
from .ui_base_user_interface import UserInterface


class TUI(UserInterface):
    """Запуск приложения через текстовый пользовательский интерфейс"""
    def input_menu_item(self):
        """Вводит пункт меню"""
        menu_item = input("Введите команду: ")
        return menu_item if menu_item in commands.values() else self.input_menu_item()

    def input_note(self):
        """Вводит заметку"""
        header = input('Введите заголовок заметки: ')
        body = self.input_body_note()
        return header, body

    def input_note_id(self):
        """Вводит ID заметки"""
        try:
            return int(input('Введите ID заметки: '))
        except ValueError:
            self.input_note_id()

    def input_body_note(self):
        """Вводит содержимое заметки"""
        body = input('Введите тело заметки: ')
        return body

    def input_selection_notes_by_date(self):
        """Вводит даты для выборки заметок на заданном диапазоне"""
        start = input('Введите дату начало выборки в формате dd-mm-YYYY: ')
        end = input('Введите дату конец выборки в формате dd-mm-YYYY: ')

        return start, end
    