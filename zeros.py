ele=input("enter elements: ")

list=ele.split(" ")
n=len(list)
while(n>0):
  for i in range(0,len(list)-1):
      if(int(list[i])==0):
        temp=list[i+1]
        list[i+1]=list[i]
        list[i]=temp
  n=n-1

for i in range(len(list)):
    print(list[i])