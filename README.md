# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

[TODO: объясните пользователю, откуда брать ключи, куда их класть и как они выглядят]

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Настройки проекта хранятся в переменных окружения, нужно указать их в файле `.env` вида:

```
DATABASES = {
    'default': {
        'ENGINE': ИМЯ_ДВИЖКА_СУБД,
        'HOST': АДРЕС_ХОСТА,
        'PORT': ПОРТ_ХОСТА,
        'NAME': ИМЯ_БД,
        'USER': ИМЯ_ПОЛЬЗОВАТЕЛЯ,
        'PASSWORD': ПАРОЛЬ_ПОЛЬЗОВАТЕЛЯ,
    }
}

SECRET_KEY = УНИКАЛЬНОЕ_ЗНАЧЕНИЕ

DEBUG = True
```

Запуск скрипта производится командой 
```
python3 manage.py runserver 0.0.0.0:8000
```
После этого в браузере открыть адрес [localhost:8000](localhost:8000)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
