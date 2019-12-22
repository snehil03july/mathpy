class Mathematics():
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1;
        self.y1=y1;
        self.x2=x2;
        self.y2=y2;
    def slopep(self):
        if (self.x2-self.x1)==0:
            return "Infinite";
        return abs((self.y2-self.y1)/(self.x2-self.x1));
