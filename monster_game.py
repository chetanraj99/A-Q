def Monster_fight_Game(W, wt, val, n,l):
    global w
    w=max(w,W)
    
    if n<0:
        return 0
    if (wt[n-1] <= W and l[n-1]==1):
        l[n-1]=0 
        return max(1+ Monster_fight_Game(W+val[n-1], wt, val, n-1,l),
			                    Monster_fight_Game(W, wt, val, n-1,l))
        
    else:
        return Monster_fight_Game(W, wt, val, n-1,l)
        
w=0
val = [25,50,8,500,199,5,5]
wt = [ 25,50,12,200,100,20,7]
W = 7
n = len(val)
l=[1]*n
max_defeat_monster=0
for _ in range(n):
    max_defeat_monster=Monster_fight_Game(W, wt, val, n,l)+max_defeat_monster
    W=w
    
print(max_defeat_monster)

