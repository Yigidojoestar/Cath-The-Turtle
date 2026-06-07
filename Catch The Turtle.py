import turtle
import random

screen=turtle.Screen()
screen.bgcolor("Purple")
screen.title("Catch The Turtle")
FONT=("Arial",30,"normal")
score = 0
game_over = False
x_coordinates=[-400,-200,0,200,400]
y_coordinates=[0,300,150,-150,-300]
turtle_list = []
skor=turtle.Turtle()
skor.penup()
skor.hideturtle()
skor.color("White")
countdown_turtle=turtle.Turtle()

def skor_gösterme():


  en_üst = screen.window_height() / 2
  y = en_üst * 0.9
  skor.setpos(0,y)
  skor.write(arg="Score: 0" , move=False , align="center" , font=FONT)

def kaplumbaga(x , y):
    t1=turtle.Turtle()

    def click(x, y):
        global score
        score += 1
        skor.clear()
        skor.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t1.onclick(click)
    t1.penup()
    t1.speed(100000000)
    t1.shape("turtle")
    t1.shapesize(2,2)
    t1.color("Green")
    t1.setpos(x, y)
    turtle_list.append(t1)

def kaplumbaga_yerleştirme():
  for x in x_coordinates:
      for y in y_coordinates:
          kaplumbaga(x,y)

def hide_turtles():
    for turtle in turtle_list:
        turtle.hideturtle()

def show_turtles_randomly():
    if not  game_over:
     hide_turtles()
     random.choice(turtle_list).showturtle()
     screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("White")

    en_üst = screen.window_height() / 2
    y = en_üst * 0.9
    countdown_turtle.setpos(0, y -50)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Overinho!", move=False, align="center", font=FONT)



def oyun():
 turtle.tracer(0)
 skor_gösterme()
 kaplumbaga_yerleştirme()
 hide_turtles()
 show_turtles_randomly()
 countdown(10)


oyun()

turtle.tracer(1)

turtle.mainloop()
