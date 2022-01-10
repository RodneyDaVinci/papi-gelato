# Prijslijst
bolletjePrijs   = 0.95
hoorntjePrijs = 1.25
bakjePrijs   = 0.75
stap2 = 0
toppingsPrijs = 0
belasting = 0.9
i = 0
particulier = False
zaak = False


# Subtotaal hoorntje bakje
def subtotaal():
    print(f'Subtotaal: €{subtotaalBol + subtotaalHoorn + subtotaalBak + toppingsPrijs}')

# Subtotaal bakje
def subtotaal2():
    print(f'Subtotaal: €{subtotaalBol + bakjePrijs + toppingsPrijs}')
    

# Subtotaal liters
def TotaalL():
    print(f'Subtotaal: €{liter + prijsLiter}')

# Betaald bedrag hoorntje bakje
def betaald():
    print(f'Betaald: €{subtotaalBol + subtotaalHoorn + subtotaalBak + toppingsPrijs}')


# Betaald bedrag bakje
def betaald2():
    print(f'Betaald: €{subtotaalBol + bakjePrijs + toppingsPrijs}')
    

# Bon hoorntje hoorntje bakje
def bon():	
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€0.95 '+ '= ' + '€' + str(format(subtotaalBol, '.2f'))   + ',-')
    print('Horrentje:       €' + str(format(subtotaalHoorn, '.2f')) + ',-')
    print('Bakje:           €' + str(format(subtotaalBak, '.2f'))   + ',-')
    print('Topping:         €' + str(format(toppingsPrijs,     '.2f')) + ',-')
    print('-----------------------------')
    print(subtotaal())
    print(betaald())

# Bon zakelijk
def bonL():
    print('--------[Papi Gelato]--------')
    print('Liter:   '      + str(liter) + ' x ' + '€9,80 '+ '= ' + '€' + str(format(prijsLiter, '.2f'))   + ',-')
    print('-----------------------------')
    print('BTW (9%)' + str(format(belasting, '.2f')) + ',-')

# Bon bakje
def bon2():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€0.95 '+ '= ' + '€' + str(format(subtotaalBol, '.2f'))   + ',-')
    print('Bakje:           €' + str(format(bakjePrijs, '.2f'))   + ',-')
    print('Topping:         €' + str(format(toppingsPrijs,     '.2f'))   + ',-')
    print('-----------------------------')
    print(subtotaal2())
    print(betaald2())

# Bon zakelijke markt
def bonL2():
    print('--------[Papi Gelato]--------')
    print('Liter:   '      + str(liter) + ' x ' + '€9,80 '+ '= ' + '€' + str(format(prijsLiter, '.2f'))   + ',-')
    print('-----------------------------')
    print('BTW (9%)' + str(format(belasting, '.2f')) + ',-')


    
# Code voor nog een keer bestellen
def again():
    keuze = input(f'Hier is uw {stap2} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) ')
    if keuze == 'Y':
        stap1()
    elif keuze == 'N':
        print('U kunt nu afrekenen.')
    else:
        print('“Sorry dat is geen optie die we aanbieden...')
    bon()

# Nog een keer bestellen bakje
def again2():
    kies = (f'Hier is uw bakje met {aantal} bolletje(s).')
    print('U kunt nu afrekenen.')
    bon2()

print('Welkom bij Papi Gelato.')


import time
time.sleep(3)

#Dit is de hoofdcode van Papi Gelato
def stap1():
    global bolletjePrijs, hoorntjePrijs, bakjePrijs, aantal, subtotaalBol, stap2, totaalBolPrijs, subtotaalHoorn, subtotaalBak, hoorntje, bakje, toppings, toppingsPrijs, particulier, zaak, liter, prijsLiter, smaakLiter, belasting, tasteLiter, keuze
    keuze = ""
    stap2 = ""
    
    pofz = input('Bent u p) particulier of z) zakelijk? ')
    if pofz == 'p':
        particulier = True
        aantal = int(input('Hoeveel bolletjes wilt u? '))
        print('U heeft ' + str(aantal) + ' bolletje(s) gekozen.')
        if aantal <= 8:
            i = 1
            while i <= aantal:
                taste = input('Welke smaak wilt u voor bolletje ' + str(i) + '? ')
                i += 1
        else:
            print('Sorry, zulke grote bakken hebben we niet')
            stap1()
        if aantal <= 3:
            stap2 = input(f'Wilt u deze {aantal} bolletje(s) in hoorntje of in een bakje? ')
            print('U heeft een ' + stap2 + ' gekozen.')
        elif aantal <= 8:
            print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes {taste}')
            bakje = 1
        elif aantal > 8:
            print('Sorry, zulke grote bakken hebben we niet')
            stap1()
        else:
            print('“Sorry dat is geen optie die we aanbieden...')
            stap1()
        
        subtotaalBol = round(aantal * bolletjePrijs,2)
        hoorntje = 0
        bakje = 0
        if stap2 == 'hoorntje':
            hoorntje += 1
        elif stap2 == 'bakje':
            bakje += 1
        subtotaalBak   = bakjePrijs   * bakje
        subtotaalHoorn = hoorntjePrijs * hoorntje
        
        toppings = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?: ')
        if toppings == "A":
            A = True
        elif toppings == "B":
            B = True
        elif toppings == "C":
            C = True
        elif toppings == "D":
            D = True
        if toppings == "A":
            toppingsPrijs = 0
        elif toppings == "B":
            toppingsPrijs = 0.50
        elif toppings == "C":
            toppingsPrijs = 0.30 * aantal
        elif toppings == "D":
            if bakje == 1:
                toppingsPrijs = 0.60
            else:
                toppingsPrijs = 0.90
        else:
            print('“Sorry dat is geen optie die we aanbieden...')
            stap1()
        bon()
    elif pofz == 'z':
        liter = int(input('Hoeveel liter ijs wilt u bestellen? '))
        print(f'U heeft gekozen voor {liter} liter ijs')
        i = 1
        while i <= liter:
            tasteLiter = input('Welke smaak wilt u voor liter ' + str(i) + '? ')
            i += 1
        prijsLiter = liter * 9.80
        belasting = (prijsLiter / 109) * 9
        bonL()
    
    else:
        print('“Sorry dat is geen optie die we aanbieden...')
        stap1()

stap1()