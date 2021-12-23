from time import sleep
from random import randint

print("""
                        """)
print("Velkommen til væddeløb!")
print("""
----------------------------------------------------------
        """)
print("""Regler til drukspillet: Hver spiller får lov til at satse på en af fire vædeløbsheste: Hjerter, Spar, Ruder og Kløver.

Hver skal spiller skal vælge et antal slurke der satses på at en vædeløbshest, kommer først i mål. 

Hvis din vædeløbshest vinder, må du dele det antal slurke ud.

Hvis din vedeløbshest taber, skal du til gengæld drikke halvdelen af det antal slurke du satsede.""")                      
print("""
----------------------------------------------------------
        """)

sleep(2)

print("Start med at indtast hvem der spiller")
print("""
                        """)

sleep(2)

SpillerEtNavn = input("Hvad hedder spiller 1? ")
print("""
        """)
SpillerToNavn = input("Hvad hedder spiller 2? ")
print("""
        """)
SpillerTreNavn = input("Hvad hedder spiller 3? ")
print("""
        """)
SpillerFireNavn = input("Hvad hedder spiller 4? ")

print("""
----------------------------------------------------------
        """)

print("""TAST "H" for at vælge hjerte, TAST "R" for at vælge ruder, TAST "K" for at vælge kløver, TAST "S" for at vælge spar""")

print("""
----------------------------------------------------------

        """)


#Spiller 1 loop

while True:
                try:
                        ValgEt = input("Vælg H, R, K eller S " + SpillerEtNavn + " " )
                        if ValgEt == "H":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Hjerter")
                                print("""
                        """)
                                break
                        elif ValgEt == "R":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Ruder")
                                print("""
                        """)
                                break
                        elif ValgEt == "K":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Kløver")
                                print("""
                        """)
                                break
                        elif ValgEt == "S":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Spar")
                                print("""
                        """)
                                break
                        else:   
                                sleep(0.5)
                                print("""

                        """)
                                print("Du skal vælge H, R, K eller S")
                        print("""

                        """)
                except ValueError:
                        print("Du skal vælge H, R, K eller S")
                        print("""
                        """)
                        sleep(1)
                continue

while True:
                try:    
                        SatsningEt = int(input("Hvor mange slurke satser du " + SpillerEtNavn  + "? "))
                        break
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)
                continue

sleep(0.5)
print("""
                        """)
print("Du har satset: " + str(SatsningEt) + " slurk(e)")
print("""
                        """)

#Spiller 2 loop

while True:
                try:
                        ValgTo = input("Vælg H, R, K eller S " + SpillerToNavn + " " )
                        if ValgTo == "H":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Hjerter")
                                print("""
                        """)
                                break
                        elif ValgTo == "R":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Ruder")
                                print("""
                        """)
                                break
                        elif ValgTo == "K":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Kløver")
                                print("""
                        """)
                                break
                        elif ValgTo == "S":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Spar")
                                print("""
                        """)
                                break
                        else:   
                                sleep(0.5)
                                print("""

                        """)
                                print("Du skal vælge H, R, K eller S")
                        print("""

                        """)
                except ValueError:
                        print("Du skal vælge H, R, K eller S")
                        print("""
                        """)
                        sleep(1)
                continue

while True:
                try:    
                        SatsningTo = int(input("Hvor mange slurke satser du " + SpillerToNavn  + "? "))
                        if SatsningTo == int:
                                print("Du har satset: " + str(SatsningTo) + " slurk(e)")
                        break
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)
                continue

sleep(0.5)
print("""
                        """)
print("Du har satset: " + str(SatsningTo) + " slurk(e)")
print("""
                        """)

#Spiller 3 loop

while True:
                try:
                        ValgTre = input("Vælg H, R, K eller S " + SpillerTreNavn + " " )
                        if ValgTre == "H":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Hjerter")
                                print("""
                        """)
                                break
                        elif ValgTre == "R":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Ruder")
                                print("""
                        """)
                                break
                        elif ValgTre == "K":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Kløver")
                                print("""
                        """)
                                break
                        elif ValgTre == "S":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Spar")
                                print("""
                        """)
                                break
                        else:   
                                sleep(0.5)
                                print("""

                        """)
                                print("Du skal vælge H, R, K eller S")
                        print("""

                        """)
                except ValueError:
                        print("Du skal vælge H, R, K eller S")
                        print("""
                        """)
                        sleep(1)
                continue

while True:
                try:    
                        SatsningTre = int(input("Hvor mange slurke satser du " + SpillerTreNavn  + "? "))
                        if SatsningTre == int:
                                print("Du har satset: " + str(SatsningTre) + " slurk(e)")
                        break
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)
                continue

sleep(0.5)
print("""
                        """)
print("Du har satset: " + str(SatsningTre) + " slurk(e)")
print("""
                        """)


#Spiller 4 loop

while True:
                try:
                        ValgFire = input("Vælg H, R, K eller S " + SpillerFireNavn + " " )
                        if ValgFire == "H":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Hjerter")
                                print("""
                        """)
                                break
                        elif ValgFire == "R":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Ruder")
                                print("""
                        """)
                                break
                        elif ValgFire == "K":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Kløver")
                                print("""
                        """)
                                break
                        elif ValgFire == "S":
                                sleep(0.5)
                                print("""
                        """)
                                print("Du har valgt Spar")
                                print("""
                        """)
                                break
                        else:   
                                sleep(0.5)
                                print("""

                        """)
                                print("Du skal vælge H, R, K eller S")
                        print("""

                        """)
                except ValueError:
                        print("Du skal vælge H, R, K eller S")
                        print("""
                        """)
                        sleep(1)
                continue

while True:
                try:    
                        SatsningFire = int(input("Hvor mange slurke satser du " + SpillerFireNavn  + "? "))
                        if SatsningFire == int:
                                print("Du har satset: " + str(SatsningFire) + " slurk(e)")
                        break
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)
                continue

sleep(0.5)
print("""
                        """)
print("Du har satset: " + str(SatsningFire) + " slurk(e)")
print("""
                        """)



HjertePoints = 0
RuderPoints = 0
SparPoints = 0
KloverPoints = 0

HjerteTegn = []
RuderTegn = []
SparTegn = []
KloverTegn = []

VinderEt = ""
VinderTo = ""
VinderTre = ""
VinderFire = ""

sleep(2)

print("Så har alle afgivet deres bets")

sleep(2)

print("""
                        """)

print("Væddeløbet starter nu:")

print("""
                        """)
print("-----------------------------------------------------")
print("""
                        """)

while HjertePoints != 6 and RuderPoints != 6 and SparPoints != 6 and KloverPoints != 6:
    RandomNumber = [50]
    for number in RandomNumber:
        if 39 <= number <= 52:
            HjertePoints += 1
            HjerteTegn.append("X")
        elif 26 <= number <= 38:
            RuderPoints += 1
            RuderTegn.append("X")
        elif 13 <= number <= 25:
            SparPoints += 1
            SparTegn.append("X")
        else:
            KloverPoints += 1
            KloverTegn.append("X")
        sleep(4)
        print("Hjerte")
        print(HjerteTegn)
        print("""
        """)
        print("Ruder")
        print(RuderTegn)
        print("""
        """)
        print("Spar")
        print(SparTegn)
        print("""
        """)
        print("Kløver")
        print(KloverTegn)
        print("""
        
        """)
        print("-----------------------------------------------------")
        print("""
        
        """)
        if RuderPoints == 6:
                print("Ruder vandt!")
                print("""
        """)
                if ValgEt == "R":
                        sleep(1)
                        print("""
        """)
                        print(SpillerEtNavn + " må dele " + str(SatsningEt) + " ud")
                        print("""
        """)
                        VinderEt = SpillerEtNavn 
                if ValgTo == "R":
                        sleep(1)
                        print("""
        """)
                        print(SpillerToNavn + " må dele " + str(SatsningTo) + " ud")
                        print("""
        """)
                        VinderTo = SpillerToNavn 
                if ValgTre == "R":
                        sleep(1)
                        print("""
        """)
                        print(SpillerTreNavn + " må dele " + str(SatsningTre) + " ud")
                        print("""
        """)
                        VinderTre = SpillerTreNavn
                if ValgFire == "R":
                        sleep(1)
                        print("""
        """)
                        print(SpillerFireNavn + " må dele " + str(SatsningFire) + " ud")
                        print("""
        """)
                        VinderFire = SpillerFireNavn
                elif ValgFire != "R" and ValgTre != "R" and ValgTo != "R" and ValgEt != "R":
                        print("Ingen vindere denne gang")
        if KloverPoints == 6:
                print("Kløver vandt!")
                print("""
        """)
                if ValgEt == "K":
                        sleep(1)
                        print("""
        """)
                        print(SpillerEtNavn + " må dele " + str(SatsningEt) + " ud")
                        print("""
        """)
                        VinderEt = SpillerEtNavn 
                if ValgTo == "K":
                        sleep(1)
                        print("""
        """)
                        print(SpillerToNavn + " må dele " + str(SatsningTo) + " ud")
                        print("""
        """)
                        VinderTo = SpillerToNavn 
                if ValgTre == "K":
                        sleep(1)
                        print("""
        """)
                        print(SpillerTreNavn + " må dele " + str(SatsningTre) + " ud")
                        print("""
        """)
                        VinderTre = SpillerTreNavn
                if ValgFire == "K":
                        sleep(1)
                        print("""
        """)
                        print(SpillerFireNavn + " må dele " + str(SatsningFire) + " ud")
                        print("""
        """)
                        VinderFire = SpillerFireNavn
                elif ValgFire != "K" and ValgTre != "K" and ValgTo != "K" and ValgEt != "K":
                        print("Ingen vindere denne gang")

        elif HjertePoints == 6:
                print("Hjerter vandt!")
                print("""
        """)
                if ValgEt == "H":
                        sleep(1)
                        print("""
        """)
                        print(SpillerEtNavn + " må dele " + str(SatsningEt) + " ud")
                        print("""
        """)
                        VinderEt = SpillerEtNavn 
                if ValgTo == "H":
                        sleep(1)
                        print("""
        """)
                        print(SpillerToNavn + " må dele " + str(SatsningTo) + " ud")
                        print("""
        """)
                        VinderTo = SpillerToNavn 
                if ValgTre == "H":
                        sleep(1)
                        print("""
        """)
                        print(SpillerTreNavn + " må dele " + str(SatsningTre) + " ud")
                        print("""
        """)
                        VinderTre = SpillerTreNavn
                if ValgFire == "H":
                        sleep(1)
                        print("""
        """)
                        print(SpillerFireNavn + " må dele " + str(SatsningFire) + " ud")
                        print("""
        """)
                        VinderFire = SpillerFireNavn
                elif ValgFire != "H" and ValgTre != "H" and ValgTo != "H" and ValgEt != "H":
                        print("Ingen vindere denne gang")
        elif SparPoints == 6:
                print("Spar vandt!")
                print("""
        """)
                if ValgEt == "S":
                        sleep(1)
                        print("""
        """)
                        print(SpillerEtNavn + " må dele " + str(SatsningEt) + " ud")
                        VinderEt = SpillerEtNavn
                if ValgTo == "S":
                        sleep(1)
                        print("""
         """)
                       
                        print(SpillerToNavn + " må dele " + str(SatsningTo) + " ud")
                        print("""
         """)
                        VinderTo = SpillerToNavn 
                if ValgTre == "S":
                        sleep(1)
                        print("""
         """)
                        print(SpillerTreNavn + " må dele " + str(SatsningTre) + " ud")
                        print("""
        """)
                        VinderTre = SpillerTreNavn
                if ValgFire == "S":
                        sleep(1)
                        print("""
        """)
                        print(SpillerFireNavn + " må dele " + str(SatsningFire) + " ud")
                        print("""
        """)
                        VinderFire = SpillerFireNavn
                elif ValgFire != "S" and ValgTre != "S" and ValgTo != "S" and ValgEt != "S":
                        print("""
        
        """)
                        print("Ingen vindere denne gang")
                        print("""
        
        """)
                break

sleep(1)

if VinderEt == SpillerEtNavn:

        print(SpillerEtNavn + " skal vælge, hvem der skal drikke " + str(SatsningEt) + " slurk(e)")
        print("""
        
        """)
        sleep(2)

        while True:
                try:    
                        SlurkEt = int(input(SpillerToNavn + "? Tast 1   /" +
                        SpillerTreNavn + "? Tast 2   /" +
                        SpillerFireNavn + "? Tast 3   "))
                        if SlurkEt == 1:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerToNavn + " skal drikke " + str(SatsningEt) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkEt == 2:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerTreNavn + " skal drikke " + str(SatsningEt) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkEt == 3:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerFireNavn + " skal drikke " + str(SatsningEt) + " slurk(e)" )
                                print("""
        
        """)
                                break
                        continue
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)

sleep(1)

if VinderTo == SpillerToNavn:

        print(SpillerToNavn + " skal vælge, hvem der skal drikke " + str(SatsningTo) + " slurk(e)")
        print("""
        
        """)
        sleep(2)

        while True:
                try:    
                        SlurkTo = int(input(SpillerEtNavn + "? Tast 1   /" +
                        SpillerTreNavn + "? Tast 2   /" +
                        SpillerFireNavn + "? Tast 3   "))
                        if SlurkTo == 1:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerEtNavn + " skal drikke " + str(SatsningTo) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkTo == 2:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerTreNavn + " skal drikke " + str(SatsningTo) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkTo == 3:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerFireNavn + " skal drikke " + str(SatsningTo) + " slurk(e)" )
                                print("""
        
        """)
                                break
                        continue
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)

sleep(1)
    
if VinderTre == SpillerTreNavn:

        print(SpillerTreNavn + " skal vælge, hvem der skal drikke " + str(SatsningTre) + " slurk(e)")
        print("""
        
        """)
        sleep(2)

        while True:
                try:    
                        SlurkTre = int(input(SpillerEtNavn + "? Tast 1   /" +
                        SpillerToNavn + "? Tast 2   /" +
                        SpillerFireNavn + "? Tast 3   "))
                        if SlurkTre == 1:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerEtNavn + " skal drikke " + str(SatsningTre) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkTre == 2:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerToNavn + " skal drikke " + str(SatsningTre) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkTre == 3:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerFireNavn + " skal drikke " + str(SatsningTre) + " slurk(e)" )
                                print("""
        
        """)
                                break
                        continue
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)
                

sleep(1)

if VinderFire == SpillerFireNavn:

        print(SpillerFireNavn + " skal vælge, hvem der skal drikke " + str(SatsningFire) + " slurk(e)")
        print("""
        
        """)
        sleep(2)

        while True:
                try:    
                        SlurkFire = int(input(SpillerEtNavn + "? Tast 1   /" +
                        SpillerToNavn + "? Tast 2   /" +
                        SpillerTreNavn + "? Tast 3   "))
                        if SlurkFire == 1:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerEtNavn + " skal drikke " + str(SatsningFire) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkFire == 2:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerToNavn + " skal drikke " + str(SatsningFire) + " slurk(e)")
                                print("""
        
        """)
                                break
                        if SlurkFire == 3:
                                sleep(2)
                                print("""
        
        """)
                                print(SpillerTreNavn + " skal drikke " + str(SatsningFire) + " slurk(e)" )
                                print("""
        
        """)
                                break
                        continue
                except ValueError:
                        print("Du skal vælge et tal")
                        print("""
                        """)
                        sleep(1)
                

sleep(1)

print("""
                        """)

print("STRAFRUNDE: Alle der tabte skal drikke halvdelen af de slurke de satsede.")

print("""
                        """)
sleep(3)

if VinderEt != SpillerEtNavn:
        sleep(2)
        print(SpillerEtNavn + " skal drikke " + str(SatsningEt/2) + " slurk(e)")
        print("""
                        """)
if VinderTo != SpillerToNavn:
        sleep(2)
        print(SpillerToNavn + " skal drikke " + str(SatsningTo/2) + " slurk(e)")
        print("""
                        """)
if VinderTre != SpillerTreNavn:
        sleep(2)
        print(SpillerTreNavn + " skal drikke " + str(SatsningTre/2) + " slurk(e)")
        print("""
                        """)
if VinderFire != SpillerFireNavn:
        sleep(2)
        print(SpillerFireNavn + " skal drikke " + str(SatsningFire/2) + " slurk(e)")
        print("""
                        """)
else:
        sleep(2)
        print("Alle har vundet!")

