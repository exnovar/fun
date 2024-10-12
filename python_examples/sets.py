# sets remove duplicates & are fast
myset = {2,1,3,4,1,1,1,1}
print(myset)


searchvar = 3

if searchvar in myset:
    print("its there")

a = {1,2,3}
b = {2,5,7}

union = a | b
intersection = a & b
difference = a - b
print(union, intersection, difference)


ax = {"apple", "banana", "greens"}
bx = {"cookie", "nothing", "greens"}


union = ax | bx
intersection = ax & bx
difference = ax - bx
print(union, intersection, difference)

