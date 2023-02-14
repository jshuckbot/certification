from ui.ui_view import commands


class SelectorMenu:
    """Меню выбора"""

    def __getitem__(self, point):
        """Выбирает пункт меню"""
        if commands['ADD_NOTE'] == point:
            return self.__add_note()
        elif commands['EDIT_NOTE'] == point:
            return self.__edit_note()
        elif commands['REMOVE_NOTE'] == point:
            return self.__remove_note()
        elif commands['FIND_NOTE'] == point:
            return self.__find_note()
        elif commands['SELECTION_NOTES_BY_DATE'] == point:
            return self.__selection_notes_by_date()
        elif commands['SHOW_NOTES'] == point:
            return self.__show_notes()
        elif commands['WRITE_FILE'] == point:
            return self.__write_file()
        elif commands['READ_FILE'] == point:
            return self.__read_file()
        elif commands['EXIT'] == point:
            return self.__exit_app()

    def __add_note(self):
        """Выполняет добавление заметки и возвращает сообщение об операции"""
        return self._manager.add(*self._input_interface.input_note())

    def __edit_note(self):
        """Изменяет заметку и возвращает сообщение об операции"""
        id_note = self._input_interface.input_note_id()
        body = self._input_interface.input_body_note()
        msg = self._manager.edit_note(id_note, body)

        return msg

    def __remove_note(self):
        """Удаляет заметку и возвращает сообщение об операции"""
        id_note = self._input_interface.input_note_id()
        msg = self._manager.remove_note(id_note)

        return msg

    def __find_note(self):
        """Ищет заметку и возвращает сообщение об операции"""
        id_note = self._input_interface.input_note_id()
        note, msg = self._manager[id_note]
        self._view.show_note(note)

        return msg

    def __show_notes(self):
        """Выводит выводит все заметки"""
        notes, msg = self._manager.get_notes()
        if len(notes) > 0:
            self._view.show_notes(notes)

        return msg

    def __selection_notes_by_date(self):
        """Делает выборку заметок и возвращает сообщение об операции"""
        start, end = self._input_interface.input_selection_notes_by_date()
        try:
            selection_notes, msg = self._manager.get_notes_in_between_dates(start, end)
        except ValueError as e:
            return e

        self._view.show_notes(selection_notes)

        return msg

    def __write_file(self):
        """Записывает в файл заметки и возвращает сообщение об операции"""
        return self._manager.write()

    def __read_file(self):
        """Читает из файла заметоки и возвращает сообщение об операции"""
        msg = self._manager.read()

        return msg

    def __exit_app(self):
        """Возвращает сообщение о выходе из приложения"""
        return f'До свидания!'
