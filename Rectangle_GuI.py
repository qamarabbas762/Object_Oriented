import turtle

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self,rectangle):
        if rectangle.lowleft.x<self.x<rectangle.upright.x and rectangle.lowleft.y<self.y<rectangle.upright.y:
            return True
        else:
            return False

    def distance(self,newx,newy):
        import math
        distx = newx-self.x
        disty = newy-self.y
        dist = math.sqrt(math.pow(distx,2)+math.pow(disty,2))
        return dist


class Rectnagle:

    def __init__(self,lowleft,upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        area = 0.5*(self.upright.x-self.lowleft.x)*(self.upright.y-self.lowleft.y)
        return area


class GuiRectangle(Rectnagle):

    def draw(self,canvas):
        canvas.penup()
        canvas.goto(rectangle.lowleft.x,rectangle.lowleft.y)

        canvas.pendown()
        canvas.forward(rectangle.upright.x-rectangle.lowleft.x)
        canvas.left(90)
        canvas.forward(rectangle.upright.y-rectangle.lowleft.y)
        canvas.left(90)
        canvas.forward(rectangle.upright.x-rectangle.lowleft.x)
        canvas.left(90)
        canvas.forward(rectangle.upright.y-rectangle.lowleft.y)



class GuiPoint(Point):

    def draw_point(self,canvas):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot()




from random import randint

rectangle = GuiRectangle(Point(randint(100,300),randint(100,300)),
                      Point(randint(300,500),randint(300,500)))




print("The Rectangle coordinates are",
      rectangle.lowleft.x,",",rectangle.lowleft.y,"and",
      rectangle.upright.x,rectangle.upright.y)

point = GuiPoint(float(input("Enter your value of x: ")),
                 float(input("Enter your value of y: ")))

canvas = turtle.Turtle()

rectangle.draw(canvas)

point.draw_point(canvas)

turtle.done()




# print("The Rectangle coordinates are",
#       rectangle.lowleft.x,",",rectangle.lowleft.y,"and",
#       rectangle.upright.x,rectangle.upright.y)
#
# user_point = Point(float(input("Enter your value of x")),
#                    float(input("Enter your value of y")))
#
# print("The point falls in rectangle:",user_point.falls_in_rectangle(rectangle))
#
# print("Now guess the area of the rectangle")
#
# user_area = float(input("Please enter your guess: "))
#
# if user_area == rectangle.area():
#     print("You guessed it right, the area of the rectangle is ",rectangle.area())
#
# else:
#     print("You guessed it wrong !!!!!","\n",
#           "the area of the rectangle is: ",rectangle.area()
#          )

