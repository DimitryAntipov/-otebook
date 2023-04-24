
from datetime import datetime
def write_into_file():
    print('Выберете вариант обращения в справочник: \n 1 - Запись новой заметки \n 2 - Поиск заметки \n 3 - Удалить заметку\n 4 - Изменить заметку  ')
    key = str(datetime.now())
    while True:
        option=int(input())
        if option<1 or option > 4:
            print("Попробуйте еще раз, такого варианта нет")
        else:
            break
    if option == 4:
        name_or_last = input("Введите заколовок той заметки которую хотите изменить: ")
        return '$ch$'+ name_or_last 
         
    if option == 3:
        name_or_last = input("Введите заколовок той заметки которую хотите удалить: ")
        print("Заметка удалена!") 
        return '$d$'+ name_or_last  
    
    if option == 2:
        name_or_last = input("Введите заколовок заметки или идентификатор: ")
        return '$s$'+ name_or_last 

    elif option == 1:
        n = '$n$'
        identifier = input("Введите идентификтор: ")
        header = input("Введите заголовок: ")
        body = input("Введите тело заметки: ") 
        print("Заметка создана!") 
        return (f'{n}{identifier};{header};{body};{key}')

      


