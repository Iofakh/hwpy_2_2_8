max_mass = int(input('Веддите максимальную грузоподемность лодки: '))
fisher_number = int(input('Веддите колличество рыбаков: '))
mass = []
boats_count = 0

for _ in range(fisher_number):
    mass.append(int(input()))

mass.sort()

while mass:
    if (mass[0] + mass[-1]) > max_mass:
        boats_count += 1
        mass.pop()
    elif len(mass) > 1:
        mass.pop()
        mass.pop(0)
        boats_count += 1

    else:
        mass.pop()
        boats_count += 1

print(boats_count)
