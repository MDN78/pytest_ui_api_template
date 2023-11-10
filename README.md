# pytest_ui_api_template

## Шаблон для автоматизации тестирования на puthon 

### Шаги:
1. Склонировать проект `git clone https://github.com/MDN78/pytest_ui_api_template.git`
2. Установить все зависимости
3. Запустить тесты `pytest` или `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report
`

### Стэк:
 - pytest
 - selenium
 - requests
 - _sqlalchemy_
 - allure
 - configparser
 - json

 ## Структура:
  - ./test - тесты
  - ./pages - описание страниц
  - ./api - хелперы по работе с API
  - .db/ - хелперы по работе с базой данных 
  - ./configuration/ConfigProvider  - провайдер настроек
    - test_config.ini - настройки для тестов
  - ./testdata/DataProvider - провайдер тестовых данных
    - test_data.json - тестовые данные


 ### Полезные ссылки:

 - [Подсказка по Markdown](https://www.markdownguide.org/cheat-sheet/)
 - [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
 - [Trello API documentations](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/#api-actions-id-get)
 - [About pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)

