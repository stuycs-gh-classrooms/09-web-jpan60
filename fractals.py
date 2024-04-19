import turtle
import random
window = turtle.Screen ()
window.setup(600, 600)

mozart = turtle.Turtle()
mozart.pd()
mozart.lt(90)

#KOCH DRAWER

def draw_koch(t, depth, length):
    if depth > 1: 
        draw_koch(t, depth - 1, length)
        t.lt(60)
        draw_koch(t, depth - 1, length)
        t.rt(120)
        draw_koch(t, depth - 1, length)
        t.lt(60)
        draw_koch(t, depth - 1, length) 
    else:
        t.fd(length)


#SPECIAL KOCH DRAWER
        #modified angles at which turtle turns; instead of turning 60  degrees after depth 1, the turtle turns 240 degrees, then 60, then 240 again. 
        #conjoins koch snowflakes, and creates a turtle shaped koch curve!
        
def draw_spesh_koch (t, depth, length):
    if depth > 1: 
        draw_koch(t, depth - 1, length)
        t.lt(240)
        draw_koch(t, depth - 1, length)
        t.rt(60)
        draw_koch(t, depth - 1, length)
        t.lt(240)
        draw_koch(t, depth - 1, length) 
    else:
        t.fd(length)
    
draw_spesh_koch(mozart, 6, 5)

#SIERPINSKI DRAWER
        
def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def draw_sierpinski(t, depth, length):
    if depth == 1:
        triangle(t, length)
    else:
        draw_sierpinski(t, depth - 1, length / 2)  
        t.fd(length / 2)
        draw_sierpinski(t, depth - 1, length / 2)
        t.bk(length / 2)
        t.lt(60)
        t.fd(length / 2)
        t.rt(60)
        draw_sierpinski(t, depth - 1, length / 2)  
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)

#SPECIAL SIERPINKSKI DRAWER
        #
        
def draw_spesh_sierpinski(t, depth, length):
    if depth == 1:
        triangle(t, length)
    else:
        draw_sierpinski(t, depth - 1, length / 2)  
        t.fd(length / 2)
        draw_sierpinski(t, depth - 1, length / 2)
        t.bk(length / 2)
        t.lt(60)
        t.fd(length / 2)
        t.rt(60)
        draw_sierpinski(t, depth - 1, length / 2)  
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)

#FRACTAL TREE DRAWER
        
def tree(t, depth, length, angle):
    if depth == 1:
        t.fd(length)
        t.bk(length)
    else:
        t.fd(length)
        t.rt(angle)
        tree(t, depth - 1, length, angle)
        t.lt(angle * 2)
        tree(t, depth - 1, length, angle)
        t.rt(angle)
        t.bk(length)
        
#SPECIAL TREE DRAWER
        #this modified function will randomly change square or square root the angle of the branches of the tree
        
def spesh_tree(t, depth, length, angle):
    if depth == 1:
        t.fd(length)
        t.bk(length)
    else:
        angle_rand = random.randrange(angle ** 1/2, angle ** 2)
        t.fd(length)
        t.rt(angle)
        tree(t, depth - 1, length, angle)
        t.lt(angle * 2)
        tree(t, depth - 1, length, angle)
        t.rt(angle)
        t.bk(length)

    