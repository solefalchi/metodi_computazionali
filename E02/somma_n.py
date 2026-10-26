"""
Esercitazione 2
Le basi di Python
Creare uno script Python che:
chieda in input un numero intero n;
stampi a schermo la somma dei primi n numeri naturali;"""


import sys,os #includo i moduli

    #Richiedo un numero per la somma
print('Questo programma calcola la somma dei primi N numeri naturali')
Nin = input('Immettere il valore di N: ') #con la funzione input() chiedo all'utente di inserire un numero intero, comunico con l'esterno
    #input restituisce sempre una stringa, anche se l'utente digita un numero intero
    # converto input in intero, perche per operazioni matematiche ho bisogono di un numero
nmax = int(Nin)  #convergo la stringa in un intero, salvandolo nella variabile nmax

somma = 0 #inizializzo l'accomulatore

for n in range(1,nmax+1):
    
    somma = somma + n

    #print( n, 'somma temporanea:', somma)


print('-----------------------------------------------------------')
print('La somma dei primi {:d} numeri naturali è: {:d}'.format(nmax, somma))
    #all'interno delle parentesi graffe, al momento dell'esecuzione, dovrò inserire dei valori
    #d all'interno delle graffe sta per decimal integer (numero intero decimale). evita di stampare numeri con la virgola
    #.format(nmax, somma), Prende le variabili elencate tra le sue parentesi tonde e le inserisce nelle graffe nell'ordine sequenziale:
    #La prima variabile, nmax, finisce nella prima coppia {...} (sostituendo {:d}).
    #La seconda variabile, somma, finisce nella seconda coppia {...} (sostituendo il secondo {:d}).
print('-----------------------------------------------------------')
