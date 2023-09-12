<h1 align="center">✨ CV SCANNER ✨</h1>

<p align="center">  
<img src="https://img.shields.io/badge/python-3.11 -blueviolet.svg">

</p>


## ***Навигация***
- [Описание](#описание)
- [Возможные неполадки](#возможные_неполадки)
- [Как пользоваться сервисом](#как_пользоваться)
  - [Архитектура](#архитектура)
  - [Технологии](#Технологии)
- [How to install](#how_to_install)

<a name="описание"></a> 
## ***Описание***

Сервис предназначен для ранжирования резюме по заданным ключевым словам.

Демонстрация https://scanercv.3s.by/



<a name="возможные_неполадки"></a> 
## ***Возможные неполадки***

При использовании сервиса необходимо использовать только PDF файлы.

<a name="как_пользоваться"></a> 
## ***Как пользоваться сервисом***

- После загрузки всех резюме - пользователь задает ключевые слова, и отправляет запрос на сервер.  
<p align="center">
<img src="./readme_asserts/work.png" width="70%"></p>


<a name="архитектура"></a> 
### Архитектура

<p align="center">
<img src="./readme_asserts/arh.png" width="70%"></p> 

<a name="computer_vision_and_machine_learning"></a> 
### Технологии

- [FastApi](https://fastapi.tiangolo.com/)
- [VUE](https://vuejs.org/)

<a name="how_to_install"></a> 
## ***How to install***

- Метод №1 (Подходит для разворачивания с помощью Docker):
  - Клонировать репозиторий
  - Выполнить команду docker-compose build
  - Выполнить команду docker-compose up
  - Пререйти по адресу 127.0.0.1:8080

- Метод №2 (local):
  - Клонировать репозиторий
  - Настройка BACKEND
    - Установить python https://www.python.org/
    - Перейти в папку cd backend
    - Установить зависимости pip install -r requirements.txt
    - Запустить файл main.py
    - Должен запуститься webserver на 127.0.0.1:8000
  - Настройка FRONTEND
    - Установить nodejs https://nodejs.org/en
    - Перейти в папку cd frontend
    - Запустить команду npm install
    - Запустить команду npm run dev
    - Должен запуститься webserver на 127.0.0.1:8080