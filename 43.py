def d(a,n) :
    b=int(input("enter the no to be deleted"))
    for i in range(n) :
        if a[i]==b :
            ind=i
            break
    for i in range(ind,n-1) :
        a[i]=a[i+1]
    a[n-1]=0
    for i in range(n-1) :
        print(a)
    return
n=int(input())
a=list(map(int,input().split()))
d(a,n)