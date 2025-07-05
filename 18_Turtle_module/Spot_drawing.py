import turtle as t
import random as r
import colorgram as co

rgb_colors=[(0,0,0)]
image= "dot_drawing.jpg"
colors= co.extract(image, 20)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

cursor = t.Turtle()
screen = t.Screen()
ancho = screen.window_width()
alto = screen.window_height()
print(ancho, alto)
# Mover a la esquina inferior izquierda
x = -ancho / 3 + 50
y = -alto / 3 +20
cursor.up()
initial_pos=(x,y)
t.colormode(255)
t.tracer(0) #Just for going faster
cursor.up()
cursor.hideturtle()
for col in range(0, 10):
    cursor.goto(initial_pos[0], initial_pos[1] + 60 * col)
    for row in range(0, 10):
        cursor.down()
        cursor.color(r.choice(rgb_colors))
        cursor.dot(30)
        cursor.up()
        cursor.forward(60)
    cursor.goto(initial_pos[0], initial_pos[1]+60*col)
t.tracer(1)
cursor.hideturtle()
screen.exitonclick()
