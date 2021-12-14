print('Welkom bij Papi Gelato.')

import time
time.sleep(3)

# Dit is de hoofdcode van Papi Gelato
def stap1():
    keuze = "" ""
    taste = input("Welke smaak wilt u? Aardbei, Chocolade, Munt of Vanille? ")
    aantal = int(input("Hoeveel bolletjes wilt u? "))
    if aantal <= 3:
        stap2 = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
    elif aantal <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes")
        exit()
    elif aantal > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        stap1()
    keuze = input(f"Hier is uw {stap2} met {aantal} bolletje(s) {taste}. Wilt u nog meer bestellen? (Y/N)")
    if keuze == 'Y':
        stap1()
    elif keuze == 'N':
        print("Bedankt en tot ziens!")
    else:
        print("Sorry dat snap ik niet...")

stap1()