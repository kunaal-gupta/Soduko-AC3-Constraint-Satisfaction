a = 1

def func():
    global a
    a = a+1
    return a


print(func())
print(a)
