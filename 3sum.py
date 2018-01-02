import copy
def c(nums):
        d = {}
        ret = []
        for i in xrange(len(nums)):
            temp = copy.copy(nums)
            a = temp[i]
            del temp[i]
            for j in xrange(i, len(temp)):
                temp1 = copy.copy(temp)
                b = temp1[j]
                del temp1[j]
                c = -(a+b)
                if c in temp1:
                    temp2 = [a,b,c]
                    temp2.sort()
                    if temp2 not in ret:
                        ret.append(temp2)
        return ret

print c([-12,-1,4,-14,0,10,7,-7,-6,9,6,-2,7,13,9,-1,4,12,9,4,14,0,-4,0,0,10,2,-7,7,-4,-11,10,2,8,4,-12,-4,-12,-4,-3,12,9,11,4,-1,-3,10,-12,-6,-4,-1,-14,3,2,-7,-11,-3,10,-11,-10,13,-15,7,0,0,-4,-5,11,0,-2,-14,-11,-8,12,1,-1,-14,-12,-6,-5,0,9,-4,-12,-4,4,14,9,-9,10,14,-11,10,6,-3,-4,10,-1,14,-13,13,7,-9,12,4,-1,-4,5,3,6,8,10,0,11,13,11,-7,5,-3,-1,0,-4,-4,-4,10,0])