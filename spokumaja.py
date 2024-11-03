import random

# Inicializē mainīgos
inventory = []
player_alive = True

# Funkcija, kas parāda inventāru
def show_inventory():
    if inventory:
        print("\033[94mTavs inventārs:\033[0m", ", ".join(inventory))
    else:
        print("\033[94mInventārs ir tukšs.\033[0m")

# Funkcija, kas parāda karti ar pieejamām istabām
def show_map():
    print("\033[92mKarte:\033[0m Ieeja , Foajē , Virtuve , Dzīvojamā istaba , Pagrabs")

# Funkcija, lai palaistu spēli un uzturētu spēles cilpu, kamēr spēlētājs ir dzīvs
def start_game():
    print("Sveicināts Piedzīvojums Spoku Mājā! \033[92m Lai apskatītu inventāru un karti, izmanto 'inventārs' vai 'karte'  \033[0m ")
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā' vai bēgt 'prom'?")
    choice = ""
    while choice not in ["iekšā", "prom"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        elif choice == "inventārs":
            show_inventory()
        elif choice == "karte":
            show_map()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir durvis uz 'virtuvi', 'dzīvojamo istabu', 'pagrabu' un 'izejas durvis' .")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba", "noslēpumainā istaba", "izeja"]:
        choice = input(">>> ").lower()
        if choice == "virtuvi":
            kitchen()
        elif choice == "dzīvojamo istabu":
            living_room()
        elif choice == "pagrabu":
            mysterious_room()
        elif choice == "izejas durvis":
            if "atslēga" in inventory:
                print("\033[92mTev ir atslēga! Tu atslēdz durvis un izbēdz no spoku mājas. Tu uzvari!\033[0m")
                end_game()
            else:
                print("\033[91mDurvis ir aizslēgtas. Tev nepieciešama atslēga, lai izietu.\033[0m")
                foyer()
        elif choice == "inventārs":
            show_inventory()
        elif choice == "karte":
            show_map()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def kitchen():
    print("Tu esi virtuvē. Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
    choice = ""
    while choice not in ["cīnīties", "bēgt"]:
        choice = input(">>> ").lower()
        if choice == "cīnīties":
            if "nazis" in inventory:
                print("\033[92mTu uzvarēji spoku ar nazi! Spoks nokrīt, un tu atrodi atslēgu.\033[0m")
                inventory.append("atslēga")
                print("Tu paņēmi atslēgu.")
                foyer()
            else:
                print("\033[91mTev nav ar ko aizstāvēties, un spoks tevi uzvarēja. Spēle beigusies.\033[0m")
                end_game()
        elif choice == "bēgt":
            print("Tu aizbēdzi atpakaļ uz foajē.")
            foyer()
        elif choice == "inventārs":
            show_inventory()
        elif choice == "karte":
            show_map()
        else:
            print("Nepareiza izvēle.")

def living_room():
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vai vēlies 'skatīties' spogulī vai iet 'atpakaļ'? Šeit ir arī durvis uz 'guļamistabu'")
    choice = ""
    while choice not in ["skatīties", "atpakaļ" , "guļamistabu"]:
        choice = input(">>> ").lower()
        if choice == "skatīties":
            print("\033[91mSpogulis ir nolādēts! Tu pārvērties par spoku. Spēle beigusies.\033[0m")
            end_game()
        elif choice == "guļamistabu":
           print("\033[91mDurvis kaut kas bloķē no otras puses, to nebūs iespējams atvērt.\033[0m")
           living_room()
        elif choice == "atpakaļ":
            foyer()
        elif choice == "inventārs":
            show_inventory()
        elif choice == "karte":
            show_map()
        else:
            print("Nepareiza izvēle.")

def mysterious_room():
    print("Tu esi pagrabā. Uz galda redzi piezīmi un nazi.")
    choice = ""
    while choice not in ["ņem piezīmi", "ņem nazi", "atpakaļ"]:
        print("Vai vēlies 'ņemt piezīmi', 'ņemt nazi' vai iet 'atpakaļ'?")
        choice = input(">>> ").lower()
        if choice == "ņemt piezīmi":
            if "piezīme" not in inventory:
                inventory.append("piezīme")
                print("\033[94mTu paņēmi piezīmi. Tajā rakstīts: 'Uzmanies no spoguļa dzīvojamā istabā!'\033[0m")
            else:
                print("Piezīme jau ir tavā inventārā.")
        elif choice == "ņemt nazi":
            if "nazis" not in inventory:
                inventory.append("nazis")
                print("Tu paņēmi nazi. Tas var noderēt cīņā ar spokiem.")
            else:
                print("Tev jau ir nazis.")
        elif choice == "atpakaļ":
            foyer()
        elif choice == "inventārs":
            show_inventory()
        elif choice == "karte":
            show_map()
        else:
            print("Nepareiza izvēle.")

 

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

# Sāk spēli
start_game()

