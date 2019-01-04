#-*- coding: UTF-8 -*-
def findMinAndMax(L):
    if L!=[]:
        max=L[0]
        min=L[0]
        for l in L:
            if max<l:
                max=l
            if min>l:
                min=l
        return (min,max)
    else:
        return (None,None)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!++++1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!++++2', findMinAndMax([7]))
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!++++3', findMinAndMax([7, 1]))
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!++++4', findMinAndMax([7, 1, 3, 9, 5]))
else:
    print('测试成功!')



L=[1,2,3,4,5,6,7]
print L[0]



g=(x*x for x in range(10))

print next(g)
print next(g)

for n in g:
    print n


