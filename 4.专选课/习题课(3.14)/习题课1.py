
def add_check(number):
    check = (-3*sum(number[::2])-sum(number[1::2]))%10
    number.append(check)