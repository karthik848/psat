def dup(a,n) :
    c=[]
    for i in range(n) :
        s=a[i]
        for j in range(i+1,n) :
            if s==a[i] :
                if s not in c :
                    c.append(s)
    print(c)
    return
n=int(input())
a=list(map(int,input().split()))
dup(a,n)


