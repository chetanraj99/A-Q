#Print shortest common Supersequence

def Print_Scs(x,y,m,n):
    t=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                t[i][j]= 1+t[i-1][j-1]
            else:
                t[i][j]= max(t[i][j-1],t[i-1][j])
    s=''
    i=m
    j=n
    while i!=0 and j!=0:
        if x[i-1]==y[j-1]:
            s+=x[i-1]
            i-=1
            j-=1
        else:
            if t[i][j-1]>t[i-1][j]:
                s+=y[j-1]
                j-=1
            else:
                s+=x[i-1]
                i-=1
    return s[::-1]
x='abcdgh'
y='abedfh'
print(Print_Scs(x,y,len(x),len(y)))
