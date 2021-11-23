import random

start = True

test_list = [6, 7, 8, 9, 10, 10, 10, 10, 11]


def discard(res):
        num = random.choice(res)
        res.pop(res.index(num))

        if num == 11:
            if input("do you wanna 11 or 1 ") == '11':
                return 11
            else:
                return 1
        return num


while start:
    res = [6, 7, 8, 9, 10, 10, 10, 10, 11]*4
    random.shuffle(res)
    s = input("start or no ")
    if s == 'start':
        comp = discard(res)
        user = discard(res)
        comp = comp + discard(res)
        print(comp)
        print(user)
        while input("do you wanna another card ?") == 'yes':
            user = user + discard(res)
            print("user = " + str(user))
            if user > 21:
                print("you lose")
                break
        if user < comp <= 21:
            print("comp win ")
        elif comp < user <= 21:
            print("you win ")
        elif user == comp:
            continue
    else:
        start = False

print(res)
