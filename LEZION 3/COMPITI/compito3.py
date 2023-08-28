"""testo=input("Inscerire le parole che si vuole, quando si preme stop si deve chudere: \n\t")
frase=[]
caratterifrase={}
parole2=""
contafini=0
bool=True
contasenzacaratspec=0
while testo != "stop":
    frase.append(testo)
    testo = input("Inscerire le parole che si vuole, quando si preme stop si deve chudere: \n\t")
i=0
for parole in frase:
    for lettere in parole:
        if lettere in caratterifrase.keys():
            caratterifrase[lettere]+=1
        else:
            caratterifrase[lettere]=1
    if parole != "," and not(parole == "!" or parole == "?" or parole== "." ):
        parole=" "+parole
    elif parole==",":
        bool = False
    if parole == "!" or parole == "?" or parole== ".":
        parole2+="\n"
        i += 1
        contafini+=1
        continue
    parole2+=parole
    i+=1
    if bool:
        contasenzacaratspec+=1
    bool=True
letteramax=""
letteramin=""
i=True
for keys,value in caratterifrase.items():
    if i:
        max = value
        letteramax=keys
        min = value
        letteramin=keys
    if value>max:
        max=value
        letteramax = keys
    elif value<min:
        min=value
        letteramin=keys
    i = False
print("il numero di parole inscerite e {} invece il numero di caratteri interpunzione e {}, invece il numero di frasi e {} il carattere meno usato e {} usato solamente {} volte invece quello piu usato e {} usato {} volte ".format(contasenzacaratspec,contafini,contafini+1,letteramin,min,letteramax,max))"""
