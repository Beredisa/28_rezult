Введение
------------

Этот репозиторий содержит базовые тесты для онлайн-магазина Hobbii.com.
Тесты разработаны с использованием шаблона  PageObject с Selenium и Python (PyTest + Selenium).
Разработчик : Оксана Бреде 

Файлы
-----

[pages/conftest.py](../../28_result/pages/conftest.py) содержит код для отлова падающих тестов

[pages/base.py](pages/base.py) содержит PageObject pattern для Python.

[pages/hobbii_pages.py](pages/hobbii_pages.py) содержит web elements (селекторы) на страницах

[tests/*](tests) содержит Web UI тесты для разных частей онлайн-магазина Hobbii (https://hobbii.com )




Как запустить тесты
----------------

1) Установите все зависимости:

    ```bash
    pip3 install -r requirements.txt
    ```


2) Запустите тесты:

    ```bash
    py -m pytest -v --driver Chrome --driver-path chromedriver.exe tests
    ```


