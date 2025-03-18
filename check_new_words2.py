#!/usr/bin/python3
def load_new_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Добавляем проверку, чтобы исключить пустые строки
        return [(word.strip(), idx+1) for idx, word in enumerate(lines) if word.strip()]

def find_words_in_file(filename, new_words):
    found_words = []

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()[2:]  # Пропустить первые две строки
        for line in lines:
            # Получаем первое слово из строки (до запятой) и удаляем пробелы
            first_word_in_line = line.split(",")[0].strip()
            for word, line_number in new_words:
                # Теперь мы проверяем на точное соответствие
                if word == first_word_in_line:
                    found_words.append((word, line_number))
    return found_words

def main():
    new_words = load_new_words("newWords.txt")
    files_to_check = ["turk1.txt", "turk2.txt"]

    for file in files_to_check:
        found_words = find_words_in_file(file, new_words)
        for word, line_number in found_words:
            print(f"In {file}, found word '{word}' from line {line_number} of newWords.txt")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
