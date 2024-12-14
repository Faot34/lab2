import csv

def unique_publishers(csv_file):
    with open(csv_file, 'r', encoding='windows-1251') as csvfile:
        table = csv.DictReader(csvfile, delimiter=';')
        publishers = set()
        
        for row in table:
            publisher = row.get('Publisher', '').strip()
            if publisher:
                publishers.add(publisher)
    
    return sorted(publishers)

publishers = unique_publishers('books-en.csv')
print("Список уникальных издателей:")
for publisher in publishers:
    print(publisher)
