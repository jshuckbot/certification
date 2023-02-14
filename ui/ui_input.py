from .ui_tui import TUI
from .ui_cli import CLI


class Input:
    """
    Отвечает за ввод данных через выбранный интерфейс.
    interface_mode:
    1 - TUI (текстовый пользовательский интерфейс)
    2 - CLI (интерфейс командной строки)
    """

    __user_interface = None

    def __init__(self, *, interface_mode=1):
        if interface_mode == 1:
            self.__user_interface = TUI()
        elif interface_mode == 2:
            self.__user_interface = CLI()

    def use_interface(self):
        """Использует выбранный интерфейс"""
        return self.__user_interface
