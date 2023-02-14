import sys
from .ui_selector_menu import SelectorMenu
from manager_notes import ManagerNotes
from .ui_view import View, commands
from .ui_input import Input


class Controller(SelectorMenu):
    """Контроллер для запуска приложения"""
    def __init__(self):
        self._manager = ManagerNotes()
        self._view = View()
        self.choice_interface_launch_app()

    def run(self):
        """Запускает приложение заметок"""
        while self._view.menu_item != commands['EXIT']:
            self._view.show_menu()
            self._view.menu_item = self._input_interface.input_menu_item()
            self._view.show_msg(self[self._view.menu_item])

    def choice_interface_launch_app(self):
        """Выбирает интерфейс для запуска приложения"""
        number_interface = len(sys.argv)
        if number_interface == 1:
            self._input_interface = Input(interface_mode=1).use_interface()
