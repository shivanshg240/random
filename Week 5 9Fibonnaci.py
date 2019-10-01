n=int(input("Enter the no. of terms to be printed in the sequence "))
a=0
b=1
print(b, end=",")
for i in range(1,n):
    nxt=a+b
    print(nxt, end=",")
    a,b=b,nxt
