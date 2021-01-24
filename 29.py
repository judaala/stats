list1=list(map(int,input("enter your data").split()))
len=len(list1)
list1.sort()
print(list1)
if len%2==0:
    median=(list1[len//2]+list1[len//2-1])/2
    print(f"median ={median}")
else:
    median=list1[len//2]
    print(f"median ={median}")
print(f"mean ={sum(list1)/(len+1)}")
dic=dict()
dic1=dict()
for name in list1:
   if name not in dic:
      dic[name]=1
   else:
      dic[name] = dic[name] + 1
maxval=max(dic.values())
if maxval==1:
    print("no mode")
else:
    for i,j in dic.items():
        if(int(j)==maxval):
            print(f"mode = {i}")
