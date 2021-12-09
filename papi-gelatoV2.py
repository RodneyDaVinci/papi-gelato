print('Welkom bij Papi Gelato.')

import time
time.sleep(3)

stap2 = False

# Dit is de hoofdcode van Papi Gelato
def stap1():
    keuze = ""
    stap2 = ""
    smaak = input("Welke smaak wilt u? aardbei. chocolade. munt. vanille. ")
    aantal = int(input("Hoeveel bolletjes wilt u? "))
    if aantal <= 3:
        stap2 = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
    elif aantal <= 8:
        print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes")
        stap2 = True
    elif aantal > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        stap1()
    if stap2 == True:
        stap2 = "bakje"
    keuze = input(f"Hier is uw {stap2} met {aantal} bolletje(s) {smaak} ijs. Wilt u nog meer bestellen? (Y/N) ")
    if keuze == "Y":
        stap1()
    elif keuze == "N":
        print("Bedankt en tot ziens!")
    else:
        print("Sorry, dat snap ik niet...")

stap1()