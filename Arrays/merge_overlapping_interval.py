arr=[[1,3],[2,6],[8,10],[15,18]]
merged=[]
for interval in arr:
    if not merged:
        merged.append(interval) 
    elif interval[0]<=merged[-1][1]:
        merged[-1][1]=max(merged[-1][1],interval[1]) 
    else:
        merged.append(interval)
print(merged)
