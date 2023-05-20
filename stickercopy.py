import turtle

chirag = turtle.Turtle()
chirag.hideturtle()
chirag.pensize(3)
chirag.speed(10)

chirag.penup()
chirag.setpos(100, -300)
chirag.pendown()

# body right
chirag.left(90)
for i in range(30):
    chirag.forward(2)
    chirag.left(0.2)

chirag.color("black", "brown")
chirag.begin_fill()
# tail start
chirag.setheading(20)
chirag.circle(150, 50)

chirag.circle(7, 180)

# tail
chirag.setheading(230)

for i in range(18):
    chirag.forward(2)
    chirag.left(0.8)
for i in range(51):
    chirag.forward(1.5)
    chirag.right(1)
chirag.end_fill()

# body right above tail
chirag.setheading(270)
chirag.forward(25)

chirag.setheading(90)

for i in range(80):
    chirag.forward(2)
    chirag.left(0.2)

chirag.penup()
chirag.setheading(180)
chirag.pendown()

chirag.forward(20)
chirag.penup()
chirag.backward(20)

chirag.pendown()
chirag.penup()
chirag.setheading(0)

# face right
chirag.pendown()
chirag.forward(30)
chirag.circle(120, 90)
chirag.forward(40)


chirag.color("black", "pink")
chirag.begin_fill()
# right ear
# ear half
chirag.setheading(45)
for i in range(30):
    chirag.forward(1.5)
    chirag.left(0.4)
for i in range(30):
    chirag.forward(2)
    chirag.left(0.9)


chirag.setheading(145)

# ear rest
for i in range(40):
    chirag.forward(2)
    chirag.left(1)
chirag.end_fill()

chirag.penup()
chirag.right(40)
chirag.pendown()

# head
chirag.setheading(120)
chirag.circle(230, 100)
chirag.setheading(135)

chirag.color("black", "pink")
chirag.begin_fill()
# ear left start
for i in range(100):
    chirag.left(0.5)
    chirag.forward(1)

chirag.setheading(270)

# ear left down
for i in range(80):
    chirag.left(0.2)
    chirag.forward(1)
chirag.end_fill()


# left face start
chirag.setheading(250)
for i in range(30):
    chirag.forward(2)
    chirag.left(1)

for i in range(20):
    chirag.forward(2)
    chirag.right(0.3)

# lower face
chirag.setheading(245)
chirag.circle(125, 90)

# arm start
chirag.setheading(220)
for i in range(15):
    chirag.forward(2)
    chirag.left(0.6)

# arm turn
chirag.circle(20, 160)

chirag.right(10)
# left arm
for i in range(60):
    chirag.forward(1)
    chirag.right(0.2)

chirag.setheading(120)
for i in range(30):
    chirag.forward(1)
    chirag.left(0.6)
chirag.setheading(180)
chirag.forward(25)

# position change
chirag.penup()
chirag.backward(25)
chirag.pendown()

# right arm
chirag.setheading(40)
chirag.forward(10)
for i in range(12):
    chirag.forward(2)
    chirag.right(9)
chirag.setheading(340)
for i in range(30):
    chirag.forward(2)
    chirag.left(0.4)

# left arm lower portion
chirag.penup()
chirag.setheading(270)
chirag.forward(50)
chirag.pendown()
chirag.setheading(150)
for i in range(80):
    chirag.forward(1)
    chirag.right(0.02)

# eyes and googles nd spot near eyes
# changing location
chirag.penup()
chirag.setheading(90)
chirag.forward(250)
chirag.setheading(180)
chirag.forward(50)
chirag.pendown()

# drawing left google
chirag.circle(60)
chirag.penup()
chirag.setheading(270)
chirag.forward(20)
chirag.setheading(0)
chirag.forward(40)
chirag.pendown()
chirag.forward(150)

# drawing right google
chirag.penup()
chirag.setheading(270)
chirag.forward(35)
chirag.setheading(180)
chirag.forward(8)
chirag.setheading(270)
chirag.pendown()
chirag.circle(60)

# drawing right eye
chirag.penup()
chirag.setheading(270)
chirag.forward(12.5)
chirag.setheading(0)
chirag.forward(60)
chirag.pendown()
chirag.color("black", "black")
chirag.begin_fill()
chirag.circle(20)
chirag.end_fill()

# drawing right eye

chirag.penup()
chirag.setheading(270)
chirag.forward(3)
chirag.setheading(180)
chirag.forward(230)
chirag.setheading(0)
chirag.pendown()
chirag.color("black", "black")
chirag.begin_fill()
chirag.circle(20)
chirag.end_fill()

chirag.color("pink", "pink")
chirag.begin_fill()
# drawing right eye spot
chirag.penup()
chirag.setheading(180)
chirag.forward(30)
chirag.pendown()
chirag.circle(12)
chirag.end_fill()


# drawing right spot
chirag.color("pink", "pink")
chirag.begin_fill()
chirag.penup()
chirag.setheading(0)
chirag.forward(285)
chirag.setheading(180)
chirag.pendown()
chirag.circle(12)
chirag.end_fill()
chirag.color("black")

# mouth
chirag.penup()
chirag.setheading(180)
chirag.forward(160)
chirag.pendown()
chirag.setheading(270)
chirag.circle(11, 180)
chirag.setheading(270)
chirag.circle(11, 180)

chirag.penup()
chirag.goto(-160, -300)
chirag.pendown()
chirag.setheading(90)
for i in range(90):
    chirag.forward(2)
    chirag.left(0.1)
turtle.done()
