import csv

def top_20_popular_books(csv_file):
    with open(csv_file, 'r', encoding='windows-1251') as csvfile:
        table = csv.DictReader(csvfile, delimiter=';')
        books = []
        
        for row in table:
            try:
                downloads = int(row.get('Downloads', 0))
                books.append((row.get('Book-Title', 'Unknown'), downloads))
            except ValueError:
                continue
        
        books.sort(key=lambda x: x[1], reverse=True)
    
    return books[:20]

top_books = top_20_popular_books('books-en.csv')
print("Топ 20 самых популярных книг:")
for idx, (title, downloads) in enumerate(top_books, start=1):
    print(f"{idx}. {title} - {downloads} загрузок")
