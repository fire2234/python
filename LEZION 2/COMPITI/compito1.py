
list1=[]
list2=[]
for i in range (5):
    list1.append(int(input("inserectr the " + str(i+1) + " number in the first list: ")))
for i in range (5):
    list2.append(int(input("inserectr the " + str(i+1) + " number in the second list: ")))



list3=list1

for x in list2:
    list3.append(x)
print(list3)
