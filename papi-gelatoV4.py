# Prijslijst
bolletjePrijs   = 1.10
hoorntjePrijs = 1.25
bakjePrijs   = 0.75
stap2 = 0
toppingsPrijs = 0


# Subtotaal hoorntje bakje
def subtotaal():
    print(f'Subtotaal: €{subtotaalBol + subtotaalHoorn + subtotaalBak + toppingsPrijs}')

# Subtotaal bakje
def subtotaal2():
    print(f'Subtotaal: €{subtotaalBol + bakjePrijs + toppingsPrijs}')

# Betaald bedrag hoorntje bakje
def betaald():
    print(f'Betaald: €{subtotaalBol + subtotaalHoorn + subtotaalBak + toppingsPrijs}')


# Betaald bedrag bakje
def betaald2():
    print(f'Betaald: €{subtotaalBol + bakjePrijs + toppingsPrijs}')
    

# Bon hoorntje hoorntje bakje
def bon():	
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(subtotaalBol, '.2f'))   + ',-')
    print('Horrentje:       €' + str(format(subtotaalHoorn, '.2f')) + ',-')
    print('Bakje:           €' + str(format(subtotaalBak, '.2f'))   + ',-')
    print('Topping:         €' + str(format(toppingsPrijs,     '.2f')) + ',-')
    print('-----------------------------')
    print(subtotaal())
    print(betaald())

# Bon bakje
def bon2():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(subtotaalBol, '.2f'))   + ',-')
    print('Bakje:           €' + str(format(bakjePrijs, '.2f'))   + ',-')
    print('Topping:         €' + str(format(toppingsPrijs,     '.2f'))   + ',-')
    print('-----------------------------')
    print(subtotaal2())
    print(betaald2())


    
# Code voor nog een keer bestellen
def again():
    keuze = input(f'Hier is uw {stap2} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) ')
    if keuze == 'Y':
        stap1()
    elif keuze == 'N':
        print('U kunt nu afrekenen.')
    else:
        print('Sorry, dat snap ik niet...')
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
    global bolletjePrijs, hoorntjePrijs, bakjePrijs, aantal, subtotaalBol, stap2, totaalBolPrijs, subtotaalHoorn, subtotaalBak, hoorntje, bakje, toppings, toppingsPrijs
    keuze = '' ''
    taste = input('Welke smaak wilt u? Aardbei, Chocolade, Munt, Vanille: ')
    print('U heeft voor ' + taste + ' gekozen.')
    aantal = int(input('Hoeveel bolletjes wilt u? '))
    print('U heeft ' + str(aantal) + ' bolletje(s) gekozen.')
    if aantal <= 3:
        stap2 = input(f'Wilt u deze {aantal} bolletje(s) in hoorntje of in een bakje?')
        print('U heeft een ' + stap2 + ' gekozen.')
    subtotaalBol = round(aantal * bolletjePrijs,2)
    hoorntje = 0
    bakje = 0    
    if stap2 == "hoorntje":
        hoorntje += 1
    elif stap2 == "bakje":
        bakje += 1
    elif aantal <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
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
        if toppings ==  "A":
            toppingsPrijs = 0
        elif toppings == "B":
            toppingsPrijs = 0.50
        elif toppings == "C":
            toppingsPrijs = 0.30 * aantal
        elif toppings == "D":
            toppingsPrijs = 0.90
        again2()
    elif aantal > 8:
        print('Sorry, zulke grote bakken hebben we niet')
        stap1()
    subtotaalBak = bakjePrijs * bakje
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
        if hoorntje == 1:
            toppingsPrijs = 0.60
        else:
            toppingsPrijs = 0.90
    again()

stap1()