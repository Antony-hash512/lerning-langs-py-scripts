import os
import sys

def sort_lines_by_line_number_desc(lines):
    def extract_line_number(line):
        try:
            return int(line.split('from line ')[1].split(' ')[0])
        except (IndexError, ValueError):
            return -1  # Return an invalid line number for sorting if extraction fails

    sorted_lines = sorted(lines, key=extract_line_number, reverse=True)
    return sorted_lines

def get_user_choice():
    print("Файл sorting_output.txt уже существует. Выберите действие:")
    print("1. Перезаписать файл")
    print("2. Дописать в конец файла")
    print("3. Отмена")
    choice = input("Введите номер выбранного действия (1, 2, или 3): ")
    return choice

def main():
    input_filename = 'sorting_input.txt'
    output_filename = 'sorting_output.txt'
    show_only = '--show' in sys.argv

    # Read lines from the input file
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Sort the lines
    sorted_lines = sort_lines_by_line_number_desc(lines)

    if show_only:
        # Print the sorted lines to the screen
        for line in sorted_lines:
            print(line, end='')
    else:
        # Check if the output file exists
        if os.path.exists(output_filename):
            user_choice = get_user_choice()
            if user_choice == '1':
                write_mode = 'w'
            elif user_choice == '2':
                write_mode = 'a'
            else:
                print("Операция отменена.")
                return
        else:
            write_mode = 'w'

        # Write the sorted lines to the output file
        with open(output_filename, write_mode, encoding='utf-8') as file:
            for line in sorted_lines:
                file.write(line)

        print(f"Результат записан в {output_filename}")

if __name__ == "__main__":
    main()

