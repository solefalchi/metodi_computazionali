"""Esercizio 2 - Operazioni di bit shift
#spostare a sinistra --> moltiplicare
#spostare a destra --> dividere"""


# --- 1. INPUT DELL'UTENTE ---

# input() restituisce sempre una stringa, quindi int() la converte in numero intero.
# Se l'utente scrive qualcosa che non è un intero (es. "ciao"), Python solleva un ValueError.
valore = int(input("Inserisci un valore intero: "))

# Stessa cosa per il numero di posizioni di cui spostare i bit.
n_bit = int(input("Inserisci il numero di bit per lo shift: "))


# --- 2. RAPPRESENTAZIONE DEL VALORE ORIGINALE ---

# "\n" va a capo prima di stampare, per lasciare una riga vuota e rendere l'output leggibile.
print("\nValore originale")

# Le f-string (stringhe che iniziano con f) permettono di inserire
# il risultato di un'espressione dentro le graffe {}.
print(f"  Decimale:     {valore}")

# bin() converte un intero in una stringa binaria con prefisso "0b".
# Esempio: bin(12) -> '0b1100'
print(f"  Binario:      {bin(valore)}")

# hex() converte un intero in una stringa esadecimale con prefisso "0x".
# Esempio: hex(12) -> '0xc'
print(f"  Esadecimale:  {hex(valore)}")


# --- 3. OPERAZIONI DI BIT SHIFT ---

# Shift a sinistra (<<): sposta tutti i bit verso sinistra di n_bit posizioni,
# riempiendo a destra con zeri. Equivale a moltiplicare per 2**n_bit.
# Esempio: 12 << 2 -> 1100 diventa 110000 (cioè 48)
shift_sx = valore << n_bit

# Shift a destra (>>): sposta i bit verso destra di n_bit posizioni,
# scartando quelli che escono. Equivale a una divisione intera per 2**n_bit.
# Esempio: 12 >> 2 -> 1100 diventa 11 (cioè 3)
shift_dx = valore >> n_bit


# --- Stampa del risultato dello shift a sinistra ---

# Nel titolo inseriamo anche l'operazione eseguita, ad esempio "12 << 2".
print(f"\nShift a sinistra ({valore} << {n_bit})")
print(f"  Decimale:     {shift_sx}")
print(f"  Binario:      {bin(shift_sx)}")
print(f"  Esadecimale:  {hex(shift_sx)}")


# --- Stampa del risultato dello shift a destra ---

print(f"\nShift a destra ({valore} >> {n_bit})")
print(f"  Decimale:     {shift_dx}")
print(f"  Binario:      {bin(shift_dx)}")
print(f"  Esadecimale:  {hex(shift_dx)}")