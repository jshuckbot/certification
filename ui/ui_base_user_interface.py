from abc import ABC, abstractmethod


class UserInterface(ABC):
    """Пользовательский интерфейс"""
    @abstractmethod
    def input_menu_item(self):
        """Вводит пункт меню"""
        pass

    @abstractmethod
    def input_note(self):
        """Вводит заметку"""
        pass

    @abstractmethod
    def input_note_id(self):
        """Вводит ID заметки"""
        pass

    @abstractmethod
    def input_body_note(self):
        """Вводит содержимое заметки"""
        pass

    @abstractmethod
    def input_selection_notes_by_date(self):
        """Вводит даты для выборки заметок на заданном диапазоне"""
        pass
    