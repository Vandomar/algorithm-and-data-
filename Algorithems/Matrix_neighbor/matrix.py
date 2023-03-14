n = int(input())
m = int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
n=n-1
m=m-1
line = int(input())
column = int(input())
neignbor=[]
if n>0 and m>0:
    if line == 0 and column == 0 :
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line][column+1])
    elif line == 0 and column == m:
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line][column-1])
    elif line == n and column == 0:
        neignbor.append(matrix[line-1][column])
        neignbor.append(matrix[line][column+1])   
    elif line == n and column == m:
        neignbor.append(matrix[line-1][column])
        neignbor.append(matrix[line][column-1])
    elif line == 0 and 0<column<m:
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line][column+1])
        neignbor.append(matrix[line][column-1])
    elif 0<line<n and column == 0:
        neignbor.append(matrix[line-1][column])
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line][column+1])
    elif line == n and 0<column<m:
        neignbor.append(matrix[line-1][column])
        neignbor.append(matrix[line][column+1])
        neignbor.append(matrix[line][column-1])
    elif column == m and 0<line<n:
        neignbor.append(matrix[line-1][column])
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line][column-1])
    elif 0<line<n and 0<column<m:
        neignbor.append(matrix[line-1][column])
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line][column+1])
        neignbor.append(matrix[line][column-1])

elif n==0 and m!=0:
    if column == 0:
        neignbor.append(matrix[line][column+1])
    elif 0<column<m:
        neignbor.append(matrix[line][column+1])
        neignbor.append(matrix[line][column-1])
    elif column == m:
        neignbor.append(matrix[line][column-1])

elif n!=0 and m==0:
    if line == 0:
        neignbor.append(matrix[line+1][column])
    elif 0<line<n:
        neignbor.append(matrix[line+1][column])
        neignbor.append(matrix[line-1][column-1])
    elif line == n:
        neignbor.append(matrix[line-1][column])                
print(*sorted(neignbor))