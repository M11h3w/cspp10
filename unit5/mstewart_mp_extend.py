a = 1
b = 1
def extend(a,b):
    a = [1,2,3]
    b = [4,5,6]
    a.append(b[0])
    a.append(b[1])
    a.append(b[2])
    print(a)
extend(a,b)