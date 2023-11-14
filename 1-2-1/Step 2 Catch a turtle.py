# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
tri = trtl.Turtle
wn = trtl.Screen()

#-----game configuration----
tri_color = "red"
#-----initialize turtle-----
tri = trtl.Turtle()
tri.color(tri_color)
tri.shape("triangle")
tri.shapesize(10)

#-----game functions--------
def tri_clicked(x,y):
    print("tri_clicked!")
    change_position()
    new_xpos = x
    new_ypos = y
    tri.goto(new_xpos, new_ypos)
def change_position():
    x = rand.randint(1,400)
    y = rand.randint(1,300)
    tri.goto(x,y)
#-----events----------------
tri.onclick(tri_clicked)
trtl.Screen()
wn.mainloop()