import json
import os
from note import Note
from functools import wraps


def _check_data(func):
    """Декоратор проверки инициализации экземпляра"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return [], 'Данные повреждены!'

    return wrapper


class JsonEncoder(json.JSONEncoder):
    """Кодирует объекты в формат json"""

    def default(self, obj):
        if isinstance(obj, Note):
            return obj.encoding()
        return json.JSONEncoder.default(self, obj)


class Json:
    """Работает с json форматом"""

    file_name = 'data_notes.json'

    def write(self, notes):
        """Записывает список в файл"""
        with open(Json.file_name, 'w', encoding='utf-8') as f:
            json.dump(notes, f, cls=JsonEncoder,
                      indent=4, ensure_ascii=False)

        return 'Запись данных прошла успешно!'

    @_check_data
    def read(self):
        """Читает заметки из файла в список"""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as f:
                notes = json.load(f)
                return [Note(**item) for item in notes], 'Данные успешно прочитаны из файла!'

        return [], 'Файл не существует!'
