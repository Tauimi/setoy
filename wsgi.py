"""
WSGI entry point для Gunicorn.
"""
import sys
import logging

# Настройка логирования
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from app import create_app
    logger.info("Successfully imported create_app from app package")
except ImportError as e:
    logger.error(f"Failed to import create_app: {e}")
    raise

try:
    # Создаем экземпляр приложения
    application = create_app()
    logger.info("Successfully created application instance")
except Exception as e:
    logger.error(f"Failed to create application: {e}")
    raise

# Проверяем, что application существует и является WSGI приложением
if not application:
    raise RuntimeError("Application instance is None")
if not hasattr(application, '__call__'):
    raise RuntimeError("Application instance is not callable")

if __name__ == '__main__':
    application.run() 