list_1 = []
max_list = int(input("Введите максимальное значение диапазона: "))
min_list = int(input("Введите минимальное значение диапазона: "))
n = int(input("Введите количество элементов списка: "))

for i in range(n):
    element = int(input("Введите элемент: "))
    if element > min_list:
        if element < max_list:
            list_1.append(i)
print(list_1)
