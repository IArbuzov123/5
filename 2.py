# Задание №2

# В первую строчку вводится число N (1 ≤ N ≤ 100 000). В следующую строку через пробел вводятся N чисел (1 ≤ Ai ≤ 10e9). 
# Вам требуется написать метод, который получает на вход массив и изменяет его таким образом, чтобы на первом месте стоял последний элемент,
# на втором - первый, на третьем - второй и т. д. Выведите N чисел - измененный массив.


res=list(map(int, input().split()))
res.insert(0, res.pop())
print(*res)












