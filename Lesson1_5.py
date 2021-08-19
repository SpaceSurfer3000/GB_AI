earnings = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if earnings > costs:
    print("Компания работает в прибыль!ееехууу")
    clean_earn = int(earnings - costs)
    profitability = int(clean_earn / earnings) * 1
    employee_amount = int(input('Введите количество сотрудников: '))
    salory_for_each = (clean_earn / employee_amount)
    print('Каждый сотрудник получит: ', salory_for_each)
else:
    print("!@№4%! ты лох! :D")
