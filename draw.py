import turtle
from PIL import Image
from PIL import EpsImagePlugin
import io

t = turtle.Turtle()
t.hideturtle()
turtle.tracer(False)

# font
font = "Arial"
size = 20
format = "normal"

# Size
radius = 50

# Values
name = "A"
duration = 10
es = 0
ef = 0
ls = 0
lf = 0

# Coords
x = 0
y = 0
dock_right = x + radius
dock_left = x - radius

# ----------------------------------------- Circle ----------------------------------------- #
t.penup()
t.goto(x, y - radius)
t.pendown()

t.circle(radius)

# ----------------------------------------- Cross ----------------------------------------- #
# 20% of radius
padding = round(radius * 0.2 / 2)
length = round(radius * 0.8)

# top down line
t.penup()
t.goto(x, y - padding)
t.pendown()
t.goto(x, y - padding - length)

# right left line
t.penup()
t.goto(x + length / 2 , y - radius / 2)
t.pendown()    
t.goto( t.xcor() - length , t.ycor())

t.penup()

# ----------------------------------------- Text ----------------------------------------- #

# Name
t.goto(x - (radius / 3) , y + radius / 4)
t.write(name, align="center", font=(font, size, format))

# Duration
t.goto(x + radius / 3 , y + radius / 4)
t.write(duration, align="center", font=(font, size, format))

'''

ES | EF
-------
LS | LF

'''
# ES
t.goto(x - radius / 4 , y - radius / 2 )
t.write(es, align="center", font=(font, size, format))

# EF
t.goto(x + radius / 4 , y - radius / 2 )
t.write(ef, align="center", font=(font, size, format))

# LS
t.goto(x - radius / 4 , y - radius)
t.write(ls, align="center", font=(font, size, format))

# LF
t.goto(x + radius / 4 , y - radius)
t.write(lf, align="center", font=(font, size, format))

# ----------------------------------------- Save as PNG ----------------------------------------- #

ps = t.getscreen().getcanvas().postscript(colormode="color")
EpsImagePlugin.gs_windows_binary = "./Ghostscript/gs10.03.0/bin/gswin64c.exe"
im = Image.open(io.BytesIO(ps.encode("utf-8")))
im.save('RED.png', format="PNG")