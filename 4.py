total = 0

while True:
    price = int(input('Введите цену товара (0 - закончить): '))

    if price == 0:
        break
    if price < 0:
        print('Ошибка цены')
        continue

    total += price

if total > 1000:
    total = total * 0.9
    print('Сумма со скидкой 10%:', total)
else:
    print('Сумма к оплате:', total)