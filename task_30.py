# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

#Cпособ_1:
a_1 = int(input('Введите первый элемент a_1: '))
d = int(input('Введите разность d: '))
n = int(input('Введите количество элементов n: '))
list_1 = []                             # или:
for i in range(n):                      #list_1 = [(i*d + a_1) for i in range(n)]
        list_1.append(a_1+d*i)
print(list_1)


# # Cпособ 2:  С помощью рекурсии
# a_1 = int(input('Введите первый элемент a_1: '))
# d = int(input('Введите разность d: '))
# n = int(input('Введите количество элементов n: '))

# def progres(a_1, d, n):
#     if n == 1:
#         return a_1
#     else:
#         print(a_1)
#         return progres(a_1 + d, d, n-1)
# print(progres(a_1,d,n))

 
    

