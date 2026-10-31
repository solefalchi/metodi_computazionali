# Definiamo una funzione principale chiamata 'main'. 
def main():
    # --- FASE 1: ACQUISIZIONE DEI DATI ---
    # Utilizziamo un blocco 'try-except'. Serve a "catturare" gli errori.
    # Se l'utente inserisce una lettera invece di un numero, il programma gestiste l'errore 
    
    try:
        # input() legge ciò che l'utente scrive a terminale come se fosse una stringa di testo (es. "5").
        # int() "casta" (converte) questa stringa in un vero e proprio numero intero matematico.
        val1 = int(input("Inserisci il primo numero intero: "))
        val2 = int(input("Inserisci il secondo numero intero: "))
    
    # Se int() fallisce (perché ad esempio abbiamo scritto "ciao"), si attiva il ValueError
    except ValueError:
        print("Errore: non hai inserito un numero intero valido. Il programma termina qui.")
        return # Esce dalla funzione main interrompendo l'esecuzione

    # --- FASE 2: RAPPRESENTAZIONI NELLE DIVERSE BASI ---
    # Il computer ragiona nativamente in binario. Le funzioni bin() e hex() non modificano 
    # il numero reale in memoria, ne cambiano solo la 'forma' in cui ci viene mostrato a schermo.
    print(f"\n--- Rappresentazione dei valori di input ---")
    
    # bin(val1) prende il numero e restit   uisce una stringa che inizia con '0b' seguita dai bit (es. 0b101).
    # hex(val1) fa lo stesso in base 16, restituendo una stringa che inizia con '0x'.
    print(f"Valore 1 ({val1}):")
    print(f"  -> Binario:      {bin(val1)}")
    print(f"  -> Esadecimale:  {hex(val1)}")
    
    print(f"Valore 2 ({val2}):")
    print(f"  -> Binario:      {bin(val2)}")
    print(f"  -> Esadecimale:  {hex(val2)}")

    # --- FASE 3: OPERAZIONI LOGICHE BIT A BIT (BITWISE) ---
    # Le operazioni bitwise non lavorano sul numero nel suo complesso, ma mettono in colonna 
    # i bit dei due numeri e operano riga per riga (proprio come le porte logiche nei circuiti elettronici).
    
    # L'operatore AND ( & ) restituisce 1 SOLO SE entrambi i bit nella stessa posizione sono 1.
    # Se anche solo uno è 0, il risultato è 0. Viene spesso usato per "mascherare" e isolare segnali.
    risultato_and = val1 & val2
    
    # L'operatore OR ( | ) restituisce 1 se ALMENO UNO dei due bit nella stessa posizione è 1.
    # Restituisce 0 solo se entrambi sono 0.
    risultato_or = val1 | val2


    # --- FASE 4: STAMPA DEI RISULTATI BITWISE ---
    print(f"\n--- Risultato operazioni bitwise tra {val1} e {val2} ---")
    
    # Stampiamo l'AND mostrando tutte e tre le rappresentazioni
    print(f"Operazione AND (&):")
    print(f"  Decimale:    {risultato_and}") # Mostra il numero standard in base 10
    print(f"  Binario:     {bin(risultato_and)}") # Mostra il risultato a livello di bit
    print(f"  Esadecimale: {hex(risultato_and)}")

    # Stampiamo l'OR mostrando tutte e tre le rappresentazioni
    print(f"\nOperazione OR (|):")
    print(f"  Decimale:    {risultato_or}")
    print(f"  Binario:     {bin(risultato_or)}")
    print(f"  Esadecimale: {hex(risultato_or)}")
if
# Questo è il "punto di ingresso" standard per gli script Python.
# Dice all'interprete: "Se questo file viene eseguito direttamente (e non importato 
# come modulo in un altro script), allora fai partire la funzione main()".
if __name__ == "__main__":
    main()