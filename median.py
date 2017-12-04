from math import ceil, floor
    
    
def median(a):
    if len(a) > 0:
        index = (len(a)-1)/2.0
        if index % 1 == 0:
            return a[int(index)]
        else:
            return (a[int(ceil(index))] + a[int(floor(index))])/2.0
    else:
        return None

def merge(a,b):
    x = 0
    y = 0
    c = []
    n1 = len(a)
    n2 = len(b)
    while x < n1 and y < n2:
        print x,y
        if a[x] < b[y]:
            c.append(a[x])
            x = x + 1
        else:
            c.append(b[y])
            y = y + 1
    c.extend(a[x:])
    c.extend(b[y:])
    return c
a = [1,3]
b = [2]
print median(merge(a,b))