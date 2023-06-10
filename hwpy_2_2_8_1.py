x = int(input('Веддите колличеcтво чисел массива: '))
print('Введите элемента массива через Enter')
mass = []
for _ in range(x):
    mass.append(int(input()))
mass.reverse()
print(mass)
