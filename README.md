# users

## Краткое описание

Создание пользователя выполняется с помощью библиотеки fastapi
Проверка Api тестов выполняется с помощью Pytest + requests + allure
Доступ к Swagger документации смотри 4 пункт

1. Создать и активировать виртуальное окружение

```angular2html
python3 -m venv .venv
source .venv/bin/activate
```

2. Установить библиотеки из requirements.txt

```shell
pip install -r requirements.txt
```

4. Создать файл с расширением .env заполнив в корне проекта

```angular2html
BASE_URL = "http://127.0.0.1:8000/"
```

## 2 Команды для запуска проекта на локальном компьютере

1. Запуск проекта

```shell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

2. Переход на страницу "Пользователи"

```html
http://localhost:8000/front/users.html
```

3. Запуск API тестов

- Перед запуском команды необходимо создать файл с названием .env и написать

```angular2html
BASE_URL=http://localhost:8000/
```

- Запуск тестов

```shell
python -m pytest -s -v
```

## 3 Установка и настройка docker в локальном компьютере для линукса - https://docs.docker.com/engine/install/ubuntu/

1. Set up Docker's apt repository.

```shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Install the Docker packages.

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the Docker Engine installation is successful by running the hello-world image.

```shell
sudo docker run hello-world
```

4. Для запуска docker без sudo необходимо сделать:

```shell
sudo usermod -aG docker $USER
```

5. /home/d/.docker - В директории на локальном компьютере удалить папку
6. Выполнить reboot

## 3.1 Запуск проекта в Docker

1. Перейти в директорию проекта на локальном компьютере через терминал пример:
   <img alt="Пример" height="100" src="![img.png](img.png)" title="Пример" width="100"/>
2. Собрать образ контейнера

```shell
docker build -t fastapi .
```

3. Проверить добавление образа

```shell
docker images
```

4. Запустить проект внутри контейнера

```shell
docker run -it fastapi bash
```

5. Команды, чтобы удалить контейнер и образ

```angular2html
docker rm
<id_container>
    docker rmi
    <id_images>
```

## 4 Дополнительная информация по проекту

1. Доступ к swagger документации - http://127.0.0.1:8000/docs#/

