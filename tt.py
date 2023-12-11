import streamlit as st
import matplotlib.pyplot as plt 

fig, ax = plt.subplots()

c1 = st.sidebar.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'purple', 'orange'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오', ['-', '--', '-,'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

love= []
y = []
for i in range(-20, 21, 3):
    love.append(i)
    y. append(-2*i*i + 3*i + 5)

plt.plot(love, y, color = c1, linestyle = s1, marker = m1)
st.pyplot(fig)
# c1 = st.radio('선의 색을 선택하시오',['red', 'green', 'blue'])


# fig, ax = plt.subplots()

# x = []
# y = []
# ysin = []
# for i in range(-20, 21, 1):
#     x.append(i)
#     y.append(3*i*i - 5*i + 2)
#     ysin.append(1200*np.sin(i))


# plt.plot(x, y, color = c1, label = '2nd equation')
# plt.plot(x, ysin, color = c1, label = 'sin function')
# plt.legend()
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.xlim([-15, 15])
# plt.ylim([-2000, 2000])

# st.pyplot(fig)


# import sys
# sys.exit()
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# x = []
# for  i in range(-100, 100):
#     x.append(i/10.0)

# y = []
# a = 2
# b = -1
# c = 5

# col = st. columns(3)
# with col[0]:
#     a = st.number_input('Insert a', step = 1)
# with col[1]:
#     b = st.number_input('insert b', step = 1)
# with col[2]:
#     c = st.number_input('insert c', step = 1)







# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.color((77/255, 239/253, 93/255))
# t.forward(100)
# turtle.done() 


# s = [3, 7, 1, 15, -6, 8, 0]
# s


# s1 = 1
# s2 = 2
# s3 = 3
# s4 = 4
# s5 = 5
# s1, s2, s3, s4, s5

# s = ['a','b', 'c', 'd', 'e']

# s.append('사과')
# s.remove('c')
# s
# i = s.index('d')
# i


# for item in s:
#     item

# import turtle
# import random
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed(0)
# t.pensize(10)

# def tree(length):
#     if length > 10:
#         t.forward(length)
#         t.right(20)
#         tree(length-8)
#         t.left(40)
#         tree(length-8)
#         t.right(20)
#         t.backward(length)
# t.left(90)
# t.color("black")
# tree(90)    
# t.goto(0,0)

# sh = 5
# def shape(sh):
#     for j in range(sh):
#         t.forward(1+5*i)
#         t.left(360/sh)

# while True:
#     for i in range(30):
#         if i < 10:
#             shape(3)
#         elif i < 20 :
#             shape(4)
#         elif i < 30:
#             shape(5)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20,0)
#     t.clear()    
# turtle.done() 











# import turtle
# import random
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(30):
#         t.circle(1+5*i)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20,0)
#     t.clear()    
# turtle.done() 

# -
# import turtle
# import math
# import random

# player = turtle.Turtle()
# player.shape("turtle")
# screen = player.getscreen()
# screen.bgcolor("black")
# screen.setup(800, 600)
# player.color("yellow")

# player.goto(-300, 0)
# velocity = 70
# player.left(45)

# def turnleft():
#     player.left(5)

# def turnright():
#     player.right(5)

# def turnup():
#     global velocity
#     velocity += 10

# def turndown():
#     global velocity
#     velocity -= 10

# def fire():
#     x = -300
#     y = 0
#     player.color(random.random(),random.random(),random.random())
#     player.goto(x, y)
#     angle = player.heading()
#     vx = velocity * math.cos(angle * 3.14 / 180.0)
#     vy = velocity * math.sin(angle * 3.14 / 180.0)
#     while player.ycor() >= 0 :
#         vx = vx
#         vy = vy - 10
#         x = x + vx
#         y = y + vy
#         player.goto(x, y)
#         player.stamp

# screen.onkeypress(turnleft, "Left")
# screen.onkeypress(turnright, "Right")
# screen.onkeypress(turnup, "Up")
# screen.onkeypress(turndown, "Down")
# screen.onkeypress(fire, "space")

# screen.listen
# turtle.mainloop


# import time
# import random as r

# for i in range(6):
#     a1 = r.randint(1,45)
#     a1

# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed(10)
# t.width(5)
# # def square(x,y, length):
# def rec(x, y, lx, ly):
#     t.up()
#     t.goto(x,y)
#     t.down()
#     for i in range(4):
#         t.forward(lx)
#         t. left(90)
#         t.forward(ly)
#         t.left(90)

#         # t.forward(length)
#         # t.left(90)


# rec(-200, 0,100,50)
# rec(0,0,100,150)
# rec(200,0,100,100)
# # square(-200,0,100)
# # square(0,0,100)
# # square(200,0,100)
# turtle.done() 


# def user_sum(n):
#     s=0
#     for i in range(1,n+1):
#         s = s + i
#         s

# user_sum(100)
# user_sum(200)


# '나는'+ '12' + '개의 사과를 먹었다'
# # for i in range(1,10):
# #     if 1%3==1:
# #         i

# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed(10)
# t.width(3)
# t.pencolor('gray')
# colors = ('red','purple', 'blue', 'yello', 'orange', 'green')
# length = 40

# for i in range(100):
#     t. forward(length)
#     t. right(60)
#     length +=5
# # n=40
# ang=360/n

# for i in range(n):
#     t.circle(80)
#     t.left(ang)
# t.circle(60)
# t.left(60)
# t.circle(60)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(60)
# distance = 150
# angle = 120
# for i in range(3):
#     t. forward(distance)
#     t.left(angle)
# turtle.done()


# s=50
# if s >=90:
#     '귀하의 점수는' + str(s) + '점으로 :red[A등급]입니다'
# elif s>=80:
#     '귀하의 점수는' + str(s) + '점으로 :green[B등급]입니다'
# elif s>=70:
#     '귀하의 점수는' + str(s) + '점으로 :blue[C등급]입니다'
# elif s>=60:
#     '귀하의 점수는' + str(s) + '점으로 :yello[D등급]입니다'
# else :
#     '귀하의 점수는' + str(s) + '점으로 :gray[F등급]입니다'


# a=0.1+0.
# a==0.3
  

# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed(2)
# size = 200

# t.left(60)
# t.fd(size)
# t.right(120)
# t.fd(size)

# t.right(30)
# t.fd(size)
# t.right(90)
# t.fd(size)
# t.right(90)
# t.fd(size)
# t.right(90)
# t.fd(size)

# turtle.done()




# r= 30
# area = 3.14*r*r
# area


# distance = 150
# angle = 120
# for i in range(3):
#     t. forward(distance)
#     t.left(angle)

# turtle.done()



# a = 3.141592*10*10.0
# b = (1/100)*1234*55

# print("hello")

# st.write("hello")

# st.write("강아지 + 고양이")

# st.write("반가워요")
# print(a,b)
# a,b