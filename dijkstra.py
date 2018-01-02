a = [-6, 6, -6]

first = a[0]
last = a[len(a)-1]
middle = 0
if len(a) % 2 == 0:
    print "eher"
    middle = a[(len(a)/2)] + a[(len(a)/2)-1]
else:
    print "edher"
    middle = a[((len(a)+1)/2)-1]


print first, last, middle