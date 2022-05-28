num = 23
running = True
while running:
    guess = int(input('Пиши число:'))
    if guess == num:
        print('Ты угадал')
        running = False
    elif guess < num:
        print('Число больше')
    else:
        print('Число меньше')
else:
    print('Молодец')
