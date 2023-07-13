num = 180_150_001
intermediate = None
res = ""
hex_num = hex(num)
while num > 0:
    intermediate = num % 16
    if intermediate < 10:
        res += str(intermediate)
    elif intermediate == 10:
        res += "a"
    elif intermediate == 11:
        res += "b"
    elif intermediate == 12:
        res += "c"
    elif intermediate == 13:
        res += "d"
    elif intermediate == 14:
        res += "e"
    elif intermediate == 15:
        res += "f"
    num //= 16

print("ваш ответ в шестнадцатеричной системе -> ", res[::-1])
print("\tПроверка -> ", hex_num[2:])

# продвинутый вариант
num = int(input("Введите число для перевода в 16-ную систему -> "))
# 180_150_001
res = ""
hex_num = hex(num)
system_16 = '0123456789abcdef'
system = 16

while num > 0:
    res += system_16[num % system]
    num //= system

print("ваш ответ в шестнадцатеричной системе -> ", res[::-1])
print("\tПроверка -> ", hex_num[2:])



import fractions


def common_div(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    res = (a + b)
    return res


# функция для нахождения НОД


num1, denom1 = list(map(int, input("Введите 2 числа для составления 1-ой дроби(пр: a/b) -> ").split('/')))
num2, denom2 = list(map(int, input("Введите 2 числа для составления 2-ой дроби(пр: a/b) -> ").split('/')))

if denom1 == denom2:
    print('Сумма дробей = {}/{}'.format(num1 + num2, denom1))
else:
    cd = int(denom1 * denom2 / common_div(denom1, denom2))
    rn = int(cd / denom1 * num1 + cd / denom2 * num2)
    g2 = common_div(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print('\tСумма дробей = {}/{}'.format(n, d) if n != d else n)

# произведение дробей
e = num1 * num2
f = denom1 * denom2
print(f"\tПроизведение дробей = {e}/{f}")

droby1 = fractions.Fraction(num1, denom1)
droby2 = fractions.Fraction(num2, denom2)
print(f"Проверка: \n\tСумма дробей = {droby1 + droby2} \n\tПроизведение дробей = {droby1 * droby2}")
