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
        #alternates colors between red and blue
        
def draw_spesh_koch (t, depth, length):
    if depth > 1:
        t.pencolor("blue")
        draw_koch(t, depth - 1, length)
        t.lt(240)
        draw_koch(t, depth - 1, length)
        t.rt(60)
        draw_koch(t, depth - 1, length)
        t.lt(240)
        draw_koch(t, depth - 1, length) 
    else:
        t.pencolor("red")
        t.fd(length)
    
draw_spesh_koch(mozart, 4, 5)

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
        #assigns colors to a triangle at different depths
        
def draw_spesh_sierpinski(t, depth, length):
    if depth == 1:
        triangle(t, length)
    else:
        t.pencolor("red")
        draw_sierpinski(t, depth - 1, length / 2)  
        t.fd(length / 2)
        t.pencolor("blue")
        draw_sierpinski(t, depth - 1, length / 2)
        t.bk(length / 2)
        t.lt(60)
        t.fd(length / 2)
        t.rt(60)
        t.pencolor("green")
        draw_sierpinski(t, depth - 1, length / 2)  
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)

draw_spesh_sierpinski(mozart, 4, 50)

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
    #random length of branches and random angle
    
def spesh_tree(t, depth, length):
    if depth == 1:
        t.fd(length)
        t.bk(length)
    else:
        random_length = length * random.randint(0, 10)
        random_angle = random.randint (0, 45)
        t.fd(random_length)
        t.rt(random_angle)
        tree(t, depth - 1, random_length, random_angle)
        t.lt(random_angle * 2)
        tree(t, depth - 1, random_length, random_angle)
        t.rt(random_angle)
        t.bk(random_length)

spesh_tree(mozart, 4, 3)