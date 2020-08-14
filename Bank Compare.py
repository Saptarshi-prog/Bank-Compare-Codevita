# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:34:58 2020

@author: Saptarshi Neogi
"""

bank = []
principal = int(input())
year = int(input())

for i in range(0, 2): # Since there are 2 banks
    installments = int(input())
    sum = 0

    for i in range(0, installments):
        years, interest = [float(i) for i in input().split()]
        square = pow((1+interest), years*12)
        emi = (principal*(interest)/(1-1/square))
        sum = sum + emi
    bank.append(sum)

if bank[0] < bank[1]:
    print("Bank A")
else:
    print("Bank B")