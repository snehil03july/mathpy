class Mathematics :
    def __init__(self,n):
        self.n=int(n);
    def fibonacci(self):
        i=1;
        x=0;
        y=1;
        print(end="0, ");
        while i<(self.n+1.0):
            t=x+y;
            x=y;
            y=t;
            if i!=self.n:
                print(t,end=", ");
                i=i+1;
            else:
                print(t);
                return;
