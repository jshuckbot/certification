from datetime import datetime


class Note:
    """Класс Заметка"""
    __id_number = 0

    def __init__(self, header, body, *,
                 id_number=None, date_create=None, date_modify=None):
        """Иницилизация атрибутов заметки"""
        if id_number is None:
            Note.__id_number += 1
        else:
            Note.__id_number = id_number
        if date_create is None:
            self.__date_create = datetime.now()
        else:
            self.__date_create = datetime.strptime(date_create, '%d-%m-%Y %H:%M:%S')
        if date_modify is None:
            self.__date_modify = datetime.now()
        else:
            self.__date_modify = datetime.strptime(date_modify, '%d-%m-%Y %H:%M:%S')

        self.__id = Note.__id_number
        self.__header = header
        self.__body = body

    def edit(self, body):
        """Изменяет содержимое заметки"""
        self.__body = body
        self.__date_modify = datetime.now()

    def __str__(self):
        """Выводит заметку"""
        return f'Заметка: {self.__id:}\n'\
            f'Заголовок: {self.__header}\n'\
            f'Тело: {self.__body}\n'\
            f'Дата создания: {self.__date_create}\n'\
            f'Дата изменения: {self.__date_modify}'

    def encoding(self):
        """Создает словарь атрибутов заметки для сериализации"""
        return {
            'id_number': self.__id,
            'header': self.__header,
            'body': self.__body,
            'date_create': self.__date_create.strftime('%d-%m-%Y %H:%M:%S'),
            'date_modify': self.__date_modify.strftime('%d-%m-%Y %H:%M:%S')
        }

    def get_date_create(self):
        return self.__date_create.date()


if __name__ == '__main__':
    note_1 = Note('Завтрак', 'Каша манная, 200г воды')
    note_2 = Note('Купить книгу', 'Книга по паттернам проектирования')
    note_3 = Note('Сходить в кино', 'Вышел в прокат Аватар 2')
    note_3.edit('Он уже прошел! долго собирался..')
    print(note_1)
    print(note_2)
    print(note_3)
