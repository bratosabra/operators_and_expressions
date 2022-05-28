for i in range(1, 6):
    print(i)
else:
    print('Цикл')

while True:
    s = input("Text: ")
    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Цикл')
