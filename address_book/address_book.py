import pickle
import os.path
from record import Record
from utils import benchmark

class AdressBook(Record): 
    @benchmark
    def rec_ab(self, abonents):
        """
        добавление пользователя в адресную книгу
        """
        with open('abonents.pickle', 'wb') as f:
            pickle.dump(abonents, f)
        f.close()

    def check(self, abonents):
        """
        проверка есть ли что-то в словаре
        """
        if any(abonents):
            return True
        else:
            return False

    @benchmark   
    def out_ab(self, abonents):
        """
        вывод пользователей из адресной книги
        """
        if os.path.exists('abonents.pickle') and self.check(abonents):
            print("В адресной книге находятся \nФамилия: Имя, почта, телефон, место работы:")
            with open('abonents.pickle', 'rb') as f:
                abonents_load = pickle.load(f)
            f.close()
            for key in abonents_load.keys():
                print(key,': ', abonents_load[key])
        else:
            print('Адресной книги нет')
    
    @benchmark
    def del_ab(self, abonents):
        """
        удаление пользователя из адресной книги
        """
        if os.path.exists('abonents.pickle') and self.check(abonents):
            print("В адресной книге есть:")
            with open('abonents.pickle', 'rb') as f:
                abonents_load = pickle.load(f)
            for key in abonents_load.keys():
                print(key,': ', abonents_load[key])
           
            num = int(input('\nВведите id абонента для удаления: '))
            if num in abonents:
                print(f'Удален пользователь "{num}"')
                del abonents[num]
                self.rec_ab(abonents)
            else:
                print('Нет такого человека')
        else:
            print('Адресной книги нет')
