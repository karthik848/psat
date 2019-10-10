def rotate(a,n) :
    x=int(input("enter yhe no. of times"))
    while x!=0 :
        for i in range(n):
            s = a[i]
            a[i] = a[n-1]
            a[n-1] = s
        x=x-1
    print(a)
    return
n=int(input())
a=list(map(int,input().split()))
rotate(a,n)
