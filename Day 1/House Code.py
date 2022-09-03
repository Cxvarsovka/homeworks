from turtle import *

speed(60)

# House Wallls

width(5)
begin_fill()
color("green")
forward(250)
left(90)
forward(250)
left(90)
forward(250)
left(90)
forward(250)
end_fill()



# Door
left(90)
forward(74)


color("black")
begin_fill()
left(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()

# Windows

# Window 1

penup()
goto(100,140)
pendown()

color("blue")
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)

right(90)
forward(35)
right(90)
forward(70)
right(180)
forward(35)
right(90)
forward(35)
left(180)
forward(70)

# Window 2

penup()
goto(150,140)
pendown()

left(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(180)
forward(35)
left(90)
forward(70)
left(180)
forward(35)
right(90)
forward(35)
left(180)
forward(70)

# Roof

color("red")

penup()
goto(250,250)
pendown()


begin_fill()

left(130)
forward(200)

left(101)
forward(200)

left(130)
forward(250)

end_fill()

exitonclick()