#Write a program that will prompt you for how many coins you want.
#Initially you have no coins.  It will ask you if you want a coin?
#If you type "yes", it will give you one coin, and print out the 
#current tally. If you type no, it will stop the program.

coin_count = 0
wants_more_coins = 'yes'

print(f'You have {coin_count} coins.')
while wants_more_coins == 'yes':
    wants_more_coins = input('Do you want another? ')
    if wants_more_coins == 'yes' or wants_more_coins == 'Yes':
        coin_count += 1
        print(f'You have {coin_count} coins.')

print('Bye')
