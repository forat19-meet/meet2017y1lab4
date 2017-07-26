for i in range (100):
    count = i+i
    if count % 3 == 0:
        print('fizz')
    else:
        print('count')
        
for i in range(100):
     count = i + i
     print(count)

     
import turtle

num_pts = 5
for i in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)

turtle.mainloop()
    
import turtle
x=0
while x<300:
    y=x**2/300
    turtle.goto(x,y)
    x = x + 1

turtle.mainloop()
