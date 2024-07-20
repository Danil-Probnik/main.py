#Работа со словарями
my_dict = {'Фамилия': 'Иванов', 'Имя': 'Иван', 'Отчество': 'Иванович'}
print(my_dict)
print(my_dict['Фамилия'])
print(my_dict.get('Год рождения', 'Без ошибки)'))
my_dict.update({'Страна': 'Россия', 'Город': 'Москва'})
A=my_dict.pop('Фамилия')
print(A)
print(my_dict)
#Работа с множествами
my_set=[1, 'Значение', 1, 2, 3, 3, 'Значение']
print(set(my_set))
my_set.append(13)
my_set.append(14)
my_set.remove(13)
print(my_set)