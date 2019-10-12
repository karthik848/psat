b=0
n=int(input())
while n!=0 :
    d=n%10
    if d%4==0 or d%7==0 :
        b=b+1
    n=n//10
if b%4==0 or b%7==0 :
    print("YES")
else :
    print("NO")
 
