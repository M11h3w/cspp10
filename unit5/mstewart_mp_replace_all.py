a = [1,2,2,3,4,2,5,6,2,7,8,2,9,2,2,2,2,10]
while 2 in a:
    index = a.index(2)
    a.remove(2)
    a.insert(index,"x")
print(a)