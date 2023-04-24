import csv
import re
from datetime import datetime
# Добавление контактов в список
def add (datasave):
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{datasave}\n')



# Поиск по имени 
def search (header):
    with open("Phonebook.csv", newline = '') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";")
        for row in reader:
            if row['Header'] == header or row['Identifier'] == header:
                print('Заголовок заметки:',row['Header'],'\n','Заметка:',row['Note Body'])

# удаление заметки 
def delit (header):
    
    with open("Phonebook.csv") as f:
        lines = f.readlines()

    pattern = re.compile(re.escape(header))
    with open("Phonebook.csv", 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)

# изменение заметки 
def change (header):
    hed =''
    key = str(datetime.now())
    with open ("Phonebook.csv", 'r') as f:
        old_data = f.read()

    with open("Phonebook.csv", newline = '') as csvfile:
        
        
        reader = csv.DictReader(csvfile,delimiter=";")
        for row in reader:
            if row['Header'] == header:
                new_header = input("Введите новый заголовок: ")
                hed = old_data.replace(row['Header'], new_header)
                new_body = input("Введите новое тело заметки: ")
                hed = hed.replace(row['Note Body'], new_body)
                hed = hed.replace(row['Data'], key)
                                 
    with open ("Phonebook.csv", 'w') as f:
        f.write(hed)    
      

 


