Bilet = int(input('Введите количество билетов: '))
a = 0 # Вспомогательная переменная
Free = 0 # Если менее 18 лет, то билет бесплатный
Half = 0 # От 18 до 25 лет — 990 руб
Full = 0 # От 25 лет — полная стоимость 1390 руб
while a!=Bilet:
    try:
        Age = int(input(f'Введите возраст {a+1} посетителя: '))
        if Age > 100 or Age <= 0:
            raise ValueError ("Посетителю не может быть столько лет")
    except ValueError as error:
        print("Неправильный возраст")
    else:
        if Age<18:
            Free += 1
        elif 18<=Age<25:
            Half += 1
        else:
            Full += 1
        a += 1
if Bilet>3:
    print('Сумма к оплате: ', round(0.9*(Half*990+Full*1390)), ' руб.')
else:
    print('Сумма к оплате: ', Half*990+Full*1390, ' руб.')