class Mathematics :
    def __init__(self,a,n,r):
        self.a=a;
        self.n=int(n);
        self.r=r;
    def geom(self):
        i=1;
        while i<(self.n+1.0):
            t=self.a*(self.r**(i-1));
            if i!=self.n:
                print(t,end=", ");
                i=i+1;
            else:
                print(t);
                return;
