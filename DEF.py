class circle():
    def area(self,r):
        self.r=r
        return(3.14*self.r*self.r)



    def perimeter(self,r):
        self.r=r
        return(2*3.14*self.r)


r=int(input("enter the radius: "))
b=circle()
print(b.area(r))
print(b.perimeter(r))
