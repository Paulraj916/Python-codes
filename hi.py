T = int(input())
N = int(input())
k = int(input())
n=N
i=0
l=k+1
f=l
j = []
while True:
    h = int(input())
    j.append(h)
    
    N-=1
    if N == 0:
        break
B=[]
while True:
    if f<n:
        #print (j[f])
        B.append(j[f])
        f+=1
    
    if f==n:
        while True :
            #print(j[i])
            i+=1
            B.append(i)
            if (n-k)==i:
                break     
    if f==n:
        break
print (B[0],B[1],B[2],B[3],B[4])

