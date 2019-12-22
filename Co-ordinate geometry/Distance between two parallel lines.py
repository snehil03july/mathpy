class Mathematics:
    def __init__(self,a1,b1,c1,a2,b2,c2):
        self.a1=a1;
        self.b1=c1;
        self.c1=c1;
        self.a2=a2;
        self.b2=b2;
        self.c2=c2;
    def distl(self):
        if self.a1==0:
            return abs(self.c1-self.c2);
        m=-self.b1/self.a1;
        d=abs(self.c1-self.c2);
        return d/(((m**2)+1)**0.5);
