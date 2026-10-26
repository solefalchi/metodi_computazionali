"""
Esercitazione 2
Le basi di Python
Sviluppare uno script python che

Crei una lista con i nomi dei giorni della settimana
Crei una lista col nome dei giorni della settimana per tutto il mese di ottobre 2026
Crei un dizionario che metta in relazione il giorno del mese di ottobre 2026 con il giorno della settimana
Stampi la correlazione fra giorno del mese e della settimana a schermo.

"""

#Viene definita una lista base (week) contenente i sette giorni della settimana in ordine cronologico, da Lunedì a Domenica.
week = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

print(week)


# Lista con i giorni della settimana nel mese di ottobre 2026
ottobre = week[3:]+week*3+week[:6]    
    #week[3:] prende gli elementi della lista a partire dall'indice 3 (ottobre inizia da giovedi)
    #week*3: Ripete l'intera lista dei giorni per tre volte (coprendo i cicli successivi di settimane piene).
    #week[:5]: Prende i primi 5 giorni della settimana (da 'Lunedì' a 'Venerdì') per completare i 31 giorni totali del mese.
print(ottobre)


# Dizionario ottobre 2026 per giorno del mese e della settimana
dict_ottobre = {}
for i in range(len(ottobre)):
    #len(ottobre) restituisce il numero totale di giorni (31).
    #range(len(ottobre)) genera gli indici da 0 a 30.
    dict_ottobre.update({ i+1: ottobre[i] })
        #Ad ogni iterazione, .update() aggiunge una coppia chiave-valore al dizionario.
        #La chiave è il giorno del mese (i+1, quindi da 1 a 31), mentre il valore è il nome del giorno della settimana (ottobre[i]).

print()
print('Dizionario metodo base', dict_ottobre)


"""secondo metodo

dict_ottobre_lc = { i+1 : ottobre[i] for i in range(len(ottobre)) }

print()
print('Dizionario da list comprehension',  dict_ottobre_lc)




# Stampa a schermo dizionario
print('\n=======================================================')
print('================= Ottobre 2025 ========================')
print('=======================================================')
for k in dict_ottobre_lc:

    print('||{:5d}{:.>36}{:>12}'.format(k, dict_ottobre_lc[k], '||') )
print('=======================================================')
"""