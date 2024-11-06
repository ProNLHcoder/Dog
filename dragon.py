import turtle

t = turtle.Turtle()
window = turtle.Screen()
t.speed("fastest")

# this function draws a dragon scale
def scale():
	t.circle(50, 180)
	t.left(90)
	t.forward(100)

# Making the face
t.goto(0,0)
t.fillcolor("saddle brown")
t.begin_fill()
t.circle(150)
t.end_fill()

# making the mouth
t.penup()
t.forward(-50)
t.left(90)
t.forward(100)
t.right(90)
t.fillcolor("red")
t.begin_fill()	
t.right(90)
scale()
t.end_fill()
t.fillcolor("black")
t.begin_fill()
t.backward(50)
t.left(90)
scale()
t.end_fill()
t.fillcolor("black")
t.begin_fill()
t.forward(100)
t.left(90)
scale()
t.end_fill()
t.fillcolor("black")
t.begin_fill()
t.right(90)
t.penup()
t.forward(25)
t.right(90)
t.forward(50)
t.pendown()
t.left(270)
t.fillcolor("black")
t.begin_fill()
scale()
t.end_fill()
t.fillcolor("black")
t.begin_fill()

# making the eyes
t.penup()
t.right(45)
t.forward(50)
t.pendown()
t.circle(25) 
t.end_fill()
t.fillcolor("black")
t.begin_fill()
t.penup()
t.setheading(0)
t.forward(200)
t.left(135)
t.pendown()
t.circle(25)
t.end_fill()

# making the left ear
t.fillcolor("saddle brown")
t.penup()
t.goto(0,300)
t.left(45)
t.right(180)
t.circle(150,-30)
t.backward(100)
t.pendown()
t.left(15)
t.begin_fill()
t.circle(-100, 80)
t.penup()
t.left(40)
t.backward(126)
t.pendown()
t.circle(-180, 60)
t.end_fill()
t.fillcolor("pink")
t.begin_fill()
t.right(180)
t.circle(180, 60)
t.right(180)
t.forward(125)
t.end_fill()
t.right(-90)
t.penup()
t.left(55)
t.goto(100,270)
t.right(45)
t.pendown()
t.fillcolor("saddle brown")
t.begin_fill()
t.backward(5)
t.forward(135)
t.left(135)
t.circle(100, 90)
t.end_fill()
t.fillcolor("saddle brown")
t.begin_fill()
t.left(135)
t.forward(140)
t.right(180)
t.circle(180, 60)
t.right(210)
t.forward(180)
t.right(180)
t.end_fill()
t.forward(180)
t.fillcolor("pink")
t.begin_fill()
t.right(150)
t.circle(-180, 60)
t.right(180)
t.forward(135)
t.end_fill()
turtle.done()