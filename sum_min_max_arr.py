a=list(map(int,input().split()))
maxi=a[0]
mini=a[0]
for i in a:
    if maxi<i:
        maxi=i
    elif mini>i:
        mini=i
    
print(maxi+mini)