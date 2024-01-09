import turtle as trtl
wn = trtl.Screen()
runner = trtl.Turtle
wn.bgpic("background.gif")
runner.penup()

#keypress
def w():
    runner.forward(45)

def s():
    runner.back(45)

def a():
    runner.left(45)

def d():
    runner.right(45)



#listen for keypress
wn.onkeypress(w, "Up")
wn.onkeypress(s, "down")
wn.onkeypress(a, "Left")
wn.onkeypress(d, "Right")


wn.listen()
wn.mainloop()

