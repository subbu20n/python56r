import turtle
Turtle = turtle.Turtle()
windows = turtle.Screen()

for i in range(0,5): 
    Turtle.forward(200) 
    Turtle.right(90)


import turtle
Turtle = turtle.Turtle()
windows = turtle.Screen()

# to draw a spiral 
def draw_spiral(myTurtle,linelen):
    Turtle.forward(linelen)
    Turtle.right(90) 
    draw_spiral(Turtle, linelen - 10)  
    draw_spiral(Turtle,80) 
window.exitonclick()
