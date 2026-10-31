"""Esercizio 1
Creare uno script python che:

chieda in input 2 valori interi;
stampi i valori in rappresentazione binaria ed esadecimale;
satmpi il risultato delle operazioni AND e OR bitwise sia in rappresentazione binaria che esadecimale."""

def main():
    try:
        val1 = int(input("Inserisci il primo numero intero: "))
        val2 = int(input("Inserisci il secondo numero intero: "))
    except ValueError:
        print("Errore: non hai inserito un numero intero valido. Il programma termina qui.")
        return

    print(f"\n--- Rappresentazione dei valori di input ---")
    print(f"Valore 1 ({val1}):")
    print(f"  -> Binario:      {bin(val1)}")
    print(f"  -> Esadecimale:  {hex(val1)}")
    print(f"Valore 2 ({val2}):")
    print(f"  -> Binario:      {bin(val2)}")
    print(f"  -> Esadecimale:  {hex(val2)}")


    risultato_and = val1 & val2
    
    risultato_or = val1 | val2

    print(f"\n--- Risultato operazioni bitwise tra {val1} e {val2} ---")
    print(f"Operazione AND (&):")
    print(f"  Decimale:    {risultato_and}")
    print(f"  Binario:     {bin(risultato_and)}")
    print(f"  Esadecimale: {hex(risultato_and)}")
    
    print(f"\nOperazione OR (|):")
    print(f"  Decimale:    {risultato_or}")
    print(f"  Binario:     {bin(risultato_or)}")
    print(f"  Esadecimale: {hex(risultato_or)}")

if __name__ == "__main__":
        main()


