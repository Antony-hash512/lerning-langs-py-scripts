#!/usr/bin/env python3
# Импортируем только нужные функции
from strings_deleter import create_backup, delete_lines

def find_duplicate_lines(filename):
    line_count = {}
    duplicates = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            # Удаляем пробельные символы в начале и в конце строки
            cleaned_line = line.strip()

            # Пропускаем пустые строки
            if not cleaned_line:
                continue

            # Считаем строки и запоминаем номера строк
            if cleaned_line in line_count:
                line_count[cleaned_line] += 1
                duplicates[cleaned_line].append(line_number)
            else:
                line_count[cleaned_line] = 1
                duplicates[cleaned_line] = [line_number]

    # Оставляем только дубликаты
    duplicates = {line: nums for line, nums in duplicates.items() if line_count[line] > 1}

    return duplicates

def main():
    filename = 'newWords.txt'
    duplicates = find_duplicate_lines(filename)

    if duplicates:
        print("Найдены повторяющиеся строки:")
        for line, nums in duplicates.items():
            num_str = ', '.join(map(str, nums))
            print(f"'{line}' на строках: {num_str}")
        # спросить у пользователя, хочет ли он удалить эти строки
        answer = input("Хотите удалить эти строки? (y/n): ")
        if answer == 'y':
            backup_filename = create_backup(filename)
            # Для каждой группы дубликатов оставляем только первую строку
            lines_to_delete = []
            for line, line_numbers in duplicates.items():
                # Оставляем первую строку, удаляем остальные
                lines_to_delete.extend(line_numbers[1:])
            
            # Сортируем номера строк для удаления
            lines_to_delete.sort()
            
            if lines_to_delete:
                delete_lines(filename, lines_to_delete)
                print(f"Удалены дубликаты. Оставлен один экземпляр каждого слова.")
            else:
                print("Нет строк для удаления.")
    else:
        print("Повторяющиеся строки не найдены.")

if __name__ == "__main__":
    main()
