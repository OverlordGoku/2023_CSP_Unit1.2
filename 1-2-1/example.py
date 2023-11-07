import turtle as trtl
test = trtl.Turtle

def drawtriangle():
    test.pendown()
    test.fd(100)
    test.right(120)
    test.fd(100)
    test.right(120)
    test.fd(100)

def drawtriangle(long, x, y):
    test.penup()
    test.goto(x,y)
    test.pendown()
    test.fd(long)





    x = 100
    y = 100
    length = 43
    for tri in range(100):
        drawtriangle(length,x,y)
        x += length * 1.25
        y += length * 1.25




drawtriangle()
wn = trtl.Screen()
wn.mainloop()