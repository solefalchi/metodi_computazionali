"""
Esercitazione 2 
Le basi di Python
Creare uno script Python che:
chieda in input un numero intero n;
stampi a schermo la somma dei primi n numeri naturali;"""

#importiamo du emoduli integrati standard di python
"""sys per interagire con l'inteprete e il sistema operativo e
os per le interazini con il file system"""
import sys,os

#Definizisco i parametri di input
nmax = 100  #definisce il limite superiore della sequenza

somma = 0 #inizializzo la variabile a 0

for n in range(1,nmax+1):  #in python l'estremo superiore dle range è sempre escluso, quindi per includere 100 devo scrivere nmax+1
    
    somma = somma + n 

    #print( n, 'somma temporanea:', somma)


print('La somma dei primi 100 numeri naturali è:', somma)