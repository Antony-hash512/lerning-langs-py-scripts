#!/usr/bin/python3
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
    else:
        print("Повторяющиеся строки не найдены.")

if __name__ == "__main__":
    main()
