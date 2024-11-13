students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_surnames=sorted(students)
#print('Список фамилий:', (list_of_surnames))

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# list_of_grades=(sum(grades[0]) / len(grades[0]),
#                 (sum(grades[1]) / len(grades[1]),        # так не получилось, провозился полдня, но так и не понял почему
#                 (sum(grades[2]) / len(grades[2]),
#                 (sum(grades[3]) / len(grades[3]),
#                 (sum(grades[4]) / len(grades[4]))))))

#print(list_of_grades)

a=(sum(grades[0]) / len(grades[0]))
b=(sum(grades[1]) / len(grades[1]))
c=(sum(grades[2]) / len(grades[2]))
d=(sum(grades[3]) / len(grades[3]))
e=(sum(grades[4]) / len(grades[4]))

list_of_grades_1=[a, b, c, d, e]

my_dict=dict(zip(list_of_surnames, list_of_grades_1 ))

print(my_dict)

