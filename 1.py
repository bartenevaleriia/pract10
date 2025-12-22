PIN = 4590

while True:
    code = int(input('Введите пин-код: '))
    if code == PIN:
        print('доступ разрешен')
        break
    else:
        print('Ошибка. Попробуйте еще раз')