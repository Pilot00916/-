import os


def test_file_path(file_path):
    # Вычисляем название файла без расширения
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)

    # Вычисляем название диска
    disk_name = os.path.splitdrive(file_path)[0].rstrip(':')

    # Вычисляем корневую папку
    root_folder = os.path.dirname(file_path).split(os.sep)[1]

    return file_name, disk_name, root_folder
