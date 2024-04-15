import turtle
window = turtle.Screen ()
window.setup(600, 600)

#koch
mozart = turtle.Turtle()
mozart.pd()
#sierPINKsi
bach = turtle.Turtle()
bach.pd()
#treee
beethoven = turtle.Turtle()
beethoven.pd()


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