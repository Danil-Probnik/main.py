immutable_var= 1,'Привет',3
print(immutable_var)
#immutable_var.remove('Привет')
#print(immutable_var) AttributeError: 'tuple' object has no attribute 'remove', ругается говорит мол,
#нельзя так, тип данных то неизменяемый то есть "tuple", можно проверить:
print(type(immutable_var))
#Консоль не будет врать - <class 'tuple'>, хочется поменять, что то в списке? тогда не нужно использовать кортеж
#нужно юзать список в него и поправки вносить можно:
immutable_var_2=[1, 'Привет', 3]
immutable_var_2.remove('Привет')# Поправочка
print(immutable_var_2)
# Вторая часть задания позволяет продемонстрировать возможность внесения изменений:
mutable_list=[1, 'GG,WP', "2", True]
mutable_list.remove(1)
print(mutable_list)#Можно и попробовать че нить другое
mutable_list.append('Eror')
print(mutable_list)
#Можно и определенный элемент заменить/убрать
mutable_list[0]=('Yes')
print(mutable_list)
mutable_list.remove('Yes')
print(mutable_list)
