class Mathematics:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1;
        self.y1=y1;
        self.x2=x2;
        self.y2=y2;
    def midpoint(self):
        print("Mid point : (x,y) : (",((self.x1+self.x2)/2),",",((self.y1+self.y2)/2),")");
        return;
