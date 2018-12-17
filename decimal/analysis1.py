def func(x,num):
    j = 0
    n = 10**num
    for i in range(1,n+1):
        j = j + x

    return j

print("x = 1")
print(func(float(1),2))
print(func(float(1),5))
print(func(float(1),8))
print("x = 0.1")
print(func(float(0.1),2))
print(func(float(0.1),5))
print(func(float(0.1),8))
print("x = 0.15625")
print(func(float(0.15625),2))
print(func(float(0.15625),5))
print(func(float(0.15625),8))
