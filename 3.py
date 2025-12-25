print('Вводите числа. 0 - остановить')
max_num = 0
while True:
    num = int(input('Число: '))
    if num == 0:
        break
    if num > max_num:
        max_num = num
print(f'Максимальное число: {max_num}')
