import csv

count = 0

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile: 
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if len(row['Book-Title']) > 30:
            count += 1

print(f'Количество книг с названиями длиннее 30 символов: {count}')
