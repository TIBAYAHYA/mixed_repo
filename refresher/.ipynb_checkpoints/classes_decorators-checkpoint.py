class Rectangle:



    def __init__(self,width,height):
        self.width = width
        self.height = height 

        


    @property #getter method
              #decorator does some fucking stuff
              # fuck you
    def width(self):
        return self._width #  what this does is     self._width = self.width
                          
    
    @property  #getter method
    def height(self):
        return self._height #what this does is      self._height = self.height
    

    #specifying what happens when we try to assign the value width outside or inside the class
    @width.setter   #settter method
    def width(self,width):
        if width <= 0:
            raise ValueError("Width cannot be less than 1")  
        else : self._width = width      



    #specifying what happens when we try to assign the value width outside or inside the class
    @height.setter   #setter method
    def height(self,height):
        if height <= 0:
            raise ValueError("Height cannot be less than 1")  
        else : self._height = height          



    #special methods
    def __str__(self):
        return f"Rectangle: Width: {self.width} - Height: {self.height}"
         #str(rectangular)




    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
        #repr(rectangular)


    def __eq__(self,other):
        if isinstance(other,Rectangle):
            return self.width == other.width and self.height == other.height\
            or self.width == other.height and self.height == other.width
        else:
            return False
        #basiclly a rotated rectangular is equal to the original rectangular



r1  = Rectangle(1000,2000)

r1._width = -100

