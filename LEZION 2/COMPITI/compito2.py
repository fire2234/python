
User_Number=int(input("inscerect the number of user you wan register "))
gameswithvote={}
while User_Number<=0:
    print("Please select a valid number of people")
    User_Number = int(input("inscerect the number of user you wan register "))

User={}


for i in range(User_Number):
    nickname=input(f"Inserect nickname of people number {i+1} of {User_Number}: ")
    if nickname in User:
        print("Nickname already taken")
    else:
        age=int(input("inserect our age: "))

        while age<18:
            print("you are not adult, please reinserect the number ")
            age = int(input("inserect  age of user: "))

        else:
            Gender = input("Inserect the gender F for girls M for boys ")
            while Gender != "M" and Gender != "F":
                print("Please select a valid Gender")
                Gender = input("Inserect the gender F for girls M for boys ")

            Favoritegame=input("Inserect your favorite game divese by \",\" ")
            Favoritegame=Favoritegame.replace(" ", "")
            Favoritegame=Favoritegame.split(",")
            print(Favoritegame)





            User[nickname]={}
            User[nickname]["Age"]=age
            User[nickname]["Gender"] = Gender
            User[nickname]["Game"]=Favoritegame
            i=i+1


print("Perfect , now see a resum of all ")

Girlcounter=0
Boyscounter=0
lenscounter=0
Maxage=User[nickname]["Age"]
Minage=User[nickname]["Age"]
Yearcounter=0
i=0
for nickname in User:
    lenscounter+=len(nickname)
    if User[nickname]["Gender"]=="M":
        Boyscounter+=1
    else:
        Girlcounter+=1
    Yearcounter+=User[nickname]["Age"]
    i+=1
    if User[nickname]["Age"]>Maxage:
        Maxage=User[nickname]["Age"]
    elif User[nickname]["Age"]<=Minage:
        Minage=User[nickname]["Age"]

if User_Number == 1:
    Minage=Maxage

for nickname in User:
    for game in User[nickname]["Game"]:
        if game in gameswithvote:
            gameswithvote[game] = gameswithvote[game]+1
        else:
            gameswithvote[game]=1
max=0
for game in gameswithvote:
    if max<gameswithvote[game]:
        max=gameswithvote[game]
        bestgame=game


print("the game with max point is {} whith {}".format(bestgame,gameswithvote[bestgame]))



print(gameswithvote)

print(f"Average age: {Yearcounter / i}\nMax age: {Maxage}\nMin age: {Minage}\nNumber of girls: {Girlcounter}\nNumber of boys: {Boyscounter}\nAverage nickname length: {lenscounter / i}")







