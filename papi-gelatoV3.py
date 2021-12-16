# Prijslijst
bolletjePrijs   = 1.10
hoorntjePrijs = 1.25
bakjePrijs   = 0.75
stap2 = 0


# Subtotaal hoorntje bakje
def subtotaal():
    print(f'Subtotaal: €{subtotaalBol + subtotaalHoorn + subtotaalBak}')

# Subtotaal bakje
def subtotaal2():
    print(f'Subtotaal: €{subtotaalBol + bakjePrijs}')

# Betaald bedrag hoorntje bakje
def betaald():
    print(f'Betaald: €{subtotaalBol + subtotaalHoorn + subtotaalBak}')


# Betaald bedrag bakje
def betaald2():
    print(f'Betaald: €{subtotaalBol + bakjePrijs}')
    

# Bon hoorntje hoorntje bakje
def bon():	
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(subtotaalBol, '.2f'))   + ',-')
    print('Horrentje:       €' + str(format(subtotaalHoorn, '.2f')) + ',-')
    print('Bakje:           €' + str(format(subtotaalBak, '.2f'))   + ',-')
    print('-----------------------------')
    print(subtotaal())
    print(betaald())

# Bon bakje
def bon2():
    print('--------[Papi Gelato]--------')
    print('Bolletjes:   '      + str(aantal) + ' x ' + '€1,10 '+ '= ' + '€' + str(format(subtotaalBol, '.2f'))   + ',-')
    print('Bakje:           €' + str(format(bakjePrijs, '.2f'))   + ',-')
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
    global bolletjePrijs, hoorntjePrijs, bakjePrijs, aantal, subtotaalBol, stap2, totaalBolPrijs, subtotaalHoorn, subtotaalBak, hoorntje, bakje
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
        again2()
    elif aantal > 8:
        print('Sorry, we hebben geen grootere bakjes.') 
        stap1() 
    subtotaalBak   = bakjePrijs   * bakje
    subtotaalHoorn = hoorntjePrijs * hoorntje
    again()

stap1()