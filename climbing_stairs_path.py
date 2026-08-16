# climbing stairs path

def climbing_stairs_path(n,memo={}):
    if n in memo:
        return memo[n]
        
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        n1=climbing_stairs_path(n-1)
        n2=climbing_stairs_path(n-2)
        n3=climbing_stairs_path(n-3)
        memo[n]= n1+n2+n3
        return memo[n]
print(climbing_stairs_path(10))
