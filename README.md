## Консольное приложение для работы с базой данных (Python + SQLAlchemy(SQLite))

## Требования для запуска:
Python 3.10+

## Подготовка:
- Клонировать репозиторий ```git clone https://github.com/Samuel-K732/DB-Management-PTMK```
- Установить зависимости ```pip install -r requirements.txt```

## Использование:
### Режим 1 - Создание таблицы
Для создания таблицы используйте команду ```python main.py 1```

### Режим 2 - Добавление сотрудника в таблицу
Для добавления записи используйте команду ```python main.py 2 "Ivanov Ivan Ivanovich" 2009-07-12 Male```

### Режим 3 - Вывод всех строк справочника сотрудников, с уникальным значением ФИО+дата, отсортированным по ФИО
Для вывода используйте команду ```python main.py 3```

### Режим 4 - Заполнение автоматически 1000000 строк справочника сотрудников + 100 сотрудников мужского пола, фамилия которых начинается на F
Для заполнения таблицы используйте команду ```python main.py 4```

### Режим 5 - Вывод всех сотрудников мужского пола, фамилия которых начинается на F
Для вывода используйте команду ```python main.py 5```

### Режим 6 (дополнительный) - полное удаление данных
Для удаления данных используйте команду ```python main.py 6```