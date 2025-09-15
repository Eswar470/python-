from abc import ABC,abstractmethod
import math
class Polygon:
    def area(self):
        pass
    def perimeter(self):
        pass
class Triangle(Polygon):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        s=self.perimeter()/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
class pentagon(Polygon):
    def __init__(self,side):
        self.side=side
    def area(self):
        return (1/4)*math.sqrt(5*(5+2*math.sqrt(5)))*self.side**2
    def perimeter(self):
        return 5*self.side
def main():
    while True:
        print("T-1,P-2")
        choice=int(input("Enter :"))
        if choice==1:
            a=1
            b=2
            c=3
            triangle=Triangle(a,b,c)
            print(f"area={triangle.area()} and perimeter={triangle.perimeter()}")
if __name__=="__main__":
    main()
        
