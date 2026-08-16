#Matrix chain multiplication memoization
def MCM(arr,i,j):
    if t[i][j]!=-1:
        return t[i][j]
    if i>=j:
        return 0
    mn=float('inf')
    for k in range(i,j):
        temp=MCM(arr,i,k)+MCM(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if temp<mn:
            mn=temp
    t[i][j]=mn
    return t[i][j]
t=[[-1 for i1 in range(4+2)] for j1 in range(4+2)]
print(MCM([40,20,30,10,30],1,4))
