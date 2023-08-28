l1=[]
l2=[]
list1=[]
list2=[]
with open("data/file.txt") as f:
    righe=f.readlines()
    l1=([x.strip("\n") for x in righe])

l2.append(l1[1])
del l1[1]
l=[l1,l2]

l1=l1[0].split(",")
l2=l2[0].split(",")
list1=[int(n) for n in l1]
list2=[int(n) for n in l2]
print(l2)
i=0
j=0
bool=True
with open("data/risultato.txt",'w') as f:
    for x in list1:
        for z in list2:
            if i==j and bool:
                f.writelines(str(int(x+z)))
                f.writelines(" ")
                j+=1
                bool=False
                continue
            else:
                f.writelines("0")
                f.writelines(" ")
            i += 1
        bool=True
        i = 0
        f.writelines("\n")





