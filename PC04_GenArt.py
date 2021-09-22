"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Sydney Green

This code creates two circle patterns from two seperate turtles.
This is different than my pseudocode as I struggled bringing that to life but I was
able to make something I liked so much more. Turtle 1 is a larger circle with larger 
cirlces making it up and alternating colors. Turtle 2 is a smaller circle
made up of smaller cirlces containing different alternating colors as turtle 1. The
random aspect of this code is that each time that it is run the circles are located
in different places as the time before. The array of colors represented in each of the patterns
makes me feel warm and happy as both circles contain bright and vibrant color palettes. 

"""
#Randomized Circle Dots
#Borrowed code helped me randomize the locations of the circle dots
#Borrowed code is from "Quick guide to random library" canvas assignment page

import turtle
import math, random

turtle.colormode(255)

panel = turtle.Screen().bgcolor('black')

T1large = turtle.Turtle()
#Turtle 1 has its name because it will create the larger circle pattern made of cirlcles
T2small = turtle.Turtle()
#Turtle 2 has its name because it will create the smaller circle pattern made of circles
T2small.shapesize(3)

T1large.width(2)
T2small.width(2)
T1large.speed(11)
T2small.speed(11)

T1large.goto(random.randint(0,250),random.randint(0,250))
#Turtle 1's goto is random. It's random because I want its location to change each time the code is ran.

#This first for loop creates many large circles that come together forming one large complete circle.
for i in range(10):
    for colours in [(217,4,41), (220,96,46), (254,215,102), (104,163,87), (4,139,168)]:           
        T1large.color(colours)
        T1large.down()
        T1large.circle(50)
        T1large.left(10)
T1large.up()
T2small.goto(random.randint(100,350),random.randint(100,350))
#Turtle 2's goto is random. It's random because I want its locaction to change each time the code is ran. 

#This second for loop creates many small circles that come together forming one smaller complete circle.
for i in range(10):
    for colours in [(138,234,146), (167,153,183), (48,102,190), (255,251,252), (251,186,114)]:           
        T2small.color(colours)
        T2small.down()
        T2small.circle(20)
        T2small.left(10)
T2small.up()

turtle.done()
