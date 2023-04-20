
number = float(input("Введите число от 0 до 1000: "))

if number > 1000 or number < 0:
    number = float(input("Ошибка! Неправильное число. Введите число от 0 до 1000: "))

endnum = int(((number/2)*10)%10)
if endnum == 0:
    print ("True")
else: print ("False")

