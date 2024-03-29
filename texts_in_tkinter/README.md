# Система управления текстовыми файлами с авторизацией

Этот проект представляет собой простую систему управления текстовыми файлами с использованием графического интерфейса на основе библиотеки Tkinter в Python. В системе реализованы функции регистрации и входа в систему для пользователей, а также операции создания, редактирования, открытия и удаления текстовых файлов.

## Как работает код:

### Регистрация и вход в систему:
- Пользователь вводит свое имя пользователя и пароль.
- При регистрации система хеширует пароль и сохраняет его в файле `credentials.json` в формате `{ "username": "hashed_password" }`.
- При входе в систему происходит сравнение введенного хешированного пароля с хешированным паролем из файла `credentials.json`.

### Управление файлами:
- После входа в систему пользователь может создавать, редактировать, открывать и удалять текстовые файлы.
- При создании файла он сохраняется в папке `texts`, в подпапке с именем пользователя.
- При редактировании содержимого файла система перезаписывает его содержимое.
- При удалении файла он удаляется из папки пользователя.

### Графический интерфейс:
- Графический интерфейс предоставляет простой и понятный способ взаимодействия с системой.
- Пользовательский интерфейс содержит поля для ввода имени пользователя, пароля, имени файла и его содержимого, а также кнопки для выполнения операций.

## Инструкции по запуску:
1. Установите библиотеку Tkinter, если она не установлена: `pip install tk`.
2. Запустите файл `main.py`.
3. Введите имя пользователя и пароль для входа в систему или для регистрации нового пользователя.
4. После входа вы можете создавать, редактировать, открывать и удалять текстовые файлы, используя соответствующие кнопки.

Этот проект создан в учебных целях для демонстрации простой системы управления файлами с использованием Python и Tkinter. 😊
