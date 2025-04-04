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
    


#special methods

    def __str__(self):
        return f"Rectangle: Width: {self.width} - Height: {self.height}"
         #str(rectangular)




    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
        #repr(rectangular)



       #we define what two class instances being equal means
    def __eq__(self,other):
        if isinstance(other,Rectangle):
            return self.width == other.width and self.height == other.height\
            or self.width == other.height and self.height == other.width
        else:
            return False
        #basiclly a rotated rectangular is equal to the original rectangular


    def __lt__(self,other):
        if isinstance(other,Rectangle):
            return self.area() < other.area()  #comparing area function of both rectangulars
        else:
            return NotImplemented  # this reverses the comparison indicator? less then becomes more than?
                                   #enables us to have gt aka greater than without setting It up, in terms of signs at least






        
r1 = Rectangle(1000,2000)

print(r1.area())

print(r1.surface())

print(str(r1))

print(repr(r1))


r2 = Rectangle(1000,2000)
print(r1==r2)


r3 = Rectangle(100,300)
print(r1>r3)