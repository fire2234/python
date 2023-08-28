Comma = ","
Marks = {"!", "?", "."}
phrase = []
phrase2 = []
lettere = {}
Word = input("Inserect thw words, if you wana stop write stop: ")
while Word.lower() != "stop":
    phrase.append(Word)
    Word = input("Inserect thw words, if you wana stop write stop: ")
j = 0  # numero parole senza interpunzione
f = 0  # numero segni di interpunzione
i = 0
l = False
k = False
bool = False
for Word in phrase:
    aim = ""
    bool = False
    if Word in Marks or Word in Comma:
        f = f + 1
        if Word in Marks:
            aim += Word
            phrase2.append(aim)
            k = True
            continue
        else:
            aim += Word
            phrase2.append(aim)
            continue
    else:
        j += 1

    if k:
        Word = Word.capitalize()
        k = False

    if i == 0:
        Word = Word.capitalize()
        aim += Word
    else:
        aim += " " + Word
    i += 1
    phrase2.append(aim)
print(phrase2)
phrase3 = []

aim = ""
i = 0
g = 0
s = False
k = False
n = 0  # numero Frasi
for frase in phrase2:
    g += 1
    if frase in Marks:
        k = True

    else:
        i += 1
    if s:
        frase = frase.strip()
        s = False
    aim += frase
    if g == len(phrase2):
        phrase3.append(aim)
        continue
    if k:
        s = True
        n += 1
        phrase3.append(aim)
        aim = ""
        k = False
for Frasi in phrase3:
    for lettera in Frasi:
        if lettera.lower() in lettere and lettera != " " and not(lettera in Marks):
            lettere[lettera.lower()] += 1
        else:
            lettere[lettera.lower()] = 1
# qui eliminiamo il fatto che conti come carattere anmche /n e lo spazio
if " " in lettere:
     del lettere[" "]
if "\n" in lettere:
    del lettere["\n"]
max_value = max(lettere.values())
min_value = min(lettere.values())
print("le lettere piu usate sono")
for key, value in lettere.items():
    if value == max_value:
        print("Lettera", key, "Utilizzi:", value)

print("\nle lettere meno usate sono")
for key, value in lettere.items():
    if value == min_value:
        print("Lettera", key, "Utilizzi:", value)
print("\n")
print("il numero di parole inscerite e {} invece il numero di caratteri interpunzione e {}, invece il numero di frasi e {} ".format(j, f, n))

print("\n")
for frasi in phrase3:
    print(frasi)
