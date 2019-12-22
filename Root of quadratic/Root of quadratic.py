class mathematics():
    def __init__(self,a,b,c):
        self.a=a;
        self.b=b;
        self.c=c;
    def root(self):
        d=(self.b**2)-(4*self.a*self.c);
        if d==0:
            d=-(self.b/(2*self.a));
            print("The eqaution has equal roots = ",d);
        elif d>0:
            root1=(-self.b+(d**0.5))/(2*self.a);
            root2=(-self.b-(d**0.5))/(2*self.a);
            print("The equation has real and distinct roots :");
            print(root1);
            print(root2);
        else:
            d=(-d)**0.5
            print("The equation has imaginary roots :")
            print("(-",self.b," + ",d,"i)/",(2*self.a));
            print("(-",self.b," - ",d,"i)/",(2*self.a));
            return
