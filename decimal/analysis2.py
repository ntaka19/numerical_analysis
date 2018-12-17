    
def func(num):
    j = 0
    n = 10**num
    for i in range(1,n+1):
        j = j + 10**(-1*num)

    return j

print("n=2")
print(func(2))

print("n=4")
print(func(4))

print("n=6")
print(func(6)) 

print("n=7")
print(func(7))

