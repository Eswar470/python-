def calculator(a,b,sign):
   operator={
        '+':a+b,
        '-':a-b,
        '*':a*b,
        '/':a/b
    }
   return operator[sign]
n=False

while not n :
    a=int(input("Enter first number:"))
    sign=input("Enter operator(+,-,/,*):")
    b=int(input("Enter 2nd number:"))
    ans=calculator(a,b,sign)
    print(f"{a}{sign}{b}={ans}")
    m=False
    while not m:
        next_step=input(f"Enter 'y' to continue with {ans} or 'n' to start new claculation or 'x' to exit.")
        if next_step=='y':
            sign2=input('pick up operation:')
            c=int(input("enter next number:"))
            ans2=calculator(ans,c,sign2)
            print(f"{ans}{sign2}{c}={ans2}")
        elif next_step=='n':
            m=True
        elif next_step=='x':
            m=True
            n=True
print('Thank you')

