#Способ первый
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Yes=dict.fromkeys(sorted(students), 0)
s1o=grades[0]
s1 = sum(s1o)/len(s1o)
s2o=grades[1]
s2 = sum(s2o)/len(s2o)
s3o=grades[2]
s3 = sum(s3o)/len(s3o)
s4o=grades[3]
s4 = sum(s4o)/len(s4o)
s5o=grades[4]
s5 = sum(s5o)/len(s5o)
Yes['Aaron']=(s1)
Yes['Bilbo']=(s2)
Yes['Steve']=(s3)
Yes['Khendrik']=(s4)
Yes['Johnny']=(s5)
print(Yes)

#Способ второй
print('Посмотрите пожалуйста на второй способ, делал с помощью функции(формулы) for in, которую подсмотрел в интернете')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Yes=dict.fromkeys(sorted(students), 0)
SO=[]
for grades[0] in grades:
    SO.append(sum(grades[0])/len(grades[0]))
Yes['Aaron'] = SO[0]
Yes['Bilbo']=SO[1]
Yes['Steve']=SO[2]
Yes['Khendrik']=SO[3]
Yes['Johnny']=SO[4]
print(Yes)

#Мне кажется вам будет интересно:
print('Мне будет очень приятно если вы воспользуетесь вводом')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Yes=dict.fromkeys(sorted(students), 0)
s1o=grades[0]
s1 = sum(s1o)/len(s1o)
s2o=grades[1]
s2 = sum(s2o)/len(s2o)
s3o=grades[2]
s3 = sum(s3o)/len(s3o)
s4o=grades[3]
s4 = sum(s4o)/len(s4o)
s5o=grades[4]
s5 = sum(s5o)/len(s5o)
Yes['Aaron']=(s1)
Yes['Bilbo']=(s2)
Yes['Steve']=(s3)
Yes['Khendrik']=(s4)
Yes['Johnny']=(s5)
print('Здраствуйте, введите пожалуйста, имя ученика (без пробелов, с заглавной буквы):')
print('Johnny,', 'Bilbo,', 'Steve,', 'Khendrik,', 'Aaron.')
name=input('Имя:')
if name=='Johnny':
    print('Средний бал студента Johnny -', s5)
if name=='Bilbo':
    print('Средний бал студента Bilbo -', s2)
if name=='Steve':
    print('Средний бал студента Steve -', s3)
if name == 'Khendrik':
    print('Средний бал студента Khendrik -', s4)
if name == 'Aaron':
    print('Средний бал студента Aaron -', s1)
else:
    print('Ученика', name, 'нет в нашей базе данных или его имя введено неверно')








