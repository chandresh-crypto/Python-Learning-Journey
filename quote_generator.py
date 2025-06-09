import random


quote =  [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Stay hungry, stay foolish. - Steve Jobs",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The best way to predict the future is to create it. - Peter Drucker"
]
print('your inspiring quote of the day is')
print(random.choice(quote))

again=input('do you want another quote?yes or no').lower()
if again == 'yes':
    print(random.choice(quote))
else:
   print('have a nice day')
