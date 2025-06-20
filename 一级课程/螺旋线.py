import turtle

turtle.setup(600, 400)
turtle.bgcolor('black')
turtle.title('黑色背景画布')

turtle.speed("fastest")
turtle.pensize(2)#画笔像素
turtle.color('white')
turtle.shape('circle')

for i in range(100): #绘画100次
    turtle.forward(2*i)
    turtle.left(91) #绘画矩形的一条边

turtle.done()#结束绘制

