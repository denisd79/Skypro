import turtle

window = turtle.Screen()
window.bgcolor('skyblue')

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

# Нарисуем тело рыбы
my_turtle.color("yellow")
my_turtle.begin_fill()
my_turtle.circle(75)
my_turtle.end_fill()

# Переместим черепаху в позицию под плавником
my_turtle.penup()
my_turtle.goto(-50, -100)
my_turtle.pendown()

# Нарисуем хвост рыбы
my_turtle.color("yellow")
my_turtle.begin_fill()
my_turtle.right(150)
my_turtle.forward(100)
my_turtle.left(150)
my_turtle.forward(100)
my_turtle.left(150)
my_turtle.forward(100)
my_turtle.hideturtle()
my_turtle.end_fill()

turtle.done()