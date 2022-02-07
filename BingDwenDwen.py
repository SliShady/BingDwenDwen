import turtle as t
import math

# 设置速度
t.speed(100)  # 速度
t.delay(10)  # 延迟
# turtle.tracer(False)
# 双耳
# 左耳
t.penup()
t.goto(-150, 200)
t.setheading(160)
t.begin_fill()
t.pendown()
t.circle(-30, 230)
t.setheading(180)
t.circle(37, 90)
t.end_fill()
# 右耳
t.penup()
t.goto(60, 200)
t.setheading(20)
t.begin_fill()
t.pendown()
t.circle(30, 230)
t.setheading(0)
t.circle(-37, 90)
t.end_fill()
# 头
t.pensize(5)
t.penup()
t.goto(-113, 237)
t.setheading(30)
t.pendown()
t.circle(-134, 60)

t.penup()
t.goto(-150, 200)
t.setheading(-120)
t.pendown()
t.circle(200, 80)

t.penup()
t.goto(60, 200)
t.setheading(-60)
t.pendown()
t.circle(-200, 80)

t.penup()
t.setheading(210)
t.pendown()
t.circle(-120, 60)
# 双眼
# 左眼
# 眼圈
t.penup()
t.goto(-140, 100)
t.setheading(-45)
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(-103, 125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(13, 360)
t.end_fill()
# 眼珠
t.fillcolor("sienna")
t.pencolor("sienna")
t.penup()
t.goto(-102, 133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(5, 360)
t.end_fill()
# 右眼
# 眼圈
t.penup()
t.goto(50, 100)
t.setheading(45)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(13, 125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(13, 360)
t.end_fill()
# 眼珠
t.fillcolor("sienna")
t.pencolor("sienna")
t.penup()
t.goto(12, 133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(5, 360)
t.end_fill()
# 鼻子
t.pencolor("black")
t.fillcolor("black")
t.penup()
t.goto(-55, 133)
t.begin_fill()
t.pendown()
t.fd(20)
t.seth(-120)
t.fd(20)
t.seth(120)
t.fd(20)
t.end_fill()
# 嘴
t.penup()
t.goto(-70, 110)
t.setheading(-30)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(50, 60)
t.setheading(-120)
t.circle(-100, 15)
t.circle(-15, 90)
t.circle(-100, 15)
t.end_fill()
# 四肢
# 左臂
t.penup()
t.goto(-175, 100)
t.fillcolor("black")
t.begin_fill()
t.setheading(-120)
t.pendown()
t.fd(100)
t.setheading(-110)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 右臂
t.penup()
t.goto(85, 100)
t.setheading(60)
t.begin_fill()
t.pendown()
t.fd(100)
t.setheading(70)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 小红心
t.penup()
t.pencolor("red")
t.fillcolor('red')
t.goto(105, 200)
t.begin_fill()
t.pendown()
t.circle(-5, 180)
t.setheading(90)
t.circle(-5, 180)
t.setheading(-120)
t.fd(17)
t.penup()
t.goto(105, 200)
t.pendown()
t.setheading(-60)
t.fd(17)
t.end_fill()
t.pencolor("black")
t.fillcolor("black")
# 左腿
t.penup()
t.goto(-120, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(-140, 20)
t.circle(5, 109)
t.fd(30)
t.circle(10, 120)
t.setheading(90)
t.circle(-140, 10)
t.end_fill()
# 右腿
t.penup()
t.goto(30, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(140, 20)
t.circle(-5, 109)
t.fd(30)
t.circle(-10, 120)
t.setheading(90)
t.circle(140, 10)
t.end_fill()
# 冰糖外壳
t.pensize(1)
t.penup()
t.goto(-160, 195)
t.setheading(160)
t.pendown()
t.circle(-40, 230)
t.setheading(30)
t.circle(-134, 58)
t.setheading(60)
t.circle(-40, 215)
t.setheading(-60)
t.fd(15)
t.circle(2, 200)
t.setheading(65)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.circle(2, 25)
t.circle(-200, 47)
t.circle(2, 60)
t.circle(140, 23)
t.circle(-2, 90)
t.setheading(180)
t.fd(70)
t.circle(-2, 90)
t.fd(30)
t.setheading(-160)
t.circle(-100, 35)
t.setheading(-90)
t.fd(30)
t.circle(-2, 90)
t.fd(70)
t.circle(-2, 90)
t.setheading(60)
t.circle(140, 30)
t.circle(2, 45)
t.circle(-200, 19)
t.circle(2, 130)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.setheading(90)
t.circle(-200, 30)
# 冰糖面罩
t.pensize(3)
t.penup()
t.goto(65, 120)
t.setheading(90)
t.pendown()
t.pencolor("red")
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
        a = a + 0.25
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.25
        t.lt(3)
        t.fd(a)
t.pencolor("orange")
t.penup()
t.goto(66, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.255
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.255
        t.lt(3)
        t.fd(a)
t.pencolor("green")
t.penup()
t.goto(67, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.2555
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.2555
        t.lt(3)
        t.fd(a)
t.pencolor("deep sky blue")
t.penup()
t.goto(68, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.25955
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.25955
        t.lt(3)
        t.fd(a)
t.pencolor("pink")
t.penup()
t.goto(71, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.26
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.26
        t.lt(3)
        t.fd(a)
t.pencolor("purple")
t.penup()
t.goto(72, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.269
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.269
        t.lt(3)
        t.fd(a)

# 五环
t.penup()
t.goto(-55, -10)
t.pendown()
t.pencolor("blue")
t.circle(10)
t.penup()
t.goto(-40, -10)
t.pendown()
t.pencolor("black")
t.circle(10)
t.penup()
t.goto(-25, -10)
t.pendown()
t.pencolor("red")
t.circle(10)
t.penup()
t.goto(-50, -20)
t.pendown()
t.pencolor("yellow")
t.circle(10)
t.penup()
t.goto(-30, -20)
t.pendown()
t.pencolor("green")
t.circle(10)

t.done()