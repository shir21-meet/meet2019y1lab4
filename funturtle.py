import turtle
turtle.bgcolor('purple')
turtle.color('yellow')
turtle.shape('circle')
turtle.pensize(5)
shir=turtle.clone()
shir.pensize(10)
shir.color('green')
shir.shape('triangle')
turtle.goto(0,130)
shir.goto(0,-130)
turtle.goto(-60,130)
shir.goto(60,-130)
turtle.color('white')
shir.color('blue')
turtle.left(90)
shir.left(90)
turtle.goto(-60,0)
shir.goto(60,0)
turtle.mainloop()
