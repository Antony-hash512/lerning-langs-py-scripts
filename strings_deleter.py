#!/usr/bin/env python3
import sys
import os
import shutil
from datetime import datetime


def create_backup(filename):
    """Создает резервную копию файла с временной меткой."""
    # Создаем каталог backups, если он не существует
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Создан каталог для резервных копий: {backup_dir}")
    
    # Формируем имя файла резервной копии
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(backup_dir, f"{os.path.basename(filename)}.{timestamp}.bak")
    
    # Копируем файл
    shutil.copy2(filename, backup_filename)
    print(f"Создана резервная копия: {backup_filename}")
    return backup_filename


def delete_lines(filename, line_numbers):
    """Удаляет строки с указанными номерами из файла."""
    # Сортируем и конвертируем номера строк в 0-индексированные
    line_indices = sorted([int(num) - 1 for num in line_numbers])
    
    # Читаем все строки из файла
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Проверяем корректность номеров строк
    if max(line_indices, default=-1) >= len(lines):
        print(f"Ошибка: в файле всего {len(lines)} строк, но указан номер строки {max(line_indices) + 1}")
        return False
    
    # Выводим информацию об удаляемых строках
    print(f"Всего строк в файле: {len(lines)}")
    print(f"Будут удалены строки с номерами: {[i + 1 for i in line_indices]}")
    
    # Создаем новый список строк, исключая те, которые нужно удалить
    new_lines = [line for i, line in enumerate(lines) if i not in line_indices]
    
    # Записываем обновленное содержимое обратно в файл
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    
    print(f"Удалено строк: {len(lines) - len(new_lines)}")
    print(f"Осталось строк: {len(new_lines)}")
    return True


def main():
    # Проверяем количество аргументов
    if len(sys.argv) < 3:
        print("Использование: python strings_deleter.py <имя_файла> <номер_строки1> <номер_строки2> ...")
        sys.exit(1)
    
    filename = sys.argv[1]
    line_numbers = sys.argv[2:]
    
    # Проверяем существование файла
    if not os.path.isfile(filename):
        print(f"Ошибка: файл '{filename}' не существует.")
        sys.exit(1)
    
    # Проверяем, что все номера строк являются целыми числами
    try:
        [int(num) for num in line_numbers]
    except ValueError:
        print("Ошибка: номера строк должны быть целыми числами.")
        sys.exit(1)
    
    # Создаем резервную копию
    backup_filename = create_backup(filename)
    
    # Удаляем строки
    if delete_lines(filename, line_numbers):
        print(f"Операция завершена успешно. Оригинальный файл сохранен как: {backup_filename}")
    else:
        print(f"Операция не выполнена. Оригинальный файл не изменен.")


if __name__ == "__main__":
    main()
