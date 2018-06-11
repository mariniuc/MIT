# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:43:25 2018

@author: Dan
"""
balance = 320000 
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0 
low = balance / 12.0
up = balance * (1 + monthlyInterestRate) ** 12 / 12.0
pay = (low + up) / 2
ubalance = balance
while True:
    pay = (low + up) / 2
    ubalance = balance
    for m in range(12):
        ubalance -= pay
        ubalance += monthlyInterestRate * ubalance
    if abs(ubalance) < 0.1:
        print("Lowest Payment:", round(pay, 2))
        break
    elif ubalance < 0:
        up = pay
        pay = (low + up) / 2
    else:
        low = pay
        pay = (low + up) / 2
   
    
