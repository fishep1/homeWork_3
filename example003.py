# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
x=[round(random.uniform(0.1, 100), 3) for x in range(11)]
print(x)
result = [round(i%1, 3) for i in x
          if i%1!=0]
# print(result)
# print(max(result))
# print(min(result))
print(f'Разница между максимальным значением дробной части и минимальным равно {round(max(result)-(min(result)), 3)}')