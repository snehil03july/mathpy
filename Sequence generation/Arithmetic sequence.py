class Mathematics :
    def __init__(self,a,n,d):
        self.a=a;
        self.n=int(n);
        self.d=d;
    def arith(self):
        i=1;
        while i<(self.n+1.0):
            t=self.a+((i-1)*self.d);
            if i!=self.n:
                print(t,end=", ");
                i=i+1;
            else:
                print(t);
                return;
