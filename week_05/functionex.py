def sumall(a,b):
    value = []
    for i in range(a,b+1):
        if i % 3 != 0:
            value.append(i)
    return value