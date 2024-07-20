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









