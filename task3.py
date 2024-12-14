import csv
import random

def generate_bibliographic_references(input_file, output_file, num_references=20):
    with open(input_file, 'r', encoding='windows-1251') as csvfile:
        table = list(csv.DictReader(csvfile, delimiter=';'))
        
        selected_books = random.sample(table, num_references)
        
        with open(output_file, 'w', encoding='utf-8') as output:
            for idx, book in enumerate(selected_books, start=1):
                reference = f"{book['Book-Author']}. {book['Book-Title']} - {book['Year-Of-Publication']}\n"
                output.write(f"{idx}. {reference}")

generate_bibliographic_references('books-en.csv', 'ссылки_на_литературу.txt')
