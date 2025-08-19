# Проект по тестированию сервиса Trello
----
> Trello - инструмент, который позволяет вашей команде управлять проектами, рабочими процессами и заданиям любых типов.
> [Сайт Trello](https://trello.com/home)

![](assets/trello_main_page.PNG)

 ## Структура:
  - ./test - тесты
  - ./pages - описание страниц
  - ./api - хелперы по работе с API
  - .db/ - хелперы по работе с базой данных
  - ./configuration/ConfigProvider  - провайдер настроек
    - test_config.ini - настройки для тестов
  - ./testdata/DataProvider - провайдер тестовых данных
    - test_data.json - тестовые данные
----
## Список проверок, реализованных в автотестах:
### API

- [x] Проверка наличия досок
- [x] Создание доски
- [x] Удаление доски
- [x] Создание листа
- [x] Редактирование карты
- [x] Перемещение карты на другой лист
- [x] Удаление карты

### UI
- [x] Авторизация пользователя на сайте

### Проект реализован с использованием:

<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="https://github.com/MDN78/MDN78/blob/main/assets/selene.png"></code>
<code><img width="5%" title="selenium" src="https://github.com/MDN78/MDN78/blob/main/assets/selenium.png"></code>
<code><img width="5%" title="requests" src="https://github.com/MDN78/MDN78/blob/main/assets/requests.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>

Для написания UI-тестов используется чистый `Selenium`. API тесты используют библиотеку `Requests`. Библиотека модульного тестирования: `PyTest`
Установки дополнительных приложений на компьютер пользователя не требуется.
Фреймворк `Allure Report` собирает графический отчет о прохождении тестов


### Локальный запуск
1. Иметь тестовый аккаунт на платформе `Trello`: логин, пароль, имя пользователя
2. Получить API key & Token via Trello service
2. Склонировать проект `git clone https://github.com/MDN78/pytest_ui_api_template.git`
3. Установить все зависимости, в том числе:
   - Создать файл `test_data.json` в корневой папке проекта
   - Наполнить тестовыми данными в формате:
```json
{
    "key": "3d8eb615e7abdd4dbe36bcche656f9",
    "token": "ATTA047246b1dc3478903f1f804ecdfd15c31b8caa37bf2fc515ae56432b1096ef234A4FDFCE0",
    "email": "test@test.com",
    "password": "123456789",
    "username": "Semen",
    "org_id": "63558b830d636136d0181047"
}
```
4. Запустить тесты `pytest` или `python -m pytest`
5. Сгенерировать отчет `allure generate allure-files -o allure-report`
6. Открыть отчет `allure open allure-report` или `allure serve`

## Allure report
Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты и log - файлы
![](assets/allure_report_2.PNG)

 ### Полезные ссылки:

 - [Подсказка по Markdown](https://www.markdownguide.org/cheat-sheet/)
 - [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
 - [Trello API documentations](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-actions-id-get)
 - [About pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
