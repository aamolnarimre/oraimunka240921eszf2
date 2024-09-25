#3.	Osztályzat1: A program olvasson be a konzolról egy egész számot! Ha a szám 0 és 100 közötti, akkor
# legyen a beolvasott szám egy százalékérték!
# A program írja ki a konzolra a százalékban megadott értékelést szövegesen
#(0%–59%-ig elégtelen, 60%–69%-ig elégséges,
#70%–79%-ig közepes, 80%–89%-ig jó, 90%–100%-ig jeles)!
#Ha a szám nem 0 és 100 közötti, akkor a program írja ki a konzolra, hogy „Hiba: érvénytelen százalék!”!



szam = int(input("Kérem adjon meg egy százalékértéket: "))
if (szam >= 0) and (szam <= 100):
    # jó eset
    if (szam >= 0) and (szam < 59):
        print("elégtelen")
    elif (szam >= 60) and (szam < 69):
        print("elégséges")
    elif (szam >= 70) and (szam < 79):
        print("közepes")
    elif (szam >= 80) and (szam < 89):
        print("jó")
    elif (szam >= 90) and (szam < 100):
        print("jeles")
else:
    #rossz szám eset
    print("Hiba: érvénytelen százalék!")

#Tesztelés:
#határértékekre: 59,69,80,0,60,70,79,89,100
#BE: 59: Ki: semmi Műküdés: hibás , mert = jel hiányzik a szám felé ugyanez igaz 69,79,89,100-nál

#határo kívüli értékek: -10, 105
#Be: -10 Ki: érvénytelen százalék! Működés: ok
#Be: 105 Ki: érvénytelen százalék! Működés: ok

#belső értékek: 10, 62, 75, 88, 94
#Be: 10 Ki: elégtelen Működés
# Be: 62 Ki: elégséges Működés:ok
# Be: 75 Ki: közepes Működés: ok
# Be: 88 Ki: jó Működés: ok
# Be: 94 Ki: jeles Működés: ok

#Pl: Be:59 Ki:elégtelen  Működés: ok







