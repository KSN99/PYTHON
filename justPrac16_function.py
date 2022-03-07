def open_account():
    print("New account has been created!")

open_account()

def deposit(balance,money):
    print("Sending is completed. You have {0}.".format(balance +money))
    return balance+money

def withdraw(balance, money):
    if balance>=money:
        print("Available. You have {0}".format(balance-money))
        return balance-money

    else:
        print("Unavaiable. {0}".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100 #수수료 부과 
    return commission, balance - money - commission
balance = 0 
balance = deposit(balance,1000)
#balance = withdraw(balance,2000)
#balance = withdraw(balance,500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며 , 잔액은 {1}원입니다.".format(commission,balance))