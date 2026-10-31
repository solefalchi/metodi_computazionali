"""Creare uno script python che:

legga il file kplr010666592-2011240104155_slc.csv e crei il DataFrame pandas corrispondente;
stampi il nome delle colonne del DataFrame;
produca un grafico del flusso in funzione del tempo
    suggerimento: usare pyplot.plot;
produca un grafico del flusso in funzione del tempo coi punti del grafico demarcati da un simbolo (no linea);
    suggerimento: usare pyplot.plot con opzione 'o' o equivalente;
produca un grafico del flusso in funzione del tempo con barre di errore e salvi il risultato in un file png e/o pdf;
    suggerimento: usare pyplot.errorbar;
produca un grafico simile al precedente selezionando un intervallo temporale attorno ad uno dei minimi;
    suggerimento: usare .loc per la serezione dei valori nel DataFrame;
produca un grafico come per il punto 5 ma con la selezione del punto 6 mostrata come riquadro.
    suggerimento: utilizzare inset_axes """


"""
TIME: il tempo (asse x)
PDCSAP_FLUX: la luminosità della stella (asse y)
PDCSAP_FLUX_ERR: l’errore sulla luminosità (barre di errore)
TIME è un tempo in giorni. Per questo nell’etichetta dell’asse x c’è scritto BJD - 2454833.
"""


# importo le librerie necessarie per il calcolo numerico, la gestione dei dati e la creazione dei grafici

import sys, os                   # moduli di sistema (qui non vengono usati davvero)
import numpy as np               # calcolo numerico (qui non usato, ma e' standard importarlo)
import pandas as pd              # lettura e gestione dei dati in tabelle (DataFrame)

import matplotlib.pyplot as plt  # creazione dei grafici


#Dati input: file CSV con i dati della curva di luce della stella KIC 10666592 (Kepler-1)

# Percorso del file CSV: puo' essere un URL (lettura diretta da internet)
kplr1 = 'https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv'

# Alternativa: file scaricato in locale nella cartella "dati". 
#kplr1 = 'dati/kplr010666592-2011240104155_slc.csv'

# Legge il CSV e lo trasforma in un DataFrame pandas (una tabella con righe e colonne)
kplrdf = pd.read_csv(kplr1)

# Stampa i nomi delle colonne del DataFrame (punto 2 dell'esercizio)
print('Columns:', kplrdf.columns)
#print(lcdf)   # (riga commentata) stamperebbe il contenuto della tabella


# ------------- Colonne usate per i grafici ----------------------------------------------
"""TIME: il tempo (asse x)
PDCSAP_FLUX: la luminosità della stella (asse y)
PDCSAP_FLUX_ERR: l’errore sulla luminosità (barre di errore)
TIME è un tempo in giorni. Per questo nell’etichetta dell’asse x c’è scritto BJD - 2454833."""


#  Grafici senza errori 


## Grafico Flusso vs. Tempo (punto 3): punti uniti da una linea
plt.subplots(figsize=(12,6))                        # crea una nuova figura 12x6 
plt.plot(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'])     # asse x = tempo, asse y = flusso
plt.axvspan(947.9, 948.35, color='orange', alpha=0.5) #per capire che parte sto zoommando 
plt.xlabel('Time (BJD - 2454833)', fontsize=14)     # etichetta asse x
plt.ylabel(r'Flux ($e^-/s$)', fontsize=14)          # etichetta asse y (r'' + $..$ = formula LaTeX)
plt.xticks(fontsize=14)                             # dimensione dei numeri sull'asse x
plt.yticks(fontsize=14)                             # dimensione dei numeri sull'asse y
plt.savefig('curva_luce_linea.png')
plt.show()                                          # mostra il grafico


## Grafico Flusso vs. Tempo con simbolo, senza linea (punto 4)
plt.subplots(figsize=(12,6))
plt.plot(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], 'o')   # 'o' = solo pallini, niente linea
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce_punti.png')  
plt.show()


# Grafici con errori   

## Grafico Flusso vs. Tempo con barre di errore, salvato come png e pdf (punto 5)
plt.subplots(figsize=(12,6))
# errorbar e' come plot ma disegna anche le barre di errore verticali (yerr).
# fmt='.' = solo piccoli punti, senza linea di collegamento
plt.errorbar(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], yerr=kplrdf['PDCSAP_FLUX_ERR'], fmt='.')

plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce.png')   # salva la figura come immagine PNG
plt.savefig('curva_luce.pdf')   # salva la stessa figura come PDF
plt.show()                      # savefig va SEMPRE prima di show, altrimenti il file risulta vuoto




## Zoom attorno a un minimo, salvato come png e pdf (punto 6)
plt.subplots(figsize=(12,6))
# .loc[condizione, 'colonna'] seleziona solo le righe che soddisfano la condizione.
# Qui la condizione e': tempo compreso tra 947.9 e 948.35 (zona di un transito).
# Servono le parentesi e l'operatore & (non "and") per combinare due condizioni.
# Lo stesso filtro viene applicato a tempo, flusso ed errore, cosi' i tre array
# hanno la stessa lunghezza e sono coerenti tra loro.
plt.errorbar(      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'TIME'],
                   kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX'],
              yerr=kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'],
              fmt='.', color='royalblue')   # color cambia il colore dei punti

plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('curva_luce_zoom.png')
plt.savefig('curva_luce_zoom.pdf')
plt.show()




## Grafico completo con riquadro (inset), salvato come png e pdf (punto 7)
# Qui servono gli oggetti fig e ax (gli assi principali), perche' l'inset
# viene creato come "figlio" di ax.
fig, ax = plt.subplots(figsize=(12,6))

# Grafico completo con barre di errore
plt.errorbar(kplrdf['TIME'], kplrdf['PDCSAP_FLUX'], yerr=kplrdf['PDCSAP_FLUX_ERR'], fmt='.', color='cornflowerblue')
plt.xlabel('Time (BJD - 2454833)', fontsize=14)
plt.ylabel(r'Flux ($e^-/s$)',      fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(1.012e6, 1.030e6)   # limita l'asse y: ingrandisce i dati e lascia spazio al riquadro

# Creo l'inset: [x, y, larghezza, altezza] espressi come frazioni (0-1) degli assi principali.
# Qui parte al 65% in orizzontale e 62% in verticale, ed e' largo/alto il 32%
# --> si trova in alto a destra.
ins_ax = ax.inset_axes([.65, .62, .32, .32])

# Dentro il riquadro disegno lo stesso zoom del punto 6 (stesso filtro sul tempo)
ins_ax.errorbar(      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'TIME'],
                      kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX'],
                 yerr=kplrdf.loc[ (kplrdf['TIME']> 947.9) & (kplrdf['TIME']< 948.35), 'PDCSAP_FLUX_ERR'],
                 fmt='.', color='royalblue')


# Salvataggio su file (sempre prima di show)
plt.savefig('curva_luce_inset.png')
plt.savefig('curva_luce_inset.pdf')

plt.show()