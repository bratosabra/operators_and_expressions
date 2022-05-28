num = 23
guess = int(input('Пиши число:'))
if guess == num:
    print('Ты угадал')
elif guess < num:
    print('Число больше')
else:
    print('Число меньше')
print('Конец')
