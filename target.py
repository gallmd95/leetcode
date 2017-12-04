nums = [3,2,4]
target = 6
d = {}
for i, each in enumerate(nums):
    d[target-each] = i
for i  in xrange(len(nums)):
    if nums[i] in d.keys():
        if not(d[nums[i]] == i):
            print [d[nums[i]],i]
print d
