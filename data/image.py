from pathlib import Path
import os


def path(file_name):
    base_path = Path(__file__).resolve().parent.parent  # Получаем путь до корневой директории проекта
    tests_folder_path = base_path / 'tests'  # Добавляем папку "tests" к пути
    return str(tests_folder_path.joinpath(file_name))
