#note: better to run this kind of stuff in jupyter, even tho jupyter sometimes sucks, there is a difference 
#when methods are ran on shll as opposed to a python interpreter
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def surface(self):
        return 2*(self.width +self.height)

    def area(self):
        return self.width * self.height
    



#what we are doing is we overried the already existing special method to modify what str("class instance calling returns"),
#as well as what the class str is represented as in the debugging 


    
    #equivalant class instance

        
rectangular1 = Rectangle(1000,2000)

print(rectangular1.area())

print(rectangular1.surface())

print(str(rectangular1))

print(rectangular1)
