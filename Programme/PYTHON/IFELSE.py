y = 100
x = 101

# Einfache IF Bedingungen
if x > y: # Abfrage ob x kleiner ist als y
 print("x ist größer als y") # die Print-Anweisung auf Python muss eingerückt sein, um anzuzeigen das diese zum IF-Block gehört.

if x <= y:
 print("x ist kleiner als y")
else: # Bei else muss ein : Doppelpunkt
 print("x ist nicht kleiner als y")
 
# if-elif-eles-Bedingung

if x == y: # Die erste Bedingung die überprüft wird
 print("x ist gleich y") # Die erste Bedigungen überprüft ob x den gleichen Wert hat wie y
 # Wenn die Bedingung wahr ist, wird der CodeBlock "print" unterhalb der ersten Bedingung ausgeführt.

# elif überprüft verschiedene Bedingungen um entsprechend unterschiedliche Aktionen auszuführen. Diese Bedingung wird nur überprüft wenn die vorherige Bedingung falsch war.
elif x > y: # Es wird geprüft ob der Wert x größer als y ist
 print("x is größer als y") # Wenn die Bedingung wahr ist, wird der CodeBlock "print" unterhalb dieser Zeile ausgeführt.


else: # else wird nur ausgeführt, wenn keine der vorherigen if- oder elif Bedingungen wahr war
 print("x ist kleiner als y") # in diesem Fall bedeutet das, dass x nicht gleich oder größer als y ist, also x muss kleiner als y sein.


# Logische Operator "and", ist dafür da um zwei Bedingungen gleichzeitig zu überprüfen.
z = 150
if x > y and x > z:
  print("x ist größer als y und z")

if x < y or x < z:
 print("x ist entweder kleiner als y oder kleiner als z")

# Weiete Logische Operatoren: Python unterstützt auch andere logische Operatoren wie or (oder) und not (nicht).

# and gibt nur True zurück wenn beide bedingungen True sind.
# or gibt True zurück wenn mindestens eine Bedingung True ist.
# not negiert das Ergebnis einer Bedingung.


