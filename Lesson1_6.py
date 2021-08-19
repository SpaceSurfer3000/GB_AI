a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
day = int(1)
print(day, "-й день: ", a)
while a < b:
    day = day + 1
    a = a * 1.1
    print(day, "-й день: ", a)

print("на ", day, "-й день спортсмен достиг результата - не менее 3 км.")
