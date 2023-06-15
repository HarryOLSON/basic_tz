Тестове завдання

Написати код на python який буде за 1 запуск імпортувати всі дампи в БД в таблицю з полями: id, first_name, last_name, birthday, title, personal_id. Кожен файл повинен бути імпортований. Імпортовані значення не повинні містити зайвої інформації (зайві відступи, табуляція, і т.п.).

Використовувати можна стандартні модулі python + sqlite/postgres/mysql/...

це завдання можна виконати різними способами але для нас цікаво саме підхід до конструкції коду тож це більше тест на абстракцію в кодингу.

`docker build -t my-mysql-image .`

`docker run -d --name my-mysql-container -p 3306:3306 my-mysql-image`

Just execute the `main.py` with `python main.py`