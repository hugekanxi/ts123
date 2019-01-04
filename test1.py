from __future__ import print_function
#-*- coding: UTF-8 -*-
for i in range(1,10):
    #print(i,end = '')
    for j in range(1,i+1):
        print('%s*%s=%s' %(i, j, i*j),end = ' ')
    print()

