import random
import time

class ply:
    __init__(self):
        self.name=''
        self.race=''
        self.job=''
        self.weapon=''
        self.exp=0
        self.lv=1
        self.hp=90+self.self.lv*10
        self.gil=10
        self.potion=1
        self.kill=0
        self.bosskill=1

def new(p):
    p.name=input("What is your name?")
    p.race=input("What is your race? (Your choices are Human, Elf, and Dwarf.)")
    p.job=input("What is your class? (Your choices are Warrior, Archer, and Mage.")
    if p.job=="Warrior":
        p.weapon="Sword"
        print("A "+p.weapon+" is your weapon")
    elif p.job=="Archer":
        p.weapon="Bow"
        print("A "+p.weapon+" is your weapon")
    else:
        p.weapon="Staff"
        print("A "+p.weapon+" is your weapon")
    print("The "+str(p.weapon)+" weilding "+ str(p.job)+" of the "+ str(p.race)+" clan, whent out on an adventure. There name was "+str(p.name))

def explore():
    while p.hp > 0:
        extra_p.hp=int(player_lvl)*10
        p.hp=90+int(extra_p.hp)
        lv_exp=90+int(extra_p.hp)
    if int(p.exp) >= int(lv_exp):
        player_lvl+= 1
        print("Level Up! "+str(player_lvl))
    player_dmg_min=0+int(player_lvl)
    player_dmg_max=7+int(player_lvl)
    
    lvl=input("What level monsters?")
        if lvl.isdigit():
            print("You explored the country field...")
            turns=1
            while turns < 100 and int(p.hp) > 0:
                monster_lvl= int(lvl)
                monster_dmg= int(lvl)
                monster_p.exp= int(lvl)/int(player_lvl)*2
                monster_loot= int(monster_lvl)
                encounter=random.randint(1,100)
                drop_lvl=int(lvl)
                if int(encounter) >=70:
                    print("You encounterd a Lv. "+str(monster_lvl)+" Monster!")
                    monster_p.hp=int(monster_lvl)*2
                    while int(monster_p.hp) > 0 and p.hp > 0:
                        print("Your Health: "+str(p.hp))
                        print("Monsters Health: "+str(monster_p.hp))
                        attack=input("Command: attack, potion, run? (attack or potion or run)")
                        if attack == "attack":
                              hit=random.randint(1,100)
                              if int(hit)<=75:
                                  dmg=random.randint(int(player_dmg_min),int(player_dmg_max))
                                  monster_p.hp=int(monster_p.hp)-int(dmg)
                                  print("\nYou did "+ str(dmg)+" damage")
                              else:
                                    print("You missed!")
                        elif attack=="potion":
                            if potions >0:
                                p.hp=90+int(extra_p.hp)
                                print("Potions left... "+str(potions))
                            else:
                                print("You have no potions... You just waisted your turn!")
                        else:
                            print("You sit there and take it")
                        monster_hit_chance=random.randint(1,100)
                        if int(monster_hit_chance)<=60:
                            p.hp=int(p.hp)-int(monster_dmg)
                            print("The monster did "+ str(monster_dmg)+" damage")
                        else:
                            print("The monster missed!")

                        if int(monster_p.hp) <= 0:
                              p.exp= int(p.exp)+int(monster_p.exp)
                              print("\nThe monster died\n")
                              print("XP gained: "+ str(monster_p.exp))
                              print("Your XP: "+ str(p.exp))
                              loot_chance=random.randint(1,100)
                              if int(loot_chance) <10:
                                  print("No loot :(")
                                  print("Your p.gil "+str(p.gil))
                              elif int(loot_chance) <70:
                                  print("Your p.gil sir. It this many..." +str(monster_loot))
                                  p.gil=int(p.gil)+int(monster_loot)
                                  print("Your p.gil "+str(p.gil))
                              elif int(loot_chance) <90:
                                  print("Rare loot! 1 potoin!")
                                  potions+=1
                                  print("\nYour total potions "+str(potions))
                              p.kill+=1
                        elif int(p.hp) <= 0:
                              print("You died")

                elif int(encounter)<70:
                    loot=random.randint(1,100)
                    trap=random.randint(1,100)
                    if int(loot)>=60:
                        p.gil=int(p.gil)+int(lvl)
                        print("You found "+str(lvl)+" p.gil")
                        print("You now have a total of "+str(p.gil)+" p.gil")
                    elif int(loot)<=10:
                        if int(trap)>=50:
                            p.hp=int(p.hp)-10
                            print("You step on a trap")
                            print("You lost ten p.hp")
                            print("Your total p.hp is "+str(p.hp))
                if int(turns)== 100:
                     boss=random.randint(1,10)
                     if int(boss)>5:
                         print("Boss Fight!")
                         boss_p.hp=int(p.hp)
                         boss_p.exp=int(monster_p.exp)*3
                         boss_dmg=int(lvl)*3
                         boss_loot=int(lvl)*100
                         run=input("Do you fight or run?")
                         while int(boss_p.hp)>0 and int(p.hp) > 0 and run=="fight":
                            print("Your Health: "+str(p.hp))
                            print("Boss Health: "+str(boss_p.hp))
                            attack=input("Do you attack or use a potion? (attack or potion)")
                            if attack == "attack":
                                hit=random.randint(1,100)
                                if int(hit)<=75:
                                    dmg=random.randint(int(player_dmg_min),int(player_dmg_max))
                                    boss_p.hp=int(boss_p.hp)-int(dmg)
                                    print("\nYou did "+ str(dmg)+" damage")
                                else:
                                    print("You missed!")
                            elif attack=="potion":
                                if potions >0:
                                    p.hp=90+int(extra_p.hp)
                                    print("Potions left... "+str(potions))
                                else:
                                    print("You have no potions... You just waisted your turn!")
                            else:
                                print("You sit there and take it")
                            boss_hit_chance=random.randint(1,100)
                            if int(boss_hit_chance)<=60:
                                p.hp=int(p.hp)-int(boss_dmg)
                                print("The boss did "+ str(boss_dmg)+" damage")
                            else:
                                print("The boss missed!")
                            if int(boss_p.hp) <= 0:
                                p.exp= int(p.exp)+int(boss_p.exp)
                                print("\nThe boss died\n")
                                print("XP gained: "+ str(boss_p.exp))
                                print("Your XP: "+ str(p.exp))
                                loot_chance=random.randint(1,100)
                                if int(loot_chance) <10:
                                    print("No loot :(")
                                    print("Your p.gil "+str(p.gil))
                            elif int(loot_chance) <90:
                                    print("Your p.gil sir. It this many..." +str(boss_loot))
                                    p.gil=int(p.gil)+int(boss_loot)
                                    print("Your p.gil "+str(p.gil))
                            elif int(p.hp) <= 0:
                                print("You died")
                            else:
                                print("Rare loot! 10 potoin!")
                                potions+=10
                                print("\nYour total potions "+str(potions))
                            boss_p.kill+=1
                print("End of turn "+ str(turns)+"\n")
                turns+=1
                time.sleep(1.0)
        else:
            print("That isnt a lvl... your just not going to ep.explore...")

def info():
    print("Total kills",str(p.kill))
    print("Total boss kills",str(boss_p.kill))


def town():
    c=input("Tyoe 'shop' or 'tarven' to visit.")
    if c=="shop":
        print("Your p.gil "+str(p.gil))
        print("The shopkeep says 'We only have potions of p.hp! They are 20 p.gil each!'")
        shop=input("How many do you want?")
        cost=int(shop)*20
        if int(p.gil)>=int(cost):
            potions=int(potions)+int(shop)
            p.gil=int(p.gil)-int(cost)
            print("Gold left "+str(p.gil))
            print("Total potoins "+str(potions))
        else:
            print("'Your too poor! Come back with some more money fool!")
            print("The shopkeeper kicks you out.")
    elif c=="tavern":
        print("Hello traveler, what can I do for you? A drink? Or the lates rumore?")
        cb=input("Whats your choice? (drink, rumore, or leave)")
        if cb=="drink":
            print("Drinks cost one p.gil.")
            drink=input("Do you want a drink?")
            if drink=="yes" and p.gil > 0:
                p.gil=int(p.gil)-1
                print("Your gil: "+str(p.gil))
                print("You get drunk out of your mind.")
            else:
                print("...Goodbye")

p=ply()
p=new(p)

command=input("type: 'explore' to explore field, 'town' to visit town, 'info' to check your status, or 'exit' to leave.")
while command!='exit':
    if command='explore':
        explore()
    elif command='town':
        town()
    elif command='info':
        info()
    command=input("type: 'explore' to explore field, 'town' to visit town, 'info' to check your status, or 'exit' to leave.")
