from csv import reader

while True:
    flag = 0
    search = input('Введите запрос: ')
    
    if search == '0':
        break
    
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        
        for row in table:
            lower_case = row[2].lower()
            index = lower_case.find(search.lower())
            
            if index != -1:
                print(f"Название: {row[1]}, Автор: {row[2]}, Год: {row[3]}")
                output.write(f'{row[2]}. {row[1]} - {row[3]}\n')
                flag += 1
        
        if flag == 0:
            print('Ничего не найдено.')
        else:
            print(f'Найдено {flag} результатов.')


