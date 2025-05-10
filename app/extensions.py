"""
Инициализация расширений Flask.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate
from flask_caching import Cache

# Инициализация расширений
db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name='Admin Panel', template_mode='bootstrap4')
migrate = Migrate()
cache = Cache()

def init_extensions(app):
    """Инициализирует все расширения для приложения."""
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app) 