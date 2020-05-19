import pickle
import os.path
from address_book import AdressBook

print('Привет! Это адресная книга.')

if os.path.exists('abonents.pickle'):
    with open('abonents.pickle', 'rb') as f:
        abonents = pickle.load(f)
    f.close()
else:
    abonents = {}
        
ab = AdressBook()

def run_book():
    while True:
        choice = input('''
Введите число: 
1 - добавить пользователя. 
2 - просмотреть текущих пользователей
3 - удалить пользователя по id
Для выхода нажмите enter.
''')
        if choice == '1':    
            name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            email = input('Введите email: ')
            phone = input('Введите телефон: ')
            job = input('Введите место работы: ')
            if len(abonents) == 0:
                num = 1
            else:
                num = list(abonents)[-1] + 1
            abonents[num]= name, last_name, email, phone, job
            ab.rec_ab(abonents)
        elif choice == '2':  
            ab.out_ab(abonents)
        elif choice == '3':
            ab.del_ab(abonents)
        else:
            print('Пока!')
            break

if __name__ == '__main__':
    run_book()
