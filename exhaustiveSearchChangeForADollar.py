# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:22:12 2022

@author: Vincent Medrano

Exhaustive search method for number of ways to make a dollar in change
"""
#initialize counter at 0
counter = 0

for half_dollar in range(0,3):
    for quarter in range(0,5):
        for dime in range(0,11):
            for nickel in range(0,21):
                for penny in range(0,101):
                    if 50*half_dollar + 25*quarter + 10*dime + 5*nickel + penny == 100:
                        print(f"{half_dollar},{quarter},{dime},{nickel},{penny}")
                        #increment counter if 100 has been made
                        counter += 1

print(f"number of ways is: {counter}")