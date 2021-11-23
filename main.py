import random

start = True

mainL = [random.randrange(0, 10, 1) for i in range(4)]
while len(mainL) != len(set(mainL)):
    mainL = [random.randrange(0, 10, 1) for i in range(4)]
print(mainL)


def check(mainL, myL):
    c = 0
    for i in mainL:
        for k in myL:
            if i == k and mainL.index(i) == myL.index(k):
                c = c + 1
    print("elements on position " + str(c))
    print("just elements " + str(len(set(mainL) & set(myL)) - c))
    return c


while start:
    myL = []
    print("4 numbers from 0 to 9")
    while len(myL) != 4:
        n = int(input())
        if n in myL or n > 9 or n < 0:
            print("enter the right number")
            continue
        else:
            myL.append(n)
    if check(mainL, myL) == 4:
        start = False

print("you win")

