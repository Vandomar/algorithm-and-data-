def data_input():
    n=int(input())
    m=int(input())
    if n==m==0:
        return None,None,None
    A=[list(map(int, input().split())) for i in range(n)]
    return n, m, A

if __name__ == '__main__':
    n, m, A = data_input()
    if n==None:
        print ()
    else:
        for i in range(m):
            print(*(A[j][i] for j in range(n)), sep=' ')