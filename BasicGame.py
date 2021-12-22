from time import sleep
from random import randint

print("Velkommen til væddeløb! Start med at indtast hvem der spiller")

#NOTE TO SELF: Det skal gøres sådan at du ikke kan komme videre før du har valgt en rigtig værdi

sleep(2)

SpillerEtNavn = input("Hvad hedder spiller 1?")
print("""
        """)
SpillerToNavn = input("Hvad hedder spiller 2?")
print("""
        """)
SpillerTreNavn = input("Hvad hedder spiller 3?")
print("""
        """)
SpillerFireNavn = input("Hvad hedder spiller 4?")

print("""
----------------------------------------------------------
        """)

print("""TAST "H" for at vælge hjerte, TAST "R" for at vælge ruder, TAST "K" for at vælge kløver, TAST "S" for at vælge spar""")

print("""
----------------------------------------------------------

        """)

ValgEt = input("Vælg H, R, K eller S " + SpillerEtNavn)
print("""
        """)

for Valg in ValgEt:
    while Valg != "H" or Valg != "R" or Valg != "K" or Valg != "S":
        print("Du skal vælge enten H, R, K eller S")
    

SatsningEt = input("Hvor mange slurke satser du " + SpillerEtNavn  + "?")
print("""
        """)

ValgTo = input("Vælg H, R, K eller S " + SpillerToNavn )
print("""
        """)
for Valg in ValgTo:
    if Valg != "H" or Valg != "R" or Valg != "K" or Valg != "S":
        print("Du skal vælge enten H, R, K eller S")

SatsningTo = input("Hvor mange slurke satser du " + SpillerToNavn + "?")
print("""
        """)

ValgTre = input("Vælg H, R, K eller S " + SpillerTreNavn)
print("""
        """)

for Valg in ValgTre:
    if Valg != "H" or Valg != "R" or Valg != "K" or Valg != "S":
        print("Du skal vælge enten H, R, K eller S")

SatsningTre = input("Hvor mange slurke satser du" + SpillerTreNavn + "?")
print("""
        """)

ValgFire = input("Vælg H, R, K eller S " + SpillerFireNavn)
print("""
        """)

for Valg in ValgFire:
    if Valg != "H" or Valg != "R" or Valg != "K" or Valg != "S":
        print("Du skal vælge enten H, R, K eller S")

SatsningFire = input("Hvor mange slurke satser du " + SpillerFireNavn + "?")
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


print("Væddeløbet starter om")
sleep(1)
print("5")
sleep(1)
print("4")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("NU!!!")
print("""

        """)



while HjertePoints != 6 and RuderPoints != 6 and SparPoints != 6 and KloverPoints != 6:
    RandomNumber = [randint(1,52)]
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
        sleep(5)
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
        elif KloverPoints == 6:
               print("Kløver vandt!")
               print("""
        
        """)
        elif HjertePoints == 6:
                print("Hjerter vandt!")
                print("""
        
        """)
        elif SparPoints == 6:
                print("Spar vandt!")
                print("""
        
        """)
        break





    

