import turtle

screen=turtle.Screen()
screen.bgcolor("Purple")
screen.title("Catch The Turtle")
FONT=("Arial",30,"normal")


def skor_gösterme():
  skor=turtle.Turtle()
  skor.penup()
  skor.hideturtle()
  skor.color("White")

  en_üst = screen.window_height() / 2
  y = en_üst * 0.9
  skor.setpos(0,y)
  skor.write(arg="Score: 0" , move=False , align="center" , font=FONT)


skor_gösterme()


turtle.mainloop()