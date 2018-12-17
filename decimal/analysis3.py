
def func(num):
    p = 2 ** num 
    q = 2 **(-1*num)

    return p,q 

print("n=2")
print(func(2))

print("n=4")
print(func(4))

print("n=6")
print(func(6)) 

print("n=8")
print(func(8))

print("n=10")
print(func(10))

print("n=12")
print(func(12))

print("n=13")
print(func(13))

print("n=14")
print(func(14))

print("n=100")
print(func(100))
