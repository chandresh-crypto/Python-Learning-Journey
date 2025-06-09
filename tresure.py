print('''                             `-..-'             __
                   _.--""  |
    .----.     _.-'   |/\| |.--.
    |jrei|__.-'   _________|  |_)  _______________  
    |  .-""-.""""" ___,    `----'"))   __   .-""-.""""--._  
    '-' ,--. `    |tic|   .---.       |:.| ' ,--. `      _`.
     ( (    ) ) __|tac|__ |// _..--  / ( (    ) )--._".-.
      . `--' ;\__________________..--------. `--' ;--------'
       `-..-'                               `-..-''''')

print('welcome to treasure')
print('your mission is to find treasure')
ask = input('which road do you prefer left or right?L or R:')
if ask == 'R' :
    print('sorry you fall in hole \n  -game over!!')
elif ask=='L':
    print('good choice you passed the road')
    ask2= input('there is no road what you prefer swim or wait for baot? S OR W:')
    if ask2=='S':
       print('sorry you died because of cold water \n  -game over!!')
    elif ask2=='W':
        print('you passed you are cool minded and observing  person')
        ask3= input('you have three doors to win treasure choose one RED,YELLOW OR BLUE?R,Y,B:')
        if ask3 == 'R':
            print('sorry you burned in fire \n   -game over!!')
        elif ask3 =='B':
            print('sorry you drown in water \n   -game over!! ')
        elif ask3=='Y' :
            print('you win the treasure !! you are so smart yaa')
else:
    print('invalid option ')
