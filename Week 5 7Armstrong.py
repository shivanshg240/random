for i in range(1000):
    m=i%10
    n=int(i/10)%10
    p=int(i/100)
    ams=(m**3)+(n**3)+(p**3)
    if ams==i:
        print(i)
