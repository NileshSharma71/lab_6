N=int(input("Enter: "))
t=0
for i in range(N):
    k=1/(i+1)
    t=k+t
print(f"The sum of the series: {t:.9f}")