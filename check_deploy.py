"""
Скрипт для проверки конфигурации перед деплоем.
"""
import os
import sys
import logging
from pathlib import Path

# Настройка логирования
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

def check_file_exists(file_path, description):
    """Проверяет существование файла."""
    if not os.path.exists(file_path):
        logger.error(f"{description} не найден: {file_path}")
        return False
    logger.info(f"{description} найден: {file_path}")
    return True

def check_wsgi():
    """Проверяет WSGI конфигурацию."""
    try:
        from wsgi import application
        logger.info("WSGI application успешно импортирован")
        if not application:
            logger.error("WSGI application is None")
            return False
        if not hasattr(application, '__call__'):
            logger.error("WSGI application не является callable")
            return False
        return True
    except Exception as e:
        logger.error(f"Ошибка при проверке WSGI: {e}")
        return False

def main():
    """Основная функция проверки."""
    logger.info("Начинаем проверку конфигурации...")
    
    # Проверяем наличие необходимых файлов
    required_files = {
        'wsgi.py': 'WSGI файл',
        'app.py': 'Файл приложения',
        'requirements.txt': 'Файл зависимостей',
        'render.yaml': 'Конфигурация Render',
        'Procfile': 'Procfile'
    }
    
    all_files_exist = True
    for file_name, description in required_files.items():
        if not check_file_exists(file_name, description):
            all_files_exist = False
    
    if not all_files_exist:
        logger.error("Не все необходимые файлы найдены")
        sys.exit(1)
    
    # Проверяем WSGI конфигурацию
    if not check_wsgi():
        logger.error("WSGI конфигурация некорректна")
        sys.exit(1)
    
    # Проверяем наличие директорий
    required_dirs = ['app', 'templates', 'static']
    for dir_name in required_dirs:
        if not check_file_exists(dir_name, f"Директория {dir_name}"):
            sys.exit(1)
    
    logger.info("Проверка конфигурации успешно завершена")
    return 0

if __name__ == '__main__':
    sys.exit(main()) 