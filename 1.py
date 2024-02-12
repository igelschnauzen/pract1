first = int(input("Введите первое число: ", ))
second = int(input("Введите второе число: ", ))
third = int(input("Введите третье число: ", ))

maximum=first
minimum=first

for i in (second, third):
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Минимальное: ", minimum)
print("Максимальное: ", maximum)
