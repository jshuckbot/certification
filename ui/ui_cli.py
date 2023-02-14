from .ui_view import commands
from .ui_base_user_interface import UserInterface


class CLI(UserInterface):
    """Запуск приложения через интерфейс командной строки"""

    def input_menu_item(self):
        """Вводит пункт меню"""
        pass

    def input_note(self):
        """Вводит заметку"""
        pass

    def input_note_id(self):
        """Вводит ID заметки"""
        pass

    def input_body_note(self):
        """Вводит содержимое заметки"""
        pass

    def input_selection_notes_by_date(self):
        """Вводит даты для выборки заметок на заданном диапазоне"""
        pass
    