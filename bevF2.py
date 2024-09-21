#2.	MegelőzőKövetkezőSzám: A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!

egeszSzam = int(input("Adj meg egy egész számot:"))

if egeszSzam < 10 and egeszSzam > -9 :
    megelozo = egeszSzam-1
    kovetkezo = egeszSzam+1
    print("A(z) " + str(egeszSzam) + " szám megelőző értéke: " + str(megelozo)+ ", kövekező szám értéke: "
          +str(kovetkezo))