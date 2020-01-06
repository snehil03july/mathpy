# Python program to implement 3-D Vectors. 
from math import sqrt 
  
class Vector: 
  
    def __init__(self, x, y, z): 
        self.x = x 
        self.y = y 
        self.z = z 
  
    
    def magnitude(self): 
  
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2) 
  
     
    def __add__(self, V): 
  
        return Vector(self.x + V.x, self.y + V.y, self.z + V.z) 
  
    
    def __sub__(self, V): 
  
        return Vector(self.x - V.x, self.y - V.y, self.z - V.z) 
  
    
    def __xor__(self, V): 
  
        return self.x * V.x + self.y * V.y + self.z * V.z 
  
    
    def __mul__(self, V): 
  
        return Vector(self.y * V.z - self.z * V.y, 
                      self.z * V.x - self.x * V.z, 
                      self.x * V.y - self.y * V.x) 
  

    def __repr__(self): 
  
        out = str(self.x) + "i "
  
        if self.y >= 0: 
            out += "+ "
        out += str(self.y) + "j "
        if self.z >= 0: 
            out += "+ "
        out += str(self.z) + "k"
  
        return out 