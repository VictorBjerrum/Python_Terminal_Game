from time import sleep
from random import randint

HjertePoints = []
RuderPoints = []
SparPoints = []
KloverPoints = []

RandomNumber = [randint(1,52)]

for number in RandomNumber:
    if 39 <= number <= 52:
        HjertePoints.append("X")
    elif 26 <= number <= 38:
         RuderPoints.append("X")
    elif 13 <= number <= 25:
        SparPoints.append("X")
    else:
        KloverPoints.append("X")
        
print(HjertePoints, RuderPoints, SparPoints, KloverPoints)