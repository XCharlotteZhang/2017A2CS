import random
import time

class ply:
    def __init__(self):
        self.name=''
        self.race=''
        self.job=''
        self.weapon=''
        self.exp=0
        self.lv=1
        self.hp=90+self.lv*10
        self.gil=50
        self.potion=1
        self.kill=0
        self.bosskill=1

def new(p):
    p.name=input("What is your name?")
    p.race=input("What is your race? ")
    p.job=input("What is your class? ")
    p.weapon=input("What is your weapon?")
    p.lv=int(input("What is your starting level?"))
    return p

def explore(p):
    p.hp=90+int(p.lv)
    player_dmg_min=0+int(p.lv)
    player_dmg_max=7+int(p.lv)
    
    lvl=input("Choose desired monster level(type number between 1-100)")
    if lvl.isdigit():
            print("You explored the country field...")
            maxturns=random.randint(1,5)
            turns=1
            while turns <= maxturns and int(p.hp) > 0:
                monster_lvl= int(lvl)
                monster_dmg= int(lvl)
                monster_exp= int(lvl)/int(p.lv)*2
                monster_loot= int(monster_lvl)
                encounter=random.randint(1,100)
                drop_lvl=int(lvl)
                if int(encounter) >=70:
                    print("You encounterd a Lv. "+str(monster_lvl)+" Monster!")
                    monster_hp=int(monster_lvl)*2
                    while int(monster_hp) > 0 and p.hp > 0:
                        print("Your Health: "+str(p.hp))
                        print("Monsters Health: "+str(monster_hp))
                        attack=input("Command: attack, potion, run? (typr 1 to attack,2 for potion or 3 for run)")
                        if attack == "1":
                              hit=random.randint(1,100)
                              if int(hit)<=75:
                                  dmg=random.randint(int(player_dmg_min),int(player_dmg_max))
                                  monster_hp=int(monster_hp)-int(dmg)
                                  print("You did "+ str(dmg)+" damage")
                              else:
                                    print("You missed!")
                        elif attack=="2":
                            if potions >0:
                                p.hp=90+int(p.lv*10)
                                print("Potions left... "+str(potions))
                            else:
                                print("You have no potions... You just waisted your turn!")
                        else:
                            print("You tried to escape but failed!")
                        monster_hit_chance=random.randint(1,100)
                        if int(monster_hit_chance)<=60:
                            p.hp=int(p.hp)-int(monster_dmg)
                            print("The monster did "+ str(monster_dmg)+" damage")
                        else:
                            print("The monster missed!")

                        if int(monster_hp) <= 0:
                              p.exp= int(p.exp)+int(monster_exp)
                              print("The monster died.")
                              print("Exp gained: "+ str(monster_exp))
                              print("Your exp: "+ str(p.exp))
                              loot_chance=random.randint(1,100)
                              if int(loot_chance) <10:
                                  print("No loot.")
                                  print("Your gil:"+str(p.gil))
                              elif int(loot_chance) <70:
                                  print("Monster:'Your gil sir...'" +str(monster_loot))
                                  p.gil=int(p.gil)+int(monster_loot)
                                  print("Your gil:"+str(p.gil))
                              elif int(loot_chance) <90:
                                  print("Rare loot! 1 potoin!")
                                  potions+=1
                                  print("Your total potions "+str(potions))
                              p.kill+=1
                        elif int(p.hp) <= 0:
                              print("You died")

                else:
                    loot=random.randint(1,100)
                    trap=random.randint(1,100)
                    if int(loot)>=60:
                        p.gil=int(p.gil)+int(lvl)
                        print("You found "+str(lvl)+" gil")
                        print("You now have a total of "+str(p.gil)+" gil")
                    elif int(loot)<=10:
                        if int(trap)>=50:
                            p.hp=int(p.hp)-10
                            print("You step on a trap")
                            print("You lost ten hp")
                            print("Your total hp is "+str(p.hp))
                turns+=1
                



def town(p):
    c=input("Type 'shop' or 'tarven' to visit.")
    if c=="shop":
        print("Your p.gil "+str(p.gil))
        print("The shopkeep says 'We only have potions of health! They are 20 gil each!'")
        shop=int(input("How many potion would you like to buy?"))
        cost=shop*20
        if p.gil>=cost:
            potions=int(potions)+int(shop)
            p.gil=int(p.gil)-int(cost)
            print("Gold left "+str(p.gil))
            print("Total potoins "+str(potions))
        else:
            print("You do not have enough money to buy the potions")
            print("The shopkeeper kicks you out.")
    elif c=="tarven":
        print("Hello traveler, what can I do for you? Some drink?")
        cb=input("Whats your choice? (drink, or leave)")
        if cb=="drink":
            print("Drinks cost one gil.")
            drink=input("Do you want a drink? (Type 'yes' to drink.)")
            if drink=="yes" and p.gil > 0:
                p.gil=int(p.gil)-1
                print("Your gil: "+str(p.gil))
                print("You get drunk out of your mind.")
            elif p.gil<0:
                print("You do not have enough money to buy the drink.")
                print("The shopkeeper kicks you out.")
            else:
                print("Goodbye.")
        else:
            print("Goodbye.")

p=ply()
p=new(p)
print("The ",str(p.weapon)," weilding ",str(p.job)," from the ",str(p.race)," clan, went out on an adventure. The name was ",str(p.name))

command=input("type: 'explore' to explore field, 'town' to visit town, or 'exit' to leave.")
while command!='exit':
    if command=='explore':
        explore(p)
    elif command=='town':
        town(p)
    command=input("type: 'explore' to explore field, 'town' to visit town, 'info' to check your status, or 'exit' to leave.")
