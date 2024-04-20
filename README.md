# Book24 Scraper

## Обзор
Book24 Scraper - это инструмент для извлечения информации о книгах с веб-сайта book24.ru. Создан на основе фреймворка Scrapy на языке Python, предназначенного для веб-скрапинга и обхода веб-сайтов.

## Особенности
- **Поиск и Скрапинг**: Позволяет вводить запросы для поиска книг на сайте book24.ru и извлекать информацию о них, такую как название, цена, URL и фотографии.
- **Гибкая Настройка**: Возможность настройки логики работы скрапера, полей элементов и конвейеров в соответствии с требованиями проекта.
- **Загрузка Изображений**: Автоматическая загрузка обложек книг для последующего анализа или использования в оффлайн-режиме.
- **Обработка Ошибок**: Встроенные механизмы обработки ошибок обеспечивают надежный скрапинг, даже в случае возникновения сетевых проблем или изменений на веб-сайте.

## Использование
1. **Установка Зависимостей**: Убедитесь, что у вас установлен Python, а затем выполните установку Scrapy и других зависимостей с помощью pip:
    ```bash
    pip install scrapy
    ```

2. **Клонирование Репозитория**: Склонируйте данный репозиторий на свой компьютер с помощью следующей команды:
    ```bash
    git clone https://github.com/your_username/book24-scraper.git
    ```

3. **Настройка Скрейпера (По Желанию)**: При необходимости измените логику работы паука, определение полей элементов и конвейеры в директории `book24_scraper`.

4. **Запуск Скрейпера**: Запустите скрипт `runner.py` с вашими поисковыми запросами:
    ```bash
    python runner.py --query "фантастика"
    ```

5. **Просмотр Результатов**: После завершения процесса скрапинга, извлеченные данные будут доступны для дальнейшего анализа или хранения.

## Внесение Вклада
Приветствуется внесение вкладов! Если у вас возникли проблемы или у вас есть предложения по улучшению проекта, не стесняйтесь открывать новые задачи или предлагать свои решения.

## Автор: `Сергей Гуков`

