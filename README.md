# ТехноМаркет - интернет-магазин электроники и бытовой техники

Этот проект представляет собой интернет-магазин электроники и бытовой техники, разработанный на Flask с использованием SQLite для хранения данных.

## Особенности проекта

- Блочная верстка с использованием DIV
- Адаптивный дизайн
- Каталог товаров с категориями
- Карточки товаров с детальным описанием
- Корзина покупок
- Форма обратной связи
- Счетчик посещений
- Функции для людей с особенностями зрения (увеличение шрифта, высококонтрастный режим)
- Калькулятор доставки
- Поиск товаров

## Технологии

- Python 3.8+
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- JavaScript

## Установка и запуск проекта локально

### Подготовка виртуального окружения

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/username/technomarket.git
   cd technomarket
   ```

2. Создайте виртуальное окружение и активируйте его:
   
   **Windows:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **Linux/MacOS:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

### Запуск приложения

1. Запустите приложение:
   ```
   python app.py
   ```

2. Откройте браузер и перейдите по адресу:
   ```
   http://127.0.0.1:5000/
   ```

## Развертывание на Render

### Подготовка к деплою

1. Убедитесь, что ваш проект находится в Git-репозитории
2. Файлы для деплоя уже настроены:
   - `gunicorn_config.py` - настройки веб-сервера Gunicorn
   - `render.yaml` - конфигурация для платформы Render
   - `requirements.txt` - включает все необходимые зависимости, включая Gunicorn

### Шаги для деплоя

1. Зарегистрируйтесь на [render.com](https://render.com/)
2. В дашборде выберите "New +" и "Web Service"
3. Подключите ваш Git-репозиторий
4. Настройка будет автоматически считана из `render.yaml`
5. Нажмите "Create Web Service"
6. После завершения сборки, ваш сайт будет доступен по URL в формате `https://{service-name}.onrender.com`

### Дополнительные настройки

- **Собственный домен**: В настройках сервиса на Render добавьте свой домен в разделе "Custom Domain"
- **Переменные окружения**: Можно добавить дополнительные переменные в настройках "Environment"
- **База данных**: Для production рекомендуется использовать PostgreSQL вместо SQLite

## Структура проекта

- `app.py` - основной файл приложения Flask
- `static/` - папка со статическими файлами (CSS, JavaScript, изображения)
- `templates/` - папка с HTML-шаблонами
- `electroshop.db` - база данных SQLite

## Доменное имя

Доменное имя проекта: www.tehnomarket.ru (не зарегистрировано, используется только для демонстрации)

## Автор

ФИО: [Ваше имя]
Группа: [Ваша группа]
Курс: [Номер курса] 