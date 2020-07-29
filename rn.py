import random

b = 0
while True:
    i = random.randint(10001, 99999)
    if i != 69420:
        print(i)
        b += 1
    else:
        print(i)
        break
print("Done in " + str(b) + " tries")