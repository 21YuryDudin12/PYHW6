a = int(input("Введите первый член прогрессии: "))
d = int(input("Введите разницу элементов: "))
n = int(input("Введите количество элементов прогрессии: "))

for i in range(1, n+1):
    current_a = a + (i-1) * d
    print(current_a, end = " ")