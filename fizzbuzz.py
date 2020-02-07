while True:
    counter = 0
    user_number = int(input('what number do you want to add in?  '))
    while counter <= user_number:
        counter += 1
        if counter % 5 == 0 and counter % 3 == 0:
            print('FIZZBUZZ!')
        elif counter % 5 == 0:
             print('TOC!')
        elif counter % 3 == 0:
             print('POP!')
        else:
            print(counter)
    user = input('Would you like to stop playing the game?')
    if user.lower() == 'yes':
        break