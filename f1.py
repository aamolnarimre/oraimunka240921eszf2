

import math

#Gyakorló feladatok1. feladat – Abszolútérték1 A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz a math.fabs használd!


szam = float(input("Aj meg egyy való számot!"))
eredmeny = math.fabs(szam)
print("|" + str(szam)+"|="+str(eredmeny))