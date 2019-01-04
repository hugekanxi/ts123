# -*- coding: UTF-8 -*-

from __future__ import print_function
for i in range(1,10):
    for j  in range(1,i+1):
        print ('%s*%s=%s' %(i,j,i*j),end='')
    print()
