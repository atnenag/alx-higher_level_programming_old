#!/usr/bin/env python3
def fizzbuzz():
    for n in range(0, 101):
        if(n%3==0)&(n%5==0):
            print("FizzBuzz", end=" ")
        elif(n%3==0):
            print("Fizz", end=" ")
        elif(n%5==0):
            print("Buzz", end=" ")
        else:
            print("{}".format(n), end=" ")
