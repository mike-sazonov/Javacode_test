# Wallet manager
Web-приложение, написанное на фреймворке FastAPI, которое по REST принимает запрос вида <br>
POST api/v1/wallets/<WALLET_UUID>/operation <br>
{ <br> operationType: DEPOSIT or WITHDRAW, <br>
amount: 1000 <br>
} <br>
после выполняет логику по изменению счета в базе данных. <br>
Также есть возможность получить баланс кошелька
GET api/v1/wallets/{WALLET_UUID}

### Содержание:
* [Используемые технологии](#используемые-технологии-)
* [Запуск проекта локально](#запуск-проекта-локально)
* [Запуск приложения с помощью Docker compose](#запуск-приложения-с-помощью-docker-compose)
* [Тестирование проекта с помощью Swagger UI](#тестирование-проекта-с-помощью-swagger-ui)
* [Нагрузочное тестирование](#нагрузочное-тестирование)
### Используемые технологии: 
* Python 3.11
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL
* Alembic
* Pytest
* JWT
* docker-compose

### Запуск проекта локально
1. Клонируйте проект с помощью команды: <br>
git clone https://github.com/mike-sazonov/Javacode_test.git <br>
2. Настройте виртуальную среду
3. В корне проекта создайте файл .env и заполните своими данными по примеру:<br><br>
DB_HOST=localhost<br>
DB_PORT=5432<br>
DB_USER=postgres<br>
DB_PASS=db_pass<br>
DB_NAME=db_name<br>
DB_NAME_TEST=db_name_test<br><br>

4. Командой **python -m pytest tests/** запускаем тесты.
5. Перед первым запуском проекта, совершаем первую миграцию с помощью Alembic:<br>
* Командой **alembic revision --autogenerate**, проверяем миграцию по адресу: Директория_проекта/alembic/versions
* Командой **alembic upgrade head** вносим изменения в нашу БД.

### Запуск приложения с помощью Docker compose
* Для запуска приложения с помощью Docker compose, в корневой папке создайте файл docker.env со своими данными: <br><br>
DB_HOST=db<br>
DB_PORT=5432<br>
DB_USER=postgres<br>
DB_PASS=db_pass<br>
DB_NAME=db_name<br>
DB_NAME_TEST=db_name_test<br><br>

* В консоли запускаем проект командой: docker compose up

### Тестирование проекта с помощью Swagger UI

* **Запустите проект из файла main.py, после чего перейдите по ссылке** http://127.0.0.1:8000/docs. <br>

* **Баланс кошелька по uuid (GET):**
![Swagger_get_request.png](images/Swagger_get_request.png)
Ответ:
![Swagger_get_response.png](images/Swagger_get_response.png)

* **Операция DEPOSIT по uuid кошелька (POST):**
![Swagger_post_request.png](images/Swagger_post_request.png)
Ответ:
![Swagger_post_response.png](images/Swagger_post_response.png)

### Нагрузочное тестирование

С помощью ApacheBench проведем нагрузочное тестирование конечных точек со следующими параметрами: <br><br>
Конечная точка GET api/v1/wallets/{WALLET_UUID}<br>
![ab_test_get.png](images/ab_test_get.png)
<br>
Результаты:
<br>
![ab_test_get_res.png](images/ab_test_get_res.png)
<br>
Конечная точка POST api/v1/wallets/<WALLET_UUID>/operation<br>
![ab_test_post.png](images/ab_test_post.png)
<br>
Результаты:
<br>
![ab_test_post_res.png](images/ab_test_post_res.png)

