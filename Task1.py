# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# 11 6 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

string_1 = "11 6 2 4 6 8 10 12 10 8 6 4 2"
string_2 = "3 6 9 12 15 18"
array_1 = []
array_2 = []
array_1 = string_1.split()
array_2 = string_2.split()

for i in range(len(array_1)):
    array_1[i] = int(array_1[i])
for i in range(len(array_2)):
    array_2[i] = int(array_2[i])

array_combo = []

for i in array_1:
    if i in array_2 and i not in array_combo:
        array_combo.append(i)
for i in array_2:
    if i in array_1 and i not in array_combo:
        array_combo.append(i)

array_combo_range = array_combo
temp = 0
j = 0
while j < len(array_combo_range):
    i = 1
    while i < len(array_combo_range)-j:
        if array_combo_range[i] < array_combo_range[i-1]:
            temp = array_combo_range[i]
            array_combo_range[i] = array_combo_range[i-1]
            array_combo_range[i-1] = temp
        i +=1
    j +=1
        
print(array_combo_range)

