n=int(input())
X=list(map(int, input().split()))
k=int(input())
sum=int(''.join(map(str, X))) + k
sum=str(sum)
print (" ".join(sum))