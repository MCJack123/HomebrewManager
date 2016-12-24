lives=5
gold=10
damagem=1
special=[]
healthm=1
import time
import random
import math
from menu import menu
def rendscreenx(text):
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives) + " XP: "+ str(xp))
    print("Special items: "+str(special))
    print("--------------------------------------------------------------------------------")
    print(text)
def randint(sinput,  einput):
    random.randint(sinput,einput)
def rendscreen(text):
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives))
    print("Special items: "+str(special))
    print("--------------------------------------------------------------------------------")
    print(text)
def rendscreenf():
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives))
    print("Special items: "+str(special))
    print("Health: "+str(health)+" Enemy Health: "+str(enemyh))
    print("--------------------------------------------------------------------------------")
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
cls()
print("Press enter to go to the next screen.")
input()
cls()
print("--------------------------------------------------------------------------------")
print("-----------Welcome to the forest------------------------------------------------")
print("-----------Are you ready?-------------------------------------------------------")
print("--------------------------------------------------------------------------------")
print("Press Enter to Continue...")
input("")
cls()
lives=5
gold=10
move="None"
rdone=0
ldone=0
while move!="L" and move!="l" and move!="R" and move!="R" and move!="s" and move!="S":
    rendscreen("You are walking in a forest.  You come to a part you don't know. You go ahead.")
    move=menu([["Left","L"],["Right","R"],["Straight","S"]],0,"Which way do you go?")
    if move=="L" or move=="l":
        if ldone==1:
            rendscreen("You've already gone here!")
            input()
            move="0"
        else:
            rendscreen("You found a chest! Inside it was 5 bars of gold.(enter to continue)")
            input()
            gold +=5
            rendscreen("It's at a dead end, however. You walk back.")
            input()
            move="0"
            ldone=1
    elif move=="R" or move=="r":
        if rdone==1:
            rendscreen("You've already gone here!")
            input()
            move="0"
        else:
            rendscreen("You walk into a trap and lose a life.(enter to continue)")
            input()
            lives+=-1
            rendscreen("You walk back.")
            input()
            move="0"
            rdone=1
rendscreen("You walk forward for a while.(enter to continue)")
input()
rendscreen("The ground begins to shake...(enter to continue)")
input()
cls()
print("Louder...")
time.sleep(1)
rendscreen("You come up to a monster!")
time.sleep(1)
rendscreen("'I will eat you!'")
time.sleep(1)
rendscreen("How to fight: Press K to kick and P to punch.")
input()
rendscreen("When it's your enemy's turn, hope for the best!")
input()
rendscreen("Press enter to start.")
input()
health=1000
enemyh=200
while enemyh>0:
    rendscreenf()
    fmove="0"
    while fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
    if fmove=="K" or fmove=="k":
        sub=math.floor(random.random()*10)+5
        enemyh=enemyh-sub*10
        print("Damage dealt: "+ str(sub*10))
        input()
    elif fmove=="adminpass":
        enemyh=0
    else:
        sub=math.floor(random.random()*10)
        enemyh+=-sub*18
        print("Damage dealt: "+ str(sub*18))
        input()
    rendscreenf()
    time.sleep(.2)
    if enemyh>0:
        health+=-math.floor(random.random()*100)
        health+=-60
        print("Monster attacks! Damage dealt: "+ str(sub+60))
        input()
rendscreen("You won the battle!")
input()
rendscreen("The monster had 20 gold and you gained two lives from defeating him!")
gold+=20
lives+=2
input()
rendscreen("You continue along the path.")
input()
ebhealth=0
special=[]
berries=0
while berries != "y" and berries != "Y" and berries != "N" and berries != "n":
    rendscreen("You find some berries.  Do you eat them?")
    berries=menu([['Yes','Y'],['No','N']],0,'You find some berries.  Do you eat them?')
if berries=="y" or berries=="Y":
    rendscreen("Under the leaves, you found a glove!  It grants +50 health in all battles!")
    ebhealth+=50
    special.append("Glove")
    input()
    rendscreen("After eating some berries, you continue walking.")
else:
    rendscreen("You continue walking.")
input()
river="0"
while river!="Y" and river!="y" and river!="N" and river!="n":
    rendscreen("After walking for quite some time, you come to a river.  There's a bear right behind you.  Do you try to cross the river?")
    river=menu([['Yes','Y'],['No','N']],0,'Do you try to cross the river?')
if river=="Y" or river=="y":
    rendscreen("You manage to cross the river, but you get sick and lose a life.")
    lives+=-1
else:
    rendscreen("You stay and fight the bear!")
    input()
    health=1000+ebhealth
    enemyh=400
    while enemyh>0:
        rendscreenf()
        fmove="0"
        while fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
        if fmove=="K" or fmove=="k":
            sub=math.floor(random.random()*10)+6
            enemyh=enemyh-sub*10
            print("Damage dealt: "+ str(sub*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.85*10
            print("Damage dealt: "+ str(sub*1.85*10))
            input()
        rendscreenf()
        time.sleep(.2)
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.4*10
            health+=-sub
            health+=-4*10
            print("Bear attacks! Damage dealt: "+ str(sub+4*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
    rendscreen("You won the battle!!!")
    input()
    rendscreen("You keep the fur coat from the bear.  It gives you +200 health in all battles!")
    input()
    ebhealth+=200
    special.append("Fur Coat")
    rendscreen("You decide to put down a log and cross the river.")
input()
rendscreen("Now that you're across the river, you decide to start exploring.")
input()
move="0"
lgone="0"
rgone="0"
while move!="L" and move!="l" and move!="R" and move!="R" and move!="s" and move!="S":
    rendscreen("Do you go left, right, or straight?")
    move=menu([['Left','L'],['Right','R'],['Straight','S']],0,'What direction do you go?')
    if move=="l" or move=="L":
        if lgone=="0":
            lgone="1"
            rendscreen("You go left. You find some food.  Do you eat it?")
            food1=0
            while food1 != "y" and food1 != "Y" and food1 != "N" and food1 != "n":
                food1=menu([['Yes','Y'],['No','N']],0,'Do you eat the food?')
            if food1=="y" or food1=="Y":
                rendscreen("It was poisoned!  Lose a life")
                lives+=-1
                input()
            else:
                rendscreen("You decide not to eat and you go back.")
                input()
        else:
            rendscreen("You've already gone this way!")
            input()
        move="0"
    elif move=="r" or move=="R":
        if rgone=="0":
            rgone="1"
            rendscreen("You found a chest!  Inside it is 25 gold!")
            gold+=25
            input()
        else:
            rendscreen("You've already gone this way!")
            input()
        move="0"
    else:
        rendscreen("There's a giant!")
        input()
        rendscreen("'I demand 40 gold or I will FIGHT YOU!'")
        input()
        fight="0"
        if gold<40:
            rendscreen("You must fight the giant.")
            giantf="1"
            input()
        else:
            watf="?"
            rendscreen("Do you want to fight?")
            while watf!="Y" and watf!="y" and watf!="N" and watf!="n":
                watf=menu([['Yes','Y'],['No','N']],0,'Do you want to fight?')
            if watf=="y" or watf=="Y":
                giantf="1"
            else:
                giantf="0"
if giantf=="1":
    health=1000+ebhealth
    enemyh=1300
    while enemyh>0:
        rendscreenf()
        fmove="0"
        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+6
            enemyh+=-sub*10
            print("Damage dealt: "+ str(sub*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
        elif fmove=="l":
            health=-1
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.9*10
            print("Damage dealt: "+ str(sub*1.9*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.5
            health+=-sub*10
            health+=-6*10
            print("Giant attacks!  Damage dealt: "+ str(sub+6*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You defeated the giant!")
    input()
    rendscreen("The giant was hoarding 200 gold!")
    input()
    gold+=200
    rendscreen("You also gain a life from defeating the giant.")
    input()
    lives+=1
    rendscreen("The giant also had a spear.  It grants double damage in all battles!")
    damagem+=1
    special.append("Spear")
    input()
else:
    rendscreen("You decided not to fight the giant and pay him 40 gold.")
    gold+=-40
    input()
rendscreen("You continue walking, now that you're past the giant.")
input()
rendscreen("On the path, you find a bomb!  Use it once to destroy an enemy.  You can only use it once, however, so use it wisely")
special.append("Bomb")
input()
rendscreen("Now that you have the bomb, you continue walking.")
#special.remove("Bomb")###How to remove bomb!!!
input()
rendscreen("You come up to a dragon!")
print("    \ |  (  \ ( \.(               )")
print("                      _____")
print("  \  \ \  `  `   ) \             (  ___                 / _   \\")
print(" (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_")
print("- .-               \+  ;          (  O                           \____")
print("                          )        \_____________  `              \  /")
print("(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/")
print("  .    /./.+-  . .- /  +--  - .     \______________//_              \_______")
print("(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |")
print("  (__ ' /x  / x _/ (                                  \___'          \     /")
print(" , x / ( '  . / .  /                                      |           \   /")
print("    /  /  _/ /    +                                      /              \/")
print("   '  (__/                                             /                  \\")
input()
if giantf=="1":
    rendscreen("'You killed my good friend the giant!  I will EAT YOU!'")
    input()
    health=1000+ebhealth
    enemyh=1500
    while enemyh>0:
        rendscreenf()
        fmove="0"
        if "Bomb" in special:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb?')
        else:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+6
            enemyh+=-sub*damagem*10
            print("Damage dealt: "+ str(sub*damagem*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
        elif fmove=="l":
            health=-1
        elif fmove=="B" or fmove=="b":
            special.remove("Bomb")
            enemyh=0
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.9*damagem*10
            print("Damage dealt: "+ str(sub*1.9*damagem*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.5
            health+=-sub*10
            health+=-6*10
            print("Dragon attacks!  Damage dealt: "+ str(sub+6*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You beat the dragon!")
    input()
else:
    rendscreen("Thank you for paying the giant.  You may pass.")
    input()
    rendscreen("The dragon lets you pass, and you continue on your way.")
    input()
rendscreen("You found another bomb on the path!")
special.append("Bomb")
input()
path=0
while path != "r" and path != "R" and path != "l" and path != "L":
    rendscreen("The path branches into 2 paths: left or right.  Which one do you take?")
    path=menu([['Left','L'],['Right','R']],0,'Which path do you take?')
if path == "r" or path == "R":
    #Stuff for right path here.
    rendscreen("You go on the right path.")
    input()
    rendscreen("There's a chest!")
    input()
    rendscreen("You open it, and there's 20 gold inside!")
    gold+=20
    input()
    rendscreen("You walk farther.")
    input()
    rendscreen("You come up to... a DRAGON!")
    print("                                        *$$$$$$eeee")
    print("                                          ***$$$$$$$$e")
    print("                                                **$$$$$e")
    print("           e$$$e                                   *$$$$$")
    print("          $$$$                                     e$$$$$")
    print("         $$$$                                  ee$$$$$$$")
    print("         $$$$               ee***ee***eeeee$$$$$$$$$$$*")
    print("         $$$$e        eee$$$     $     $$$$$$$$$$$$$*        ee")
    print("         *$$$$$$$$$$$$$$$$$$ $$$ $ $$$ $$$$$$$$**      ee****WW$")
    print(" eeeeee    *$$$$$$$$$$$$$$$$  $$ $  $$ $*****        e*!!!W**!W*")
    print("$!WWWW!***ee   *************eee$$**eee$             e*!W**!!!!$")
    print(" $!!!!***WW!**eee        e**!!!!!!!!!!!***e      e**!!W*!!!!!!$")
    print(" $!!!!!!!!!*W!!!!$      $!!!!W****WWWW!!!!!$     *W!!!*WW!!!!!$")
    print(" $!!!!!!!!!WW*!!!$      *W!!*W!!!!!!!!*W!!W*     e*!!!!!!*W!!!$")
    print(" $!!!!!W***!!WW!!*e       ******WWWWW*****       $!!!W***W!**W*")
    print(" $!!!W*WW****!!*W!!*eee    ee   $!!$   ee     ee*!!W*!!!!!*W!!$")
    print("  $W*!$!!!!!!!!!!*WW!!!****!W***!!!!***W!*****!!!!$!!!!!!!!*W$")
    print("  $!W*!!!!!!!!!!!W**!WW!!!!W*!!!!!!!!!!*WW*****W!!$!!!!!!!!!W*")
    print("   *WW!!!!!!!!!W*!W**!!***W$!!!!W!!!W!!!$!!!!!!$!W*!!!!!!W**")
    print("      ****WW!W*!W$WWW!!!!!!$!!!!*WWW*!!!$!!!!!!$W$!!!WWWW*")
    print("            *$W*!!!!!*WW!!!$!!!!!!$!!!!W*!!WW**!!!*$*")
    print("              $!!!!!!!!!*W!*W!!!!!$!!!!$!W*!!!!!!!!!$")
    print("              *W!!!!!!!!!!***W!!!!$!!!!$*!!!!!!!!!!!$")
    print("               $!!!!!!!!!!!!!$!!!!$!!!W*!!!!!!!!!!!$")
    print("                $!!!!!*W!!!!!$!!!!$!!!$!!!!!W!!!!!$")
    print("eeeeeeee         $!!!!!!$!!!!$!!!!$!!!$!!!!W*!!!!W*")
    print("$!!!!W*       ee$W$!!!!!!$!!!$!!!!$!!!$!!!W*!!!!W*")
    print("$!!!*ee**e**e*WW*!!$!!!!!!$!!$!!!!$!!!$!!!$!!!WW*")
    print("$!$WW!!*******!!WWW**W*W!!$WW*!!!!$!!!$!W$WW**W!*e")
    print("$*   **WWWWWW***e*!!$!!$**!W*!!!WW*$!!!*W!!*W!!*W!*e")
    print("              e*!!!$!!W*!W*!!!!$    $!!!!$!!!$!!!$!*e")
    print("              *WWW*WW*WWW*WWWW*      *WWW*WWW*WWW*WW*")
    input()
    rendscreen("Dragon: I WILL RIP YOU APART WITH MY CLAWS!")
    input()
    health=1000+ebhealth
    enemyh=2500
    while enemyh>0:
        rendscreenf()
        fmove="0"
        if "Bomb" in special:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
        else:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+13
            enemyh+=-sub*damagem*10
            print("Damage dealt: "+ str(sub*damagem*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
            input()
        elif fmove=="l":
            health=-1
            input()
        elif fmove=="B" or fmove=="b":
            special.remove("Bomb")
            enemyh=enemyh-1000
            input()
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*3.1*damagem*10
            print("Damage dealt: "+ str(sub*3.1*damagem*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*20)
            health+=-sub*10
            health+=-8*10
            print("Dragon attacks!  Damage dealt: "+ str(sub+8*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You beat the dragon!")
    input()
    rendscreen("The dragon was hoarding:")
    input()
    rendscreen("200 gold...")
    gold+=200
    input()
    rendscreen("A golden vest... that grants double health in all battles.")
    healthm=healthm*2
    special.append("Golden Vest")
    input()
    rendscreen("A sword, that grants 2x damage in all battles.")
    damagem=damagem*2
    special.append("Sword")
    input()
    rendscreen("The path ends there, however.  You walk back.")
    input()
exitarena=0
rendscreen("You go on the left path.")
input()
rendscreen("You walk up to an arena.  There are five monsters.  Here are the arena rules:")
print("You must defeat all 5 enemies.")
print("To enter, you must pay 20 gold.")
input()
enterarena1=0
rendscreen("Do you want to enter the arena?")
while enterarena1!="y" and enterarena1!="Y" and enterarena1!="n" and enterarena1!="N":
    enterarena1=menu([['Yes','Y'],['No','N']],0,'Do you want to enter?')
if enterarena1=="y" or enterarena1=="Y":
    rendscreen("You choose to enter the arena.")
    input()
    gold+=-20
    rendscreen("Moster 1: health: 500")
    input()
    health=healthm*1000+ebhealth
    enemyh=500
    while enemyh>0:
        rendscreenf()
        fmove="0"
        if "Bomb" in special:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
        else:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+13
            enemyh+=-sub*damagem*10
            print("Damage dealt: "+ str(sub*damagem*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
            input()
        elif fmove=="l":
            health=-1
            input()
        elif fmove=="B" or fmove=="b":
            special.remove("Bomb")
            enemyh=-1
            input()
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*3.1*damagem*10
            print("Damage dealt: "+ str(sub*3.1*damagem*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*100)
            health+=-40
            print("Monster attacks!  Damage dealt: "+ str(sub+40))
            input()
        if health<0:
            youlose=0
            print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
            while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                youlose=input()
            if youlose=="A" or youlose=="a":
                gold+=-300
                health=healthm*1000+ebhealth
            else:
                enemyh=-1
                exitarena=1
    if exitarena!=1:
        rendscreen("You beat enemy one!")
        input()
        rendscreen("Enemy 2: health: 1000")
        input()
        health=healthm*1000+ebhealth
        enemyh=1000
        while int(enemyh)>0:
            rendscreenf()
            fmove="0"
            if "Bomb" in special:
                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                    fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
            else:
                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                    fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
            if fmove=="k" or fmove=="K":
                sub=math.floor(random.random()*10)+13
                enemyh+=-sub*damagem*10
                print("Damage dealt: "+ str(sub*damagem*10))
                input()
            elif fmove=="adminpass":
                enemyh=0
                input()
            elif fmove=="l":
                health=-1
                input()
            elif fmove=="B" or fmove=="b":
                special.remove("Bomb")
                enemyh=-1
                input()
            else:
                sub=math.floor(random.random()*10)
                enemyh+=-sub*3.1*damagem*10
                print("Damage dealt: "+ str(sub*3.1*damagem*10))
                input()
            rendscreenf()
            if enemyh>0:
                sub=math.floor(random.random()*100)
                health+=-40
                print("Monster attacks!  Damage dealt: "+ str(sub+40))
                input()
            if health<0:
                youlose=0
                print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                    youlose=input()
                if youlose=="A" or youlose=="a":
                    gold+=-300
                    health=healthm*1000+ebhealth
                else:
                    enemyh=-1
                    exitarena=1
        if exitarena!=1:
            rendscreen("You beat enemy 2!")
            input()
            rendscreen("Enemy 3: health: 1250")
            input()
            health=healthm*1000+ebhealth
            enemyh=1250
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                else:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                if fmove=="k" or fmove=="K":
                    sub=math.floor(random.random()*10)+13
                    enemyh+=-sub*damagem*10
                    print("Damage dealt: "+ str(sub*damagem*10))
                    input()
                elif fmove=="adminpass":
                    enemyh=0
                    input()
                elif fmove=="l":
                    health=-1
                    input()
                elif fmove=="B" or fmove=="b":
                    special.remove("Bomb")
                    enemyh=-1000
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*100)
                    health+=-40
                    print("Monster attacks!  Damage dealt: "+ str(sub+40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                        youlose=input()
                        if youlose=="A" or youlose=="a":
                            gold+=-300
                            health=healthm*1000+ebhealth
                        else:
                            enemyh=-1
                            exitarena=1
                if exitarena!=1:
                    rendscreen("You beat enemy 3!")
                    input()
                    rendscreen("Enemy 4: health: 1500")
                    health=healthm*1000+ebhealth
                    enemyh=1500
                    while enemyh>0:
                        rendscreenf()
                        fmove="0"
                        if "Bomb" in special:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                        else:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                        if fmove=="k" or fmove=="K":
                            sub=math.floor(random.random()*10)+13
                            enemyh+=-sub*damagem*10
                            print("Damage dealt: "+ str(sub*damagem*10))
                            input()
                        elif fmove=="adminpass":
                            enemyh=0
                            input()
                        elif fmove=="l":
                            health=-1
                            input()
                        elif fmove=="B" or fmove=="b":
                            special.remove("Bomb")
                            enemyh=-1
                            input()
                        else:
                            sub=math.floor(random.random()*10)
                            enemyh+=-sub*3.1*damagem*10
                            print("Damage dealt: "+ str(sub*3.1*damagem*10))
                            input()
                        rendscreenf()
                        if enemyh>0:
                            sub=math.floor(random.random()*100)
                            health+=-40
                            print("Monster attacks!  Damage dealt: "+ str(sub+40))
                            input()
                        if health<0:
                            youlose=0
                            print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                            while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                youlose=input()
                            if youlose=="A" or youlose=="a":
                                gold+=-300
                                health=healthm*1000+ebhealth
                            else:
                                enemyh=-1
                                exitarena=1
                    if exitarena!=1:
                        rendscreen("You beat enemy 4")
                        input("Final enemy: health: secret")
                        health=healthm*1000+ebhealth
                        enemyhs=2000
                        enemyh="Secret"
                        while enemyhs>0:
                            rendscreenf()
                            fmove="0"
                            if "Bomb" in special:
                                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                    fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                            else:
                                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                    fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                            if fmove=="k" or fmove=="K":
                                sub=math.floor(random.random()*10)+13
                                enemyhs+=-sub*damagem*10
                                print("Damage dealt: "+ str(sub*damagem*10))
                                input()
                            elif fmove=="adminpass":
                                enemyhs=0
                                input()
                            elif fmove=="l":
                                health=-1
                                input()
                            elif fmove=="B" or fmove=="b":
                                special.remove("Bomb")
                                enemyhs=enemyhs-500
                                input()
                            else:
                                sub=math.floor(random.random()*10)
                                enemyhs+=-sub*3.1*damagem*10
                                print("Damage dealt: "+ str(sub*3.1*damagem*10))
                                input()
                            rendscreenf()
                            if enemyhs>0:
                                sub=math.floor(random.random()*100)
                                health+=-40
                                print("Monster attacks!  Damage dealt: "+ str(sub+40))
                                input()
                            if health<0:
                                youlose=0
                                print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                                while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                    youlose=input()
                                if youlose=="A" or youlose=="a":
                                    gold+=-300
                                    health=healthm*1000+ebhealth
                                else:
                                    enemyhs=-1
                                    enemyh=-1
                                    exitarena=1
                        if exitarena!=1:
                            enemyh=-1
                            rendscreen("You beat all the enemies!")
                            input()
if enterarena1=="y" or enterarena1=="Y" and exitarena==0:
    rendscreen("Prizes:")
    input()
    rendscreen("100 gold")
    gold+=100
    input()
    rendscreen("5 bombs")
    special.append("Bomb")
    special.append("Bomb")
    special.append("Bomb")
    special.append("Bomb")
    special.append("Bomb")
    input()
    rendscreen("A staff: double damage and double health in all battles")
    input()
    special.append("Staff")
    damagem=damagem*2
    healthm=healthm*2
    rendscreen("5 lives")
    lives+=5
    input()
rendscreen("You continue on the path.")
input()
rendscreen("Now, you've beaten the tutorial.  Keep playing against harder enemies and getting better.")
xp=100
mars=0
#gameloop
input()
while True:
    move=random.randint(1,9)
    if move==1 or move==2 or move==3 or move==4 or move==5:
        #path
        path=0
        rendscreenx("The path branches into three directions: left, right, and straight.  Which one do you take?")
        while path!="l" and path!="L" and path!="r" and path!="R" and path!="s" and path!="S":
            path=menu([['Left','L'],['Right','R'],['Straight','S']],random.randint(0,2),'What direction do you go in?')
        if path == "l" or path == "L":
            rendscreenx("You go on the left path.")
            input()
            lpath=random.randint(1,11)
            if lpath==1:
                goldgotten=math.floor(xp/100)
                rendscreenx("You found a chest with " + str(goldgotten) + " gold!")
                gold+=goldgotten
                xp+=1
            elif lpath==2:
                rendscreenx("You walk into a trap and lose a life.")
                lives+=-1
                xp+=2
            elif lpath==3:
                rendscreenx("A massive ant bites you!  Lose a life!")
                lives+=-1
                xp+=3
            elif lpath==4:
                rendscreenx("You found a bomb!")
                special.append("Bomb")
                xp+=1
            elif lpath==5:
                lpath5=random.randint(1,3)
                if lpath5==1:
                    rendscreenx("You found a sword!  It grants double damage in all battles!")
                    special.append("Sword")
                    damagem=damagem*2
                    xp+=10
                else:
                    rendscreenx("You continue on the path.")
                    xp+=1
            elif lpath==6:
                rendscreenx("You got hit by a sharp leaf!  You lose a life.")
                lives+=-1
                xp+=2
            elif lpath==7:
                rendscreenx("You find some food.  You gain 4 lives!")
                lives+=4
                xp+=3
            elif lpath==8:
                rendscreenx("You find a medkit!  Gain 5 lives.")
                lives+=5
                xp+=4
            elif lpath==9:
                #Random special item!
                #rsa=random.randint
                rsa=random.randint(1,5)
                if rsa==1:
                    rendscreenx("You got a bomb!")
                    special.append("Bomb")
                elif rsa==2:
                    rendscreenx("You found a sword!  It gives 2x damage in all battles!")
                    special.append("Sword")
                    damagem=damagem*2
                elif rsa==3:
                    rsa2=random.randint(1,100)
                    if rsa2==1:
                        rendscreen("You found the epic staff!  It grants x10 health and x10 damage in all battles!")
                        special.append("Epic Staff")
                        damagem=damagem*10
                        healthm=healthm*10
                    else:
                        rendscreenx("You got a bomb!")
                        special.append("Bomb")
                elif rsa==4:
                    rendscreenx("You found a cape that grants +500 health in all battles!")
                    ebhealth+=500
                    special.append("Cape")
                elif rsa==5:
                    rendscreenx("You found a stockpile of bombs...5 of them!")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                xp+=20
            elif lpath==10:
                rendscreenx("You fall into a trap and lose a life.")
                lives+=-1
                xp=xp+5
            elif lpath==11:
                rendscreenx("You go to a villge.  They give you 50 gold to stay away from them.  You stay away.")
                gold+=50
                xp+=10
            input()
        elif path=="r" or path=="R":
            rpath=random.randint(1,10)
            if rpath==1:
                rendscreenx("You found a chest with 100 gold!")
                gold+=100
                xp+=2
            elif rpath==2:
                rendscreenx("You step in quicksand. Lose a life!")
                lives+=-1
                xp+=3
            elif rpath==3:
                rendscreenx("A massive frog bites you!  Lose a life!")
                lives+=-1
                xp+=4
            elif rpath==4:
                rendscreenx("You found a bomb!")
                special.append("Bomb")
                xp+=1
            elif rpath==5:
                rpath5=random.randint(1,3)
                if rpath5==1:
                    rendscreenx("You found a staff!  It grants double health in all battles!")
                    healthm=healthm*2
                    special.append("Staff")
                    xp+=15
                else:
                    rendscreenx("You continue on the path.")
                    xp+=1
            elif rpath==6:
                rendscreenx("You got in poison ivy!  You lose a life.")
                lives+=-1
                xp+=2
            elif rpath==7:
                rendscreenx("You find some water.  You gain 2 lives!")
                lives+=2
                xp+=5
            elif rpath==8:
                rendscreenx("You find a medkit!  Gain 8 lives.")
                lives+=8
                xp+=1
            elif rpath==9:
                #Random special item!
                #rsa=random.randint
                rsa=random.randint(1,5)
                if rsa==1:
                    rendscreenx("You got 2 bombs!")
                    special.append("Bomb")
                    special.append("Bomb")
                elif rsa==2:
                    rendscreenx("You found a sword!  It gives 2x damage in all battles!")
                    special.append("Sword")
                    damagem=damagem*2
                elif rsa==3:
                    rsa2=random.randint(1,1000)
                    if rsa2==1:
                        rendscreen("You found the epic sword!  It grants x100 health and x100 damage in all battles!")
                        special.append("Epic Sword")
                        damagem=damagem*100
                        healthm=healthm*100
                        xp+=500
                    else:
                        rendscreenx("You got a bomb!")
                        special.append("Bomb")
                elif rsa==4:
                    rendscreenx("You found a cloak that grants +500 health in all battles!")
                    ebhealth+=500
                    special.append("Cloak")
                elif rsa==5:
                    rendscreenx("You found a stockpile of bombs...10 of them!")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                xp+=20
            elif rpath==10:
                rendscreenx("You get sick and lose a life!")
                lives+=-1
                xp=xp+5
            input()
        else:
            cpath=random.randint(1,10)
            if cpath==1:
                rendscreenx("You found a book that's pretty good.  However, it does nothing.")
                book=random.randint(1,5)
                if book==1:
                    special.append("Harry Potter and the Sorcer's Stone")
                elif book==2:
                    special.append("The Name of this Book is Secret")
                elif book==3:
                    special.append("Surely You’re Joking, Mr. Feynman!")
                elif book==4:
                    special.append("Magnus Chase and the Gods of Asgard")
                elif book==5:
                    special.append("This book hasn't been written yet.")
                xp+=30
            elif cpath==2:
                berriese=0
                while berriese!="y" and berriese!="Y" and berriese!="n" and berriese!="N":
                    rendscreenx("You find some berries.  Do you eat them?")
                    berriese=menu([['Yes','Y'],['No','N']],random.randint(0,2),'Do you eat the berries?')
                if berriese=="y" or berriese=="Y":
                    rendscreenx("They were poisoned! Lose a life!")
                    lives+=-1
                    xp+=10
                else:
                    rendscreenx("You don't eat the berries.")
                    xp+=2
            elif cpath==3:
                berriese=0
                while berriese!="y" and berriese!="Y" and berriese!="n" and berriese!="N":
                    rendscreenx("You find some berries.  Do you eat them?")
                    berriese=menu([['Yes','Y'],['No','N']],random.randint(0,2),'Do you eat the berries?')
                if berriese=="y" or berriese=="Y":
                    rendscreenx("They tasted good! Gain a life!")
                    lives+=1
                    xp+=10
                else:
                    rendscreenx("You don't eat the berries.")
                    xp+=2
            elif cpath==4:
                berriese=0
                while berriese!="y" and berriese!="Y" and berriese!="n" and berriese!="N":
                    rendscreenx("You find some berries.  Do you eat them?")
                    berriese=menu([['Yes','Y'],['No','N']],random.randint(0,1),'Do you eat the berries?')
                if berriese=="y" or berriese=="Y":
                    rendscreenx("You found a bomb under them!")
                    special.append("Bomb")
                    xp+=10
                else:
                    rendscreenx("You don't eat the berries.")
                    xp+=2
            elif cpath==5:
                rendscreenx("You found a cloak!  It grants +300 health in all battles!")
                special.append("Cloak")
                ebhealth+=300
                xp+=5
            elif cpath==6:
                goldf=random.randint(1,xp)
                rendscreenx("You found " + str(goldf) + " gold!")
                gold+=goldf
                xp+=4
            elif cpath==7:
                livel=random.randint(2,4)
                rendscreenx("You fell into a snake hole.  The snake bit you!  Lose " + str(livel) + "lives!")
                lives+=-livel
                xp+=livel*4
            elif cpath==8:
                rendscreenx("You lie down for a nap.")
                input()
                rendscreenx("After you wake up, you see a staff ahead...")
                input()
                rendscreenx("You go to touch it...")
                input()
                rendscreenx("It zaps you! Lose 2 lives!")
                lives+=-2
                input()
                rendscreenx("However, you pick it up, and it's super powerful...")
                input()
                rendscreenx("The lightning staff grants 4x attack power!")
                damagem=damagem*4
                special.append("Lightning Staff")
                xp+=40
            else:
                rendscreenx("You fall down... lose 3 lives!")
                lives+=-3
                xp+=8
            input()
    elif move==6:
        #normal enemy
        #Types
        #Monster 5 HP per XP, bombs destroy Rewards 30 XP
        #Dragon 20 HP per XP, bombs do 500 damage Rewards 60 XP
        #Bear 10 HP per XP, bombs destroy Rewards 20 XP
        #Giant 30 HP per XP, bombs do 1500 damage Rewards 100 XP
        #Mars refugee 40 HP per xp, bombs destroy
        if mars==1:
            type=random.randint(1,5)
        else:
            type=random.randint(1,4)
        if type==1:
            enemy="monster"
            enemyh=5*xp
            bomba="destroy "
            xpe=30
            bombm=9999999999999999999999999999
        elif type==2:
            enemy="dragon"
            enemyh=20*xp
            bomba="do 1000 damage to "
            xpe=60
            bombm=1000
        elif type==3:
            enemy="bear"
            enemyh=10*xp
            bomba="destroy "
            xpe=20
            bombm=9999999999999999999999999999
        elif type==4:
            enemy="giant"
            enemyh=30*xp
            bomba="do 1500 damage to "
            xpe=100
            bombm=1500
        else:
            enemy="martian"
            enemyh=40*xp
            bomba="destroy "
            xpe=200
            bombm=9999999999999999999999999999
        rendscreenx("You come up to a " + enemy + "!")
        input()
        rendscreenx("It wants to fight you!")
        health=healthm*1000+ebhealth
        while enemyh>0:
            rendscreenf()
            fmove="0"
            if "Bomb" in special:
                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                    fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
            else:
                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                    fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
            if fmove=="k" or fmove=="K":
                sub=math.floor(random.random()*10)+13
                enemyh+=-sub*damagem*10
                print("Damage dealt: "+ str(sub*damagem*10))
                input()
            elif fmove=="adminpass":
                enemyh=0
                input()
            elif fmove=="l":
                health=-1
                input()
            elif fmove=="B" or fmove=="b":
                special.remove("Bomb")
                enemyh+=-bombm*damagem
                input()
            else:
                sub=math.floor(random.random()*10)
                enemyh+=-sub*3.1*damagem*10
                print("Damage dealt: "+ str(sub*3.1*damagem*10))
                input()
            rendscreenf()
            if enemyh>0:
                sub=math.floor(random.random()*100*xp/50)
                health+=-40*xp/50
                print(enemy + " attacks!  Damage dealt: "+ str(sub+40*xp/50))
                input()
            if health<0:
                youlose=0
                print("You lost a life!")
                lives+=-1
                health=healthm*1000+ebhealth
        rendscreenx("You beat the "+enemy+"!")
        xp+=xpe
        input()
    elif move==7:
        #arena!
        exitarena=0
        arenatype=random.randint(1,2)
        #up to ten in later updates
        if arenatype==1:
            entry=randint(1,500)
            rendscreen("You choose to enter the arena.")
            input()
            gold+=-20
            rendscreen("Moster 1: health: 500")
            input()
            health=healthm*1000+ebhealth
            enemyh=500
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                else:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                if fmove=="k" or fmove=="K":
                    sub=math.floor(random.random()*10)+13
                    enemyh+=-sub*damagem*10
                    print("Damage dealt: "+ str(sub*damagem*10))
                    input()
                elif fmove=="adminpass":
                    enemyh=0
                    input()
                elif fmove=="l":
                    health=-1
                    input()
                elif fmove=="B" or fmove=="b":
                    special.remove("Bomb")
                    enemyh=-1
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*100)
                    health+=-40
                    print("Monster attacks!  Damage dealt: "+ str(sub+40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                        youlose=input()
                    if youlose=="A" or youlose=="a":
                        gold+=-300
                        health=healthm*1000+ebhealth
                    else:
                        enemyh=-1
                        exitarena=1
            if exitarena!=1:
                rendscreen("You beat enemy one!")
                input()
                rendscreen("Enemy 2: health: 1000")
                input()
                health=healthm*1000+ebhealth
                enemyh=1000
                while int(enemyh)>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                    else:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                    if fmove=="k" or fmove=="K":
                        sub=math.floor(random.random()*10)+13
                        enemyh+=-sub*damagem*10
                        print("Damage dealt: "+ str(sub*damagem*10))
                        input()
                    elif fmove=="adminpass":
                        enemyh=0
                        input()
                    elif fmove=="l":
                        health=-1
                        input()
                    elif fmove=="B" or fmove=="b":
                        special.remove("Bomb")
                        enemyh=-1
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*100)
                        health+=-40
                        print("Monster attacks!  Damage dealt: "+ str(sub+40))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                        while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                            youlose=input()
                        if youlose=="A" or youlose=="a":
                            gold+=-300
                            health=healthm*1000+ebhealth
                        else:
                            enemyh=-1
                            exitarena=1
                if exitarena!=1:
                    rendscreen("You beat enemy 2!")
                    input()
                    rendscreen("Enemy 3: health: 1250")
                    input()
                    health=healthm*1000+ebhealth
                    enemyh=1250
                    while enemyh>0:
                        rendscreenf()
                        fmove="0"
                        if "Bomb" in special:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                        else:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                        if fmove=="k" or fmove=="K":
                            sub=math.floor(random.random()*10)+13
                            enemyh+=-sub*damagem*10
                            print("Damage dealt: "+ str(sub*damagem*10))
                            input()
                        elif fmove=="adminpass":
                            enemyh=0
                            input()
                        elif fmove=="l":
                            health=-1
                            input()
                        elif fmove=="B" or fmove=="b":
                            special.remove("Bomb")
                            enemyh=-1000
                            input()
                        else:
                            sub=math.floor(random.random()*10)
                            enemyh+=-sub*3.1*damagem*10
                            print("Damage dealt: "+ str(sub*3.1*damagem*10))
                            input()
                        rendscreenf()
                        if enemyh>0:
                            sub=math.floor(random.random()*100)
                            health+=-40
                            print("Monster attacks!  Damage dealt: "+ str(sub+40))
                            input()
                        if health<0:
                            youlose=0
                            print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                            while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                youlose=input()
                                if youlose=="A" or youlose=="a":
                                    gold+=-300
                                    health=healthm*1000+ebhealth
                                else:
                                    enemyh=-1
                                    exitarena=1
                        if exitarena!=1:
                            rendscreen("You beat enemy 3!")
                            input()
                            rendscreen("Enemy 4: health: 1500")
                            health=healthm*1000+ebhealth
                            enemyh=1500
                            while enemyh>0:
                                rendscreenf()
                                fmove="0"
                                if "Bomb" in special:
                                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                        fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                                else:
                                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                                if fmove=="k" or fmove=="K":
                                    sub=math.floor(random.random()*10)+13
                                    enemyh+=-sub*damagem*10
                                    print("Damage dealt: "+ str(sub*damagem*10))
                                    input()
                                elif fmove=="adminpass":
                                    enemyh=0
                                    input()
                                elif fmove=="l":
                                    health=-1
                                    input()
                                elif fmove=="B" or fmove=="b":
                                    special.remove("Bomb")
                                    enemyh=-1
                                    input()
                                else:
                                    sub=math.floor(random.random()*10)
                                    enemyh+=-sub*3.1*damagem*10
                                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                                    input()
                                rendscreenf()
                                if enemyh>0:
                                    sub=math.floor(random.random()*100)
                                    health+=-40
                                    print("Monster attacks!  Damage dealt: "+ str(sub+40))
                                    input()
                                if health<0:
                                    youlose=0
                                    print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                        youlose=input()
                                    if youlose=="A" or youlose=="a":
                                        gold+=-300
                                        health=healthm*1000+ebhealth
                                    else:
                                        enemyh=-1
                                        exitarena=1
                            if exitarena!=1:
                                rendscreen("You beat enemy 4")
                                input("Final enemy: health: secret")
                                health=healthm*1000+ebhealth
                                enemyhs=2000
                                enemyh="Secret"
                                while enemyhs>0:
                                    rendscreenf()
                                    fmove="0"
                                    if "Bomb" in special:
                                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 1000 damage in this battle)?')
                                    else:
                                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                                    if fmove=="k" or fmove=="K":
                                        sub=math.floor(random.random()*10)+13
                                        enemyhs+=-sub*damagem*10
                                        print("Damage dealt: "+ str(sub*damagem*10))
                                        input()
                                    elif fmove=="adminpass":
                                        enemyhs=0
                                        input()
                                    elif fmove=="l":
                                        health=-1
                                        input()
                                    elif fmove=="B" or fmove=="b":
                                        special.remove("Bomb")
                                        enemyhs=enemyhs-500
                                        input()
                                    else:
                                        sub=math.floor(random.random()*10)
                                        enemyhs+=-sub*3.1*damagem*10
                                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                                        input()
                                    rendscreenf()
                                    if enemyhs>0:
                                        sub=math.floor(random.random()*100)
                                        health+=-40
                                        print("Monster attacks!  Damage dealt: "+ str(sub+40))
                                        input()
                                    if health<0:
                                        youlose=0
                                        print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                                        while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                            youlose=input()
                                        if youlose=="A" or youlose=="a":
                                            gold+=-300
                                            health=healthm*1000+ebhealth
                                        else:
                                            enemyhs=-1
                                            enemyh=-1
                                            exitarena=1
                                if exitarena!=1:
                                    enemyh=-1
                                    rendscreen("You beat all the enemies!")
                                    input()
            if enterarena1=="y" or enterarena1=="Y" and exitarena==0:
                rendscreen("Prizes")
                input()
                rendscreen(str(entry*5) + " gold")
                gold+=entry*5
                input()
                rendscreen("5 bombs")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                input()
                rendscreen("5 lives")
                lives+=5
                input()
                xp+200
        elif arenatype==2:
            #3 dragons
            #Huge XP
            #HP based on XP
            #1st dragon 10 HP per XP
            #2nd dragon 20 HP per XP
            #3rd dragon random.randint(20,40) HP per XP
            rendscreenx("You walk up to an arena.  There are three dragons.  Here are the arena rules:")
            print("You must defeat all 3 enemies.")
            print("To enter, you must pay 200 gold.")
            input()
            rendscreenx("You enter the arena.")
            exitarena=0
            gold+=-200
            health=healthm*1000+ebhealth
            enemyh=10*xp
            rendscreenx("Dragon 1: " + str(enemyh) + " health")
            input()
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 500 damage in this battle)?')
                else:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                if fmove=="k" or fmove=="K":
                    sub=math.floor(random.random()*10)+13
                    enemyh+=-sub*damagem*10
                    print("Damage dealt: "+ str(sub*damagem*10))
                    input()
                elif fmove=="adminpass":
                    enemyh=0
                    input()
                elif fmove=="l":
                    health=-1
                    input()
                elif fmove=="B" or fmove=="b":
                    special.remove("Bomb")
                    enemyh+=-500*damagem
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*100)
                    health+=-40
                    print("Dragon attacks!  Damage dealt: "+ str(sub+40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost!  You can pay 1000 gold to try this arena again(A), or you can just lose(L).")
                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                        youlose=input()
                    if youlose=="A" or youlose=="a":
                        gold+=-1000
                        health=healthm*1000+ebhealth
                    else:
                        enemyh=-1
                        exitarena=1
            if exitarena!=1:
                health=healthm*1000+ebhealth
                enemyh=20*xp
                rendscreenx("Dragon 2: " + str(enemyh) + " health")
                input()
                while enemyh>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 500 damage in this battle)?')
                    else:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                    if fmove=="k" or fmove=="K":
                        sub=math.floor(random.random()*10)+13
                        enemyh+=-sub*damagem*10
                        print("Damage dealt: "+ str(sub*damagem*10))
                        input()
                    elif fmove=="adminpass":
                        enemyh=0
                        input()
                    elif fmove=="l":
                        health=-1
                        input()
                    elif fmove=="B" or fmove=="b":
                        special.remove("Bomb")
                        enemyh+=-500*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*100)
                        health+=-40
                        print("Dragon attacks!  Damage dealt: "+ str(sub+40))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost!  You can pay 1000 gold to try this arena again(A), or you can just lose(L).")
                        while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                            youlose=input()
                        if youlose=="A" or youlose=="a":
                            gold+=-1000
                            health=healthm*1000+ebhealth
                        else:
                            enemyh=-1
                            exitarena=1
                if exitarena!=1:
                    health=healthm*1000+ebhealth
                    enemyh=random.randint(20,40)*xp
                    rendscreenx("Dragon 3: " + str(enemyh) + " health")
                    input()
                    while enemyh>0:
                        rendscreenf()
                        fmove="0"
                        if "Bomb" in special:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs only deal 500 damage in this battle)?')
                        else:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                        if fmove=="k" or fmove=="K":
                            sub=math.floor(random.random()*10)+13
                            enemyh+=-sub*damagem*10
                            print("Damage dealt: "+ str(sub*damagem*10))
                            input()
                        elif fmove=="adminpass":
                            enemyh=0
                            input()
                        elif fmove=="l":
                            health=-1
                            input()
                        elif fmove=="B" or fmove=="b":
                            special.remove("Bomb")
                            enemyh+=-500*damagem
                            input()
                        else:
                            sub=math.floor(random.random()*10)
                            enemyh+=-sub*3.1*damagem*10
                            print("Damage dealt: "+ str(sub*3.1*damagem*10))
                            input()
                        rendscreenf()
                        if enemyh>0:
                            sub=math.floor(random.random()*100)
                            health+=-40
                            print("Dragon attacks!  Damage dealt: "+ str(sub+40))
                            input()
                        if health<0:
                            youlose=0
                            print("You lost!  You can pay 1000 gold to try this arena again(A), or you can just lose(L).")
                            while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                youlose=input()
                            if youlose=="A" or youlose=="a":
                                gold+=-1000
                                health=healthm*1000+ebhealth
                            else:
                                enemyh=-1
                                exitarena=1
            if exitarena!=1:
                rendscreenx("You won!")
                input()
                rendscreenx("Rewards:")
                input()
                rendscreenx("1000 gold!")
                gold+=1000
                input()
                rendscreenx("10 bombs")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                input()
                rendscreenx("2 lives")
                input()
                rendscreenx("A dragon staff: grants +1000 health in all battles!")
                special.append("Dragon Staff")
                ebhealth+=1000
                input()
                xp+=500
            else:
                rendscreenx("You lost the arena :(")
                input()
                xp+=10
    elif move==8:
        if xp>10000 and mars==0:
            #invasion from Mars!
            i=0
            while i<20:
                i+=1
                enemy="Martian Drone"
                enemyh=50000
                bomba="destroy "
                xpe=30
                bombm=9999999999999999999999999999
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
                input()
                rendscreenx("It wants to fight you!")
                health=healthm*1000+ebhealth
                while enemyh>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
                    else:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                    if fmove=="k" or fmove=="K":
                        sub=math.floor(random.random()*10)+13
                        enemyh+=-sub*damagem*10
                        print("Damage dealt: "+ str(sub*damagem*10))
                        input()
                    elif fmove=="adminpass":
                        enemyh=0
                        input()
                    elif fmove=="l":
                        health=-1
                        input()
                    elif fmove=="B" or fmove=="b":
                        special.remove("Bomb")
                        enemyh+=-bombm*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*10000)
                        health+=-4000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+4000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            i=0
            while i<20:
                i+=1
                enemy="Martian"
                enemyh=60000
                bomba="destroy "
                xpe=30
                bombm=9999999999999999999999999999
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
                input()
                rendscreenx("It wants to fight you!")
                health=healthm*1000+ebhealth
                while enemyh>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
                    else:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                    if fmove=="k" or fmove=="K":
                        sub=math.floor(random.random()*10)+13
                        enemyh+=-sub*damagem*10
                        print("Damage dealt: "+ str(sub*damagem*10))
                        input()
                    elif fmove=="adminpass":
                        enemyh=0
                        input()
                    elif fmove=="l":
                        health=-1
                        input()
                    elif fmove=="B" or fmove=="b":
                        special.remove("Bomb")
                        enemyh+=-bombm*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*10000)
                        health+=-4000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+4000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            i=0
            while i<10:
                i+=1
                enemy="Martian UFO"
                enemyh=100000
                bomba="destroy "
                xpe=30
                bombm=9999999999999999999999999999
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
                input()
                rendscreenx("It wants to fight you!")
                health=healthm*1000+ebhealth
                while enemyh>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
                    else:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                    if fmove=="k" or fmove=="K":
                        sub=math.floor(random.random()*10)+13
                        enemyh+=-sub*damagem*10
                        print("Damage dealt: "+ str(sub*damagem*10))
                        input()
                    elif fmove=="adminpass":
                        enemyh=0
                        input()
                    elif fmove=="l":
                        health=-1
                        input()
                    elif fmove=="B" or fmove=="b":
                        special.remove("Bomb")
                        enemyh+=-bombm*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*20000)
                        health+=-8000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+8000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            i=0
            while i<2:
                i+=1
                enemy="Martian Space Station"
                enemyh=500000
                bomba="deal 1000 damage to "
                xpe=30
                bombm=1000
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
                input()
                rendscreenx("It wants to fight you!")
                health=healthm*1000+ebhealth
                while enemyh>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
                    else:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                            fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                    if fmove=="k" or fmove=="K":
                        sub=math.floor(random.random()*10)+13
                        enemyh+=-sub*damagem*10
                        print("Damage dealt: "+ str(sub*damagem*10))
                        input()
                    elif fmove=="adminpass":
                        enemyh=0
                        input()
                    elif fmove=="l":
                        health=-1
                        input()
                    elif fmove=="B" or fmove=="b":
                        special.remove("Bomb")
                        enemyh+=-bombm*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*18000)
                        health+=-7000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+8000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            enemy="Martian Leader"
            enemyh=500000
            bomba="deal 2000 damage to "
            xpe=30
            bombm=2000
            mars=1
            rendscreeenx("You come up to a " + enemy + "!")
            input()
            rendscreenx("It wants to fight you!")
            health=healthm*1000+ebhealth
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
                else:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                if fmove=="k" or fmove=="K":
                    sub=math.floor(random.random()*10)+13
                    enemyh+=-sub*damagem*10
                    print("Damage dealt: "+ str(sub*damagem*10))
                    input()
                elif fmove=="adminpass":
                    enemyh=0
                    input()
                elif fmove=="l":
                    health=-1
                    input()
                elif fmove=="B" or fmove=="b":
                    special.remove("Bomb")
                    enemyh+=-bombm*damagem
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*18000)
                    health+=-7000
                    print(enemy + " attacks!  Damage dealt: "+ str(sub+8000))
                    input()
                if health<0:
                    youlose=0
                    print("You lost a life!")
                    lives+=-1
            rendscreenx("You beat the "+enemy+"!")
            input()
            if lives>0:
                rendscreenx("You beat the Martian invasion!!!")
                input()
                rendscreenx("Your loot:")
                input()
                rendscreenx("100 Bombs")
                input()
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                rendscreenx("10 swords that grant 2x damage in all battles each!")
                damagem=damagem*1024
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                input()
                rendscreenx("A ray gun... grants 100 damage in all battles!")
                damagem=damagem*100
                special.append("Ray Gun")
                input()
                rendscreenx("A martian cloak: gives +100000 health in all battles!")
                ebhealth+=100000
                input()
                mars=1
                xp+=5000
            else:
                rendscreenx("You were defeated by Mars :(")
                xp+=-1000
                input()
        else:
            rendscreenx("You continue on the path.")
            xp+=1
            input()
    elif move==9:
        rendscreenx("You walk up to a village!")
        input()
        village=random.randint(1,6)
        if village==1:
            #Gods
            rendscreenx("The villagers praise you as their god.  They give you 50 gold.")
            gold+=50
            xp+=10
        elif village==2:
            #Gods
            rendscreenx("The villagers praise you as their god.  They give a sword that grants 3x damage in all battles.")
            special.append("Sword")
            damagem=damagem*3
            xp+=10
        elif village==3:
            #Gods
            rendscreenx("The villagers praise you as their god.  Unfortuatly, they hate their gods.  Lose a life.")
            lives+=-1
            xp+=15
        elif village==4:
            #Gods
            rendscreenx("The villagers praise you as their god.  They find material objects usless, but experience priceless.")
            xp+=100
        elif village==5:
            #Gods
            rendscreenx("The villagers praise you as their god.  They give you 1000 gold.")
            gold+=1000
        elif village==6:
            rendscreenx("The villagers fight you!")
            enemy="villager"
            enemyh=10*xp
            bomba="destroy "
            xpe=10
            bombm=9999999999999999999999999999
            rendscreenx("You come up to a " + enemy + "!")
            input()
            rendscreenx("It wants to fight you!")
            health=healthm*1000+ebhealth
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=menu([['Kick','K'],['Punch','P'],['Bomb','B']],'0','Kick or Punch or use Bomb(bombs '+ bomba + 'the ememy in this battle)?')
                else:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                        fmove=menu([['Kick','K'],['Punch','P']],'0','Kick or Punch?')
                if fmove=="k" or fmove=="K":
                    sub=math.floor(random.random()*10)+13
                    enemyh+=-sub*damagem*10
                    print("Damage dealt: "+ str(sub*damagem*10))
                    input()
                elif fmove=="adminpass":
                    enemyh=0
                    input()
                elif fmove=="l":
                    health=-1
                    input()
                elif fmove=="B" or fmove=="b":
                    special.remove("Bomb")
                    enemyh+=-bombm*damagem
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*100*xp/40)
                    health+=-40*xp/40
                    print(enemy + " attacks!  Damage dealt: "+ str(sub+40*xp/40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost a life!")
                    lives+=-1
            rendscreenx("You beat the "+enemy+"!")
            xp+=xpe
            input()
    time.sleep(.2)