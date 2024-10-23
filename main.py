#файл для чтения
with open('text.txt', 'r', encoding='utf-8') as input_file: 
    #строки из файла
    lines = input_file.readlines()
# файл для записи
with open('output.txt', 'w', encoding='utf-8') as output_file:
# Фильтрация строк
    for line in lines:
        if len(line.strip()) > 5:
            output_file.write(line)

