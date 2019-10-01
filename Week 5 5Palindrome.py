st=str(input("Enter the String"))
ust=str.upper(st)
l=len(ust)
n=int(l/2)
c=0
for i in range(0,n+1):
    if ust[i]!=ust[l-1-i]:
        c=1
        break
if c==1:
   print("The given String is not a Palindrome")
else:
   print("The given String is a Palindrome")
