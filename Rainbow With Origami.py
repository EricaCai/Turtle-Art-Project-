#Rainbow Spiral With Origami
import colorsys
import turtle
import random
from myFunctions import*
frank = turtle.Turtle()
bob = turtle.Turtle()
frank.speed(11)
turtle.bgcolor("black")
"----------------------------------------------------------------------------"""
#head of origami cat (sister's choice)
bob.hideturtle()
bob.color("white")
bob.width(3)
jump(bob,300,300)
bob.rt(90)
bob.fd(150)
bob.rt(45)
bob.fd(100)
bob.rt(90)
bob.fd(100)
bob.rt(45)
bob.fd(150)
bob.rt(135)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.backward(100)
bob.rt(90)
bob.fd(100)
bob.backward(100)
bob.rt(90)
bob.fd(100)
"----------------------------------------------------------------------------"""
#origami cat body
bob.color("white")
bob.width(3)
jump(bob,160,10)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.backward(100)
bob.lt(45)
bob.fd(145)
"----------------------------------------------------------------------------"""
#origami cat tail
bob.color("white")
bob.width(3)
jump(bob,190,-20)
bob.rt(90)
bob.fd(100)
bob.rt(90)
bob.fd(100)
bob.rt(135)
bob.fd(100)
"----------------------------------------------------------------------------"""
#rainbow square like spiral
frank.hideturtle()
jump(frank,0,0)
for i in range(1001):
    color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
    #compatibility quirk: on 2.7 and below, use i/1000.0
    frank.color(color)
    frank.fd(i)
    frank.rt(98)
"----------------------------------------------------------------------------"""
#origami cat left eye
jump(bob,200,150)
bob.begin_fill()
bob.color("white")
bob.circle(8)
bob.end_fill()
"----------------------------------------------------------------------------"""
#origami cat right eye
jump(bob,250,150)
bob.begin_fill()
bob.color("white")
bob.circle(8)
bob.end_fill()
