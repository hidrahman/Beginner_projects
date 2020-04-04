# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:39:50 2020

@author: K-
"""


import random

actual = random.randrange(1,20)

guess = int(input("Please enter your guess: "))

if guess == actual:
        print("Your guess is correct.")
elif guess < actual < 20:
        print("Your guess is too low.")
elif guess > 20:
        print("Out of range, please guess value between 1 to 20.")
elif guess < 1:
        print("Out of range, please guess value between 1 to 20.")
else:
        print("Your guess is too high.")

print("The actual number is: ",actual)