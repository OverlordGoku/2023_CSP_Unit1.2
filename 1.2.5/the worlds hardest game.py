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
box.shape("square")
box.color("red")
box.shapesize(5)
box.left(180)
box.forward(100)
box.right(90)
box.forward(130)


#keypress
def w():
        runner.forward(45)

def s():
    runner.back(45)

def a():
    runner.left(45)

def d():
    runner.right(45)


#box movement
for movement in range(10000):
    box.right(180)
    box.forward(300)


#listen for keypress
wn.onkeypress(w, "w")
wn.onkeypress(s, "s")
wn.onkeypress(a, "a")
wn.onkeypress(d, "d")


wn.listen()
wn.mainloop()

