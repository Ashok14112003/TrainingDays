#GCD and LCM

def gcd(x,y):
    while(y>0):
        x,y=y,x%y
    return x
x=int(input())
y=int(input())
print(gcd(x,y))
def lcm(x,y):
    return x*y//gcd(x,y)
print(lcm(x,y))