import turtle
import random

screen=turtle.Screen()
screen.bgcolor("Purple")
screen.title("Catch The Turtle")
FONT=("Arial",30,"normal")

turtle_list = []

def skor_gösterme():
  skor=turtle.Turtle()
  skor.penup()
  skor.hideturtle()
  skor.color("White")

  en_üst = screen.window_height() / 2
  y = en_üst * 0.9
  skor.setpos(0,y)
  skor.write(arg="Score: 0" , move=False , align="center" , font=FONT)

def kaplumbaga(x , y):
    t1=turtle.Turtle()

    t1.penup()
    t1.speed(100000000)
    t1.shape("turtle")
    t1.shapesize(2,2)
    t1.color("Green")
    t1.setpos(x, y)
    turtle_list.append(t1)

x_coordinates=[-400,-200,0,200,400]
y_coordinates=[0,300,150,-150,-300]

def kaplumbaga_yerleştirme():
  for x in x_coordinates:
      for y in y_coordinates:
          kaplumbaga(x,y)

def hide_turtles():
    for turtle in turtle_list:
        turtle.hideturtle()

def show_turtles_randomly():
    random.choice(turtle_list).showturtle()


turtle.tracer(0)


skor_gösterme()
kaplumbaga_yerleştirme()
hide_turtles()
show_turtles_randomly()


turtle.tracer(1)

turtle.mainloop()
