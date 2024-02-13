list=[]

item=int(input("Enter the no. of item sold\t"))
for x in range(0, item):
	temp=int(input("Enter the price\t:"))
	list.append(temp)
	
print("list element:\n")
print(list)

total=0
for x in range(0, item):
 	total= total+list[x]
 	
print("total selling\t:", total)

temp= list[0]
for x in range(0, item-1):
    if(list[x]>list[x+1]):
      	temp= list[x+1]
      	
print("Price of lowest item sold\t", temp)

temp=list[0] 
for x in range(0, items-1):
	if(list[x]<list[x+1]):
		temp =list[x+1]
	
print("Price of costiest item sold\t", temp)		
