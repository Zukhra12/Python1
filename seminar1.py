# Задача 1
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
num = int(input("Введите цифру: "))
if num == 6 and num == 7:
    print("Гип гип ураа, выходно!")
else:
    print("До выходного еще работать(")

# Задача 2
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input("Введите координаты точки Х: "))
y = int(input("Введите координаты точки Y: "))
if x > 0 and y > 0:
    print("I четверть")
if x < 0 and y > 0:
    print("II четверть")
if x < 0 and y < 0:
    print("III четверть")
if x > 0 and y < 0:
    print("IV четверть")

# Задача 3
#Напишите программу, которая по заданному номеру четверти,
#показывает диапазон возможных координат точек в этой четверти (x и y).
num = int(input("Введите номер четверти: "))
if num == 1 :
    print("x > 0 and y > 0")
if num == 2:
    print("x < 0 and y > 0")
if num == 3:
    print("x < 0 and y < 0")
if num == 4:
    print("x > 0 and y < 0")

# Задача 4 Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
ax = int(input("Введите координаты x точки A: "))
ay = int(input("Введите координаты y точки A: "))
bx = int(input("Введите координаты x точки B: "))
by = int(input("Введите координаты y точки B: "))

from math import sqrt
ab = sqrt((by-ay)**2+(bx-ax)**2), 2
print("Расстояние между точками А и В = ", ab )