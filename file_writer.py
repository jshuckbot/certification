"""Записывает в файл формате json можно расширить класс, если написать реализацию csv"""

from in_json import Json


class FileWriter:
    """Класс для записи и чтения из файла"""

    def __init__(self):
        self.__format = Json()

    def write(self):
        """Читает из файла в определенном формате"""
        return self.__format.write(self._notes)

    def read(self):
        """Записывает в файл в определенном формате"""
        self._notes, msg = self.__format.read()
        return msg
