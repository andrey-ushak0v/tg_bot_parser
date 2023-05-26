## Бот - парсер
бот, который парсит сообщения с канала на который получает ссылку

## инструкция по запуску
клонируйте проект на свой компьютер

``` git clone <ссылка на репозиторий> ```

создайте и активируйте виртуальное окружение

``` python3 -m venv venv ```

``` source venv/bin/activate ```

установите зависимости

``` pip install -r requirements.txt ```

создайте файл .env и поместите в него свои данные: token, api_id, api_hash

запустите файл bot.py

* вы прекрасны. отправьте боту ссылку на ваш любмиый канал и он пришлет вам последние 20 постов 
* поменять количество постов можно в файле parse_channel, поменяв значение переменной 'LIMIT' в 8ой строчке