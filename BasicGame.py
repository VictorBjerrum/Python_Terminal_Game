from time import sleep
from random import randint


HjertePoints = 0
RuderPoints = 0
SparPoints = 0
KloverPoints = 0

HjerteTegn = []
RuderTegn = []
SparTegn = []
KloverTegn = []


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
        sleep(2)
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
                print("Ruder vandt")
                print("""
        
        """)
        elif KloverPoints == 6:
               print("Kløver vandt")
               print("""
        
        """)
        elif HjertePoints == 6:
                print("Hjerter vandt")
                print("""
        
        """)
        elif SparPoints == 6:
                print("Spar vandt")
                print("""
        
        """)
        break



    

