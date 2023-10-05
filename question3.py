#1st one:
t=0
n=int(input("Enter value of n: "))
e=float(input("Enter error: "))
for i in range(n):
    j=(1/2)**i
    if j-(j+1)<e:
        t+=j
