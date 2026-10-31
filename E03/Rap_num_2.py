""" Esercizio 2
Creare uno script python che:

chieda in input un valore intero e il numero di bit cui applicare delle operazioni di bit shift;
stampi il valore intero in rappresentazione binaria ed esadecimale;
satmpi il risultato delle operazioni di bit shift (<< e>>) sia in rappresentazione binaria che esadecimale."""


# input() restituisce sempre una stringa, quindi int() la converte in numero intero.
# Se l'utente scrive qualcosa che non è un intero (es. "ciao"), Python solleva un ValueError.
valore = int(input("Inserisci un valore intero: "))

# Stessa cosa per il numero di posizioni di cui spostare i bit.
n_bit = int(input("Inserisci il numero di bit per lo shift: "))

print("\nValore originale")

# Le f-string (stringhe che iniziano con f) permettono di inserire
# il risultato di un'espressione dentro le graffe {}.
print(f"  Decimale:     {valore}")

# bin() converte un intero in una stringa binaria con prefisso "0b".

print(f"  Binario:      {bin(valore)}")

# hex() converte un intero in una stringa esadecimale con prefisso "0x".

print(f"  Esadecimale:  {hex(valore)}")

# Shift a sinistra (<<): sposta tutti i bit verso sinistra di n_bit posizioni,
# riempiendo a destra con zeri. Equivale a moltiplicare per 2**n_bit.

shift_sx = valore << n_bit

# Shift a destra (>>): sposta i bit verso destra di n_bit posizioni,
# scartando quelli che escono. Equivale a una divisione intera per 2**n_bit.

shift_dx = valore >> n_bit

print(f"\nShift a sinistra ({valore} << {n_bit})")
print(f"  Decimale:     {shift_sx}")
print(f"  Binario:      {bin(shift_sx)}")
print(f"  Esadecimale:  {hex(shift_sx)}")


print(f"\nShift a destra ({valore} >> {n_bit})")
print(f"  Decimale:     {shift_dx}")
print(f"  Binario:      {bin(shift_dx)}")
print(f"  Esadecimale:  {hex(shift_dx)}")