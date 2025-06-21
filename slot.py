import random


def spin_row():
    symbol = ['🍋','⭐','🔔']
    result =[]
    return[random.choice(symbol) for _ in range(3)]

def print_row(row):
    print('*******************')
    print(' | '.join(row))
    print('*******************')
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍋':
           return bet*10
        elif row[0]=='⭐':
            return bet*20
        elif row == '🔔':
            return bet *50

    return 0

def main(balance):
    print('************************')
    print('welcome to python slot 🎰')
    print('************************')
    print('- minimum spin amount must be grater than $20 ')
    current_balance = balance
    while balance >0:
         print(f'your amount is -${balance}')
         bet=(input('place amount to bet:'))
         if not bet.isdigit():
                 print('invalid amount ')
                 continue
         bet = int(bet)
         if bet>balance:
             print('invalid fund')
             continue
         elif bet<=20:
             print('bet must be bigger than $20')
             continue

         balance-=bet
         row =spin_row()
         print('spinning......')
         print_row(row)
         payout =get_payout(row,bet)
         if payout>0:
             print(f'you win {payout}')
         else:
             print('sorry you loose')
         balance+=payout
         play_again = input('do you want to play again (Y/N):').upper()

         if play_again!='Y':
             break
    print('--------------------------------------')
    print(f'GAME OVER YOUR BALANCE IS ${balance}')
    print('--------------------------------------')







