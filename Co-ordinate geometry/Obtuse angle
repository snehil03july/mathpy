import math
class Mathematics:
    def __init__(self,a1,b1,c1,a2,b2,c2):
        self.a1=a1;
        self.b1=b1;
        self.c1=c1;
        self.a2=a2;
        self.b2=b2;
        self.c2=c2;
    def angleacute(self):
        if self.b1==0:
            if self.b2==0:
                return 0;
            elif self.a2==0:
                return 90;
            else:
                m1=0;
                m2=-(self.a2/self.b2)
                return 180-(math.degrees(math.atan(abs((m2-m1)/(1+(m1*m2))))));
        elif self.b2==0:
            if self.a1==0:
                return 90;
            else:
                m1=-(self.a1/self.b1);
                m2=0;
                return 180-(math.degrees(math.atan(abs((m2-m1)/(1+(m1*m2))))));
        else:
            m1=-(self.a1/self.b1);
            m2=-(self.a2/self.b2);
            return 180-(math.degrees(math.atan(abs((m2-m1)/(1+(m1*m2))))));
