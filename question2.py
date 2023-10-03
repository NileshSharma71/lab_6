#1st one:
N=int(input("Enter: "))
t=0
for i in range(N):
    k=1/(i+1)
    t=k+t
print(f"The sum of the series1: {t:.9f}")
#2nd one:
import math
kk=0
for i in range(N):
    j=1/(math.factorial(i))
    kk+=j
print(f"The sum of the series2: {kk:.9f}")
#3rd one: 
kkk=1
x=float(input("Enter value of x: "))
for i in range(N):
    jj=(x**(i+1))/(i+1)
    kkk+=jj
print(f"The sum of the series3: {kkk:.9f}")