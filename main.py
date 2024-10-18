#файл для чтения
input_file = open('text.txt', 'r', encoding='utf-8')
 #строки из файла
lines = input_file.readlines()

# файл для записи
output_file = open('output.txt', 'w', encoding='utf-8')
# Фильтрация строк
for line in lines:
    if len(line.strip()) > 5:
        output_file.write(line)

