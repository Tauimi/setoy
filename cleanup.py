import os
import shutil

# Список директорий __pycache__, которые нужно удалить
cache_dirs = [
    '__pycache__',
    'app/__pycache__',
    'app/admin/__pycache__',
    'app/utils/__pycache__',
    'app/routes/__pycache__',
    'app/models/__pycache__',
    'migrations/__pycache__',
    'migrations/versions/__pycache__'
]

def remove_cache_dir(path):
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Удалено: {path}")
    else:
        print(f"Не найдено: {path}")

def main():
    for dir_path in cache_dirs:
        remove_cache_dir(dir_path)

if __name__ == '__main__':
    main() 