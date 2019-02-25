import modeli
import baza
import sqlite3
import os
import datetime
now = datetime.datetime.now()
f = open("views/letnoPorocilo.txt", "w+")


f.write("Letno poročilo\n\n")

intervencije = modeli.vse_intervencije()
def dodaj_intervencije(intervencije, leto=2018):
    f.write("Vse intervencije iz leta "+  str(leto) + ":\n")
    for i in range(len(intervencije)):
        inter = intervencije[i]
        zac_leto = inter[1].split(".")[2]

        if int(zac_leto) == leto:
            niz = str(i+1) + ". " +inter[1] + ", " + inter[3] + ", " + inter[5] + "\n"
            f.write(niz)

    return None
dodaj_intervencije(intervencije, 2018)
f.close()

