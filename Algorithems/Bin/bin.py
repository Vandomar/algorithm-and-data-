a=int(input())
result=False
if a%4==0:
    i=0
    while a >= pow(4,i):
        if pow(4,i)==a:
            result=True
            break
        i=i+1
elif a==1:
    result=True
print (result)