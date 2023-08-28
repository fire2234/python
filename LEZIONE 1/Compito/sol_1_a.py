print("__________________________________\n\n")
print("benvenuto nell casino dell gabbrone")
nome=input("inscerisca il nome: ")
cognome=input("inscerisca il cognome: ")
eta=int(input("inscerisca L'eta: "))

if not(len(nome) > 1 and len(cognome) > 1 and eta >= 18):
    print("\n\n ce un errore nei suoi dati insceriti, oppure e minorenne")
else:
    print("\n\n i dati da lei inscerito sono tutti correti qui di seguito la serie dei dati inscerita\n Nome: " + nome.capitalize() + "\n Cognome: " + cognome.capitalize() + "\n Eta: " +str(eta) +"\n la ringrazziamo di essersi abbonato all nostro casino")