n = int(input()) 
sum = 0

while n > 0:
    digit = n % 10 #последняя цифра
    sum += digit   # суммируем последовательно 
    n //= 10       # целочисленное деление - переход на след порядок

print("Сумма цифр числа:", sum)