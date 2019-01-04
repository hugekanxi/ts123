#-*- coding: UTF-8 -*-
import math

def quadratic(a,b,c):
     y=b*b-4*a*c
     if y==0:

         x1=-b/2*a
         x2=x1

         return x1,x2

     if y<0:
         return '原方程无实根'
print '方程的根解：'
print quadratic(4,4,1)


