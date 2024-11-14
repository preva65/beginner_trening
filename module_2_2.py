first= int(input('Введите первое число: '))
print(first)
second= int(input('Введите второе число: '))
print(second)
third= int(input('Введите третье число: '))
print(third)

lst=[first, second, third]

if (len(set(lst)))== 1:
    print(3)
if (len(set(lst)))== 2:
    print(2)
if (len(set(lst)))== 3:
    print(0)