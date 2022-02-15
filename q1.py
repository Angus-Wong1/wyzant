import random 
"""
1. (20 points) John is drunk today. He walks in a grid of streets randomly picks one of four directions and stumbles to the next intersection, then again randomly picks one of four directions, and so on. You might think that on average John does not move very far because the choices cancel each other out, but that is actually not the case.
   Write a function to calculate the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) after `n` intersections.
   """
x = [1, 0, 2, 3]
y = [4, 4, 3, 1]

from math import sqrt

#create function to calculate Manhattan distance 
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))
 
#define vectors
A = [2, 4, 4, 6]
B = [5, 5, 7, 8]

#calculate Manhattan distance between vectors
print(manhattan(A, B))
def drunkard_walk(x, y, n):
    x=0
    y=0
    for i in range(0,100): #for 100 intersection
        direction= random.randint(0,3)

        if direction==0: #0 for north
            x+=1
        if direction==1: #1 for east
            y+=1
        if direction==2: #2 for south
            x-=1
        if direction==3: #3 for west
            y-=1
    return x,y

print(drunkard_walk(0,0,100))
def main():
    """
    Please do not change the code below.
    """
    x_0 = 0
    y_0 = 0
    steps = 100
    print(f"The drunkard started from ({x_0}, {y_0}).")
    distance = drunkard_walk(x_0, y_0, steps)
    print(f"After {steps} intersections, he's {distance} blocks from where he started.")

