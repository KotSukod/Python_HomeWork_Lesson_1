# Напишите программу, которая принимает на вход коорднаты двух точек 
# и находит расстояние между ними в 2D пространстве

print("Введите координаты точки А")
xa = int(input("Введите х: "))
ya = int(input("Введите y: "))
print("Введите координаты точки B")
xb = int(input("Введите х: "))
yb = int(input("Введите y: "))

a = float((xb - xa))
a = a**2
b = float((yb - ya))
b = b**2
sqrt = (a+b) ** 0.5
print(sqrt)