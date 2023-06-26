string=input("enter elements: ")
n=len(string)
flag=0
for i in range(0,n):
  if string.count(string[i])==1:
    print(i)
    flag=0
    break
  else:
    flag=1
if(flag==1):
  print("-1")
