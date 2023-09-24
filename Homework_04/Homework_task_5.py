x = input('Enter a random number: ')
summa = 0
for i in range(len(x)):
    b = int(x) // 10 ** i % 10
    summa += b
print(f'Sum of digits of this number: {summa}')
