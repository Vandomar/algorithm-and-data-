n=int(input())
temperature=list(map(int, input().split()))
chaos=0
for i in range (1,n-1):
    if temperature[i-1]<temperature[i] and temperature[i]>temperature[i+1]:
        chaos=chaos+1
if temperature[n-2] < temperature[n-1]:
    chaos=chaos+1
if n>1:
    if temperature[0] > temperature[1]:
        chaos=chaos+1
if n==1: chaos=1
print (chaos)