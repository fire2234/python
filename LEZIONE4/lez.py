def myfunction(path1,path2):
    dizionario={}
    lista=[]
    with open(path1) as f:
        file1=f.readlines()
    with open(path2) as f:
        file2=f.readlines()
    for x in file1:
        x=x.strip("\n")
        dizionario[x]=""
    for x in file2:
        x = x.strip("\n")
        if x in dizionario:
            lista.append(x)
    i=len(lista)-1
    with open("data/file_03_3.txt",'w')as f:
        while i != -1 :
            f.writelines(lista[i]+"\n")
            i-=1
path1="data/file_03_1.txt"
path2="data/file_03_2.txt"
print("coap")
myfunction(path1,path2)
