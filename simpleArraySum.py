def simpleArraySum(ar,n):
    sum=0
    for i in range(n):
        sum=sum+ar[i]

    return sum


n=int(input("Enter the limit of array "))
sum=0
ar=[]
for i in range(n):
    
    x=int(input())
    ar.append(x)

print("Sum of elements : ",simpleArraySum(ar,n))
