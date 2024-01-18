import turtle as trtl
wn = trtl.Screen()
runner = trtl.Turtle()
box = trtl.Turtle()
wn.bgpic("bg2.gif")


runner.penup()

#turtle position setup
runner.right(180)
runner.forward(420)
runner.right(180)

#box setup
box.penup()
box.shape("square")
box.shapesize(5)
box.goto(400, -50)


#keypress
def w():
    runner.forward(20)
    win()
def s():
    runner.back(20)
    win()
def a():
    runner.left(45)
    win()
def d():
    runner.right(45)
    win()

#Game win event

def win():
    if runner.xcor() >= 400:
        print("you win")

    if runner.ycor() >= 20:
        print("you win")



#listen for keypress
wn.onkeypress(w, "w")
wn.onkeypress(s, "s")
wn.onkeypress(a, "a")
wn.onkeypress(d, "d")


wn.listen()
wn.mainloop()

