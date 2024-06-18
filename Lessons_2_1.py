number = int(input("Введіть 5-и число: "))

num1 = number // 10000
num2 = (number % 10000) // 1000
num3 = (number % 1000) // 100
num4 = (number % 100) // 10
num5 = number % 10

number2 = num5 * 10000 + num4 * 1000 + num3 * 100 + num2 * 10 + num1

# Вивести перевернуте число
print("Перевернуте число:", number2)