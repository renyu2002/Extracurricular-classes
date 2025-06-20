import turtle

# 设置画布和画笔
screen = turtle.Screen()
screen.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(100)  # 设置绘制速度

# 绘制房子主体
def draw_house_body():
    pen.penup()
    pen.goto(-100, -100)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(200)
        pen.left(90)
    pen.end_fill()

# 绘制屋顶
def draw_roof():
    pen.penup()
    pen.goto(-120, 100)
    pen.pendown()
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.goto(0, 200)
    pen.goto(120, 100)
    pen.goto(-120, 100)
    pen.end_fill()

# 绘制门
def draw_door():
    pen.penup()
    pen.goto(-20, -100)
    pen.pendown()
    pen.fillcolor("brown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(40)
        pen.left(90)
        pen.forward(60)
        pen.left(90)
    pen.end_fill()

# 绘制窗户
def draw_windows():
    # 左侧窗户
    pen.penup()
    pen.goto(-70, 0)
    pen.pendown()
    pen.fillcolor("lightblue")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    
    # 右侧窗户
    pen.penup()
    pen.goto(30, 0)
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()

# 绘制烟囱
def draw_chimney():
    pen.penup()
    pen.goto(70, 100)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
    pen.end_fill()

# 绘制烟
def draw_smoke():
    pen.penup()
    pen.goto(80, 140)
    pen.pendown()
    pen.color("gray")
    pen.pensize(3)
    pen.circle(10)
    pen.penup()
    pen.goto(95, 155)
    pen.pendown()
    pen.circle(12)
    pen.penup()
    pen.goto(110, 170)
    pen.pendown()
    pen.circle(14)

# 绘制太阳
def draw_sun():
    pen.penup()
    pen.goto(200, 200)
    pen.pendown()
    pen.color("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()

# 绘制草地
def draw_grass():
    pen.penup()
    pen.goto(-300, -100)
    pen.pendown()
    pen.color("green")
    pen.fillcolor("green")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(600)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
    pen.end_fill()

# 绘制花朵
def draw_flower(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("green")
    pen.pensize(2)
    pen.goto(x, y + 20)
    
    # 花朵中心
    pen.penup()
    pen.goto(x, y + 20)
    pen.pendown()
    pen.color("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(3)
    pen.end_fill()
    
    # 花瓣
    colors = ["red", "orange", "pink", "purple"]
    for color in colors:
        pen.penup()
        pen.goto(x, y + 20)
        pen.pendown()
        pen.color(color)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(5)
        pen.end_fill()
        pen.right(90)

# 执行绘制
draw_grass()
draw_house_body()
draw_roof()
draw_door()
draw_windows()
draw_chimney()
draw_smoke()
draw_sun()

# 绘制几朵花
draw_flower(-200, -150)
draw_flower(-150, -160)
draw_flower(-100, -140)
draw_flower(100, -150)
draw_flower(150, -160)
draw_flower(200, -140)

# 完成绘制
pen.hideturtle()
screen.exitonclick()
