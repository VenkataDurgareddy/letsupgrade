n=(int(input("Enter a number")))
k=0
for i in range(1,n+1):
    if n%i==0:
        k=k+1
if k==2:
    print("prime")
else:
    print("Not prime")