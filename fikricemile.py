import random
import time

charhp = 120
FikriHp = 200
CemileHp = 200
BossDmg = random.randint(20, 100)


#karakter ismi
#yol seçimi
#karşılama
#kaçma olasılığı
#savaş

charName = str(input("Name Your Hero:     "))
entryPoint = int(input("CHOOSE YOUR WAY: 1(DARK WOODS), 2(ABANDONED CİTADEL)"))
if entryPoint == 1:
    print("As you wander across the foggy and dark forest, you come across an ancient beast named FİKRİ. Be silent.")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    time.sleep(2)
    print(".")
    prblty = 1
    if prblty == 1:
        print("He saw you. Take position!   ")
        while charhp > 0 and FikriHp > 0:
            AskForAction = int(input("Take Action... 1(TEKME) 2(FİST) 3(FİYUFİT)"))
            if AskForAction == 1:
                dmg = 40
            elif AskForAction == 2:
                dmg = 50
            elif AskForAction == 3:
                dmg = 100
            else:
                print("Take Action...")
                continue
        #boss'a hasar atıcaz
            FikriHp -= dmg
            print(f"FİKRİ took -{dmg} damage. FİKRİ has {FikriHp} left. ")
            if FikriHp <= 0:
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print("You Have Defeated Fikri...")
                break
            else:
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print("It's FİKRİ's turn... ")
                charhp -= BossDmg
                print(f"{charName} took -{BossDmg} damage. He has {charhp} health left. ")
                if charhp <= 0:
                    print(f"{charName} Has died...")
                    break
    else:
        print("He hasn't noticed you. You are free to go.")
elif entryPoint == 2:
    print("As you wander inside the abandoned dusty halls of the ancient citadel, you come across an ancient beast named CEMİLE. Be silent...   ")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    prblty = random.randint(1,5)
    if prblty >= 3:
        print("She has noticed you. Take position!  ")
        while charhp > 0 and CemileHp > 0:
            AskForAction = int(input("Take Action: 1(Kick) 2(Fist) 3(FİKRİ'S bite)"))
            if AskForAction == 1:
                dmg = 40
            elif AskForAction == 2:
                dmg = 50
            elif AskForAction == 3:
                dmg = 100
            else:
                print("Take Action...")
                continue
        #boss'a hasar atıcaz
            CemileHp -= dmg
            print(f"CEMİLE took -{dmg} damage. She has {CemileHp} health left.")
            if CemileHp <= 0:
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print("CEMİLE has been defeated...  ")
                break
            else:
                time.sleep(3)
                print("İTS CEMİLE'S TURN")
                charhp -= BossDmg
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print(f"{charName} took -{BossDmg} damage. He has {charhp} health left. ")
                if charhp <= 0:
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    print(f"{charName} Has Died...")
                    break
    else:
        print("She haven't noticed you. You're free to leave.")
else:
    print("Unknown Input Try Again:     ")



#New Route 
#1 goes downward 2 goes upward
UpwardRiddle = False
if CemileHp == 0:
    print("After you defeat the ancient being you see an endless looking stairs leaning towards the sky, guarded by two stone guardians. 'SAY THE WORD!' they say...    ")
    time.sleep(2)
    UpwardQnA = str(input("You think for a second and answer out loud:      ")).lower()
    if UpwardQnA == "smough":
        UpwardRiddle = True
    else:
        while True:
            UpwardQnA2 = str(input("You have one more chance..."))
            if UpwardQnA2 == "smough":
                UpwardRiddle = True
                break
            else:
                print("You have lost your chance... ")
                break

if UpwardRiddle == True:
    print("As you go up in between the light halos from clouds, you feel the aura of an angelic being, yet it terrifies you. ")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    
    AoHp = 1000
    AoDmg = 50
    charhp = 500
    
    while AoHp > 0 and charhp > 0:
        AOaction = int(input("AO has challenged you... Take action: 1(kick)-2(fist)-3(faithful strike)   "))
        
        if AOaction == 1:
            CharDmg = 100
        elif AOaction == 2:
            CharDmg = 150
        elif AOaction == 3:
            CharDmg = 200
        else:
            print("Invalid action, try again.")
            continue

        # Senin saldırın
        AoHp -= CharDmg
        print(f"AO took -{CharDmg} dmg leaving with {AoHp} HP")
        if AoHp <= 0:
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated AO. You are now the king of the universe.  ")
            break

        # AO’nun saldırısı
        charhp -= AoDmg
        print(f"{charName} took -{AoDmg} dmg leaving with {charhp} HP")
        if charhp <= 0:
            print("You died in the heaven...    ")
            break
