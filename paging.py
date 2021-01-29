# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:27:51 2021

@author: user
"""

m=int(input("게시물의 총 건수?"))
def getTotalPage(m,n):
    if m%n==0 : return (m//n)
    else : return(m//n+1)


print(getTotalPage(m,10))