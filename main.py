first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

print("Первое число: ", first)
print("Второе число: ", second)
print("Третье число: ", third)

if first == second and first == third and second == third :
    print("\n Все числа равны")
elif first == second or first == third or second == third:
    print("\n Два числа равны")
else:
    print("\n Совпадений не найдено")