#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i=10
    while i>=1:
        print(i)
        i-=1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    pass
    squared_integers=[integer**2 for integer in int_list]
    return squared_integers
def fizzbuzz():
    # code goes here!
    
    i=1
    while i<=100:
        if i%15==0:
            print(f"FizzBuzz")
        elif i%3==0:
            print(f"Fizz")
        elif i%5==0:
            print(f"Buzz")
        else:
            print(i)
        i+=1
        