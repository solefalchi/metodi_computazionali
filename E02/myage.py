""" 
Esercizio 2
Le basi di python
Creare uno script Python che:

chieda in input la vostra data di nascita;
calcoli la vostra età in anni, giorni e secondi;
stampi a schermo i risultati con stringhe formattatate in modo che appaiano incolonnati; per svolgere quetsa parte è necessario familiarizzare con il modulo datetime:
"""

import sys,os
from datetime import datetime, timedelta
    #datetime (per gestire oggetti che combinano data e ora)
    #timedelta (per rappresentare una differenza o intervallo di tempo tra due date).

# Richiesta data di nascita 
print('Questo programma calcola la vostra età in anni, giorni e secondi')
mybirthday = input('Immettere la data di nascita (d-m-y): ')
    #definisco data da stringa formattata giorno-mese-anno
mybdaydate = datetime.strptime(mybirthday, "%d-%m-%Y")
    #prende la stringa inserita dall'utente e la converte in un vero e proprio oggetto datetime di Python 
    #seguendo il formato specificato ("%d-%m-%Y" = giorno a due cifre, trattino, mese a due cifre, trattino, anno a quattro cifre).
    #Senza questa conversione, Python vedrebbe la data come una semplice sequenza di caratteri e non potrebbe fare calcoli matematici.

# data e ora attuale
datenow = datetime.now()
print('La data attuale è: {:d}-{:d}-{:d}'.format( datenow.day, datenow.month, datenow.year))
    #datetime.now() restituisce data e ora esatte del sistema nel momento in cui lo script viene eseguito.
    #L'istruzione di stampa usa il metodo .format() inserendo i singoli attributi (day, month, year) dell'oggetto datenow nei segnaposto {:d} (che indicano un numero intero).
# calcolo direttamente dfferenza in anni
age_years = datenow.year - mybdaydate.year
if datenow.month < mybdaydate.month or ( datenow.month == mybdaydate.month and datenow.day < mybdaydate.day):
    age_years-=1

    ##La correzione: Tuttavia, questa semplice sottrazione non basta perché non tiene conto del giorno esatto del compleanno nell'anno in corso. Se ad esempio oggi è ottobre e sei nata a novembre, quell'anno in più non è ancora "scattato".
    #La struttura condizionale if verifica esattamente questo: se il mese attuale è precedente al mese di nascita, oppure se siamo nello stesso mese ma il giorno attuale è precedente al giorno di nascita, significa che il compleanno di quest'anno non è ancora arrivato. Di conseguenza, l'età viene decrementata di uno (age_years -= 1).


# calcolo differenza temporale con datetime
datediff = datenow - mybdaydate
    #Sottraendo direttamente due oggetti datetime (datenow - mybdaydate), Python restituisce un oggetto di tipo timedelta (datediff), che rappresenta l'intervallo di tempo trascorso.

# differenza temporale in secondi 
datediff_sec = datediff.total_seconds()
    #Il metodo .total_seconds() converte quell'intervallo interamente in secondi

# età in secondi
age_secs  = int( datediff_sec )  
    #age_secs converte il risultato in un numero intero (int())

# età in ore
age_hours = int( datediff_sec / (60 * 60) )
    #age_hours calcola le ore dividendo i secondi totali per $3600$ 



# stampa risultati 
print('-------------------------------------------------------')
print('  Data di nascita  {:02d}-{:02d}-{:d}'.format( mybdaydate.day, mybdaydate.month, mybdaydate.year))
print('  Data attuale     {:02d}-{:02d}-{:d}'.format( datenow.day,    datenow.month,    datenow.year))
print()
print('  Età    [anni]: {:>12d}'.format(age_years))
print('  Età     [ore]: {:>12d} - {:>6d} khr'.format(age_hours, int(age_hours/1000)))
print('  Età [secondi]: {:>12d} - {:>6d} Ms'.format(age_secs,   int(age_secs/1e6)  ))
print('-------------------------------------------------------')