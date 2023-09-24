for i in range(101):
    print(i)
    answer = input('Should we break? ')
    if answer == 'yes':
        break
    elif answer == 'no':
        continue
    else:
        while True:
            print('Dont understand you')
            answer = input('Should we break? ')
            if answer in ('yes', 'no'):
                break
        if answer == 'yes':
            break
        elif answer == 'no':
            continue
