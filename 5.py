balance = 1000

while True:
    print('1. Узнать баланс')
    print('2. Снять 100 руб')
    print('3. Положить 100 руб')
    print('4. Выход')

    choice = input('Выберите действие: ')

    if choice == '1':
        print('Ваш баланс:', balance)
    elif choice == '2':
        if balance >= 100:
            balance -= 100
            print('Снято 100 руб.')
        else:
            print('Недостаточно средств')
    elif choice == '3':
        balance += 100
        print('Добавлено 100 руб.')
    elif choice == '4':
        print('До свидания')
        break
    else:
        print('Неверная команда')