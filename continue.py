# просто нумерация
for i in range(1, 6):
    print(i)
else:
    print('Цикл')

# закончится при слове выход, выводит длину строки
while True:
    s = input("Text1: ")
    if s == 'выход1':
        break
    print('Длина строки:', len(s))
print('Цикл1 закончен')

# Пишет мало, если мал
while True:
    s = input('Text2: ')
    if s == 'выход2':
        break
    if len(s) < 5:
        print('Мало')
        continue
    print('Длина:', len(s))
    print('Длина норм')
print('Цикл2 закончен')
