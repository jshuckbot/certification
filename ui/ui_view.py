commands = {
    'ADD_NOTE': 'add',
    'EDIT_NOTE': 'edit',
    'REMOVE_NOTE': 'remove',
    'FIND_NOTE': 'find',
    'SELECTION_NOTES_BY_DATE': 'selection',
    'SHOW_NOTES': 'show',
    'WRITE_FILE': 'push',
    'READ_FILE': 'pull',
    'EXIT': 'exit',
}


class _MenuNotes:
    """Меню для заметок"""
    menu_item = None
    MENU_ITEMS = [
        f"Команда [{commands['ADD_NOTE']}] - добавляет заметку",
        f"Команда [{commands['EDIT_NOTE']}] - редактирует заметку по ID",
        f"Команда [{commands['REMOVE_NOTE']}] - удаляет заметку по ID",
        f"Команда [{commands['FIND_NOTE']}] - ищет заметку по ID",
        f"Команда [{commands['SELECTION_NOTES_BY_DATE']}] - делает выборку по дате",  # по дипазону или по ондой
        f"Команда [{commands['SHOW_NOTES']}] - показывает все заметки",
        f"Команда [{commands['WRITE_FILE']}] - записывает заметки в файл формате JSON",
        f"Команда [{commands['READ_FILE']}] - читает заметки из файла формате JSON",
        f"Команда [{commands['EXIT']}] -  выходит из приложения",

    ]

    def _print_star_line(self):
        """Рисует линию"""
        print('*' * 30)

    def _print_dush_line(self):
        """Рисует линию из тире"""
        print('-' * 30)

    def show_menu(self):
        """Показывает меню"""
        print()
        self._print_dush_line()
        for item in self.MENU_ITEMS:
            print(item)
        self._print_dush_line()
        print()


class View(_MenuNotes):
    def show_notes(self, notes):
        """Показывает заметки"""
        print('Все наши заметки:')
        for note in notes:
            print(note)
        self._print_star_line()

    def show_note(self, note):
        """Показывает заметку"""
        print(note)

    def show_msg(self, msg):
        """Показывает информационное сообщение"""
        self._print_star_line()
        print(msg)
        self._print_star_line()
