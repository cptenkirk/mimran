# Variablen Speichern mit Wetrte


# Variablen sind Container, in denen man Daten speichern kann. In diesem Fall sind die Variablen als "name" und "alter" deklariert.
# String hier ist die Variable "name" der den Wert "mehmet" speichert. Und "mehmet" als Wert, ist ein String, also eine Zeichenkette (eine Folge von Zeichen)
# Der String muss in einem Anführungszeichen"" gesetzt werden.
name = "mehmet" 

# alter ist die Variable der den Wert 25 speichert. Der Wert 25 ist eine ganze Zahl ohne Kommastellen also ein Integer.
alter = 25 # integer





# Typumwandlung (Casting) In diesem Code sind zwei Datentypen, String(Zeichenkette) und Integer(ganze Zahl), es ist oft notwendig Datentypen umzuwandeln.
# Wert einer Variable ändern, sie ändert den Wert der Variable "alter" 25 in 26 um.
alter = 39

# Dieser Code ändert den alter 
alter_str  = str(alter) # alter_str Bedeutung, das Suffix "_str" vom "alter", ist eine Konvention um anzuzeigen, dass eine Variable ein String-Wert enthält. str(): ist eine eingebaute Funktion in Python (und auch in anderen Programmiersprachen). str() wandelt den Wert vom "alter" in diesem Fall "str(alter)" die 25 in 26 um. Der Rückgabewert der Funktion "str()" wird immer ein String sein.


# Werte ausgeben
print("Name : ", name)
print("Alter: ", alter_str)

# Gleitkommazahlen "float"
hoehe = 180.66 # ist ein float
hoehe_int = int(hoehe) # da wir den float in einer ganzen Zahl sehen wollen wandeln wir den float in ein integer um also machen wir wieder ein Casting.
print("Hoehe: ", hoehe_int)


""" Ausgabe von gemischten Werten !!"""



# append(einzelne Elemente) und extend(mehrere Elemente) sind Funktionen, die es  ermöglicht dynamisch weitere Elemente in eine Liste einzufügen, wobei bei append() nicht mehr als ein Element möglich ist.
# Merke!! append und extend sind Funktionen die hinter einer Variable z.B "zeichen" mit einem Punkt angehängt werden, z.B. "zeichen.extend()".


# Zahlen-, Buchstaben- und Sonderzeichenliste erstellen. In den eckigen Klammern "[]" sind die Elemente z.B. wie in der Variable "zeichen".
zeichen = ["§","✔","%","👍","?","!"] # Buchstaben und Sonderzeichen können nur in einem "" Anführungszeichen platziert werden.
zeichen.extend(["§","$","%","&","?","!"]) # bei extend() müssen die Elemente in eine eckige Klammer.
print("Zeichenliste :", zeichen[0:9]) # in [0:9] dieser Ausgabe werden maximal 9 Elemente aufgelistet, sie ist ein Slicing-Ausdruck.


gemischtewerte = ["$",3,"f","&",7,"j"]
print("gemischte Werte: ", gemischtewerte)

buchstaben = ["hi","mehmet","jo"] 
buchstaben.append("k")
buchstaben.remove("jo")
print("buchstaben: ", buchstaben[0:4]) # buchstaben[0:4] ist ein Slicing-Ausdruck, sie erstellt eine neue Liste die eine Teilmenge der ursprünglichen Liste enthält, wenn die Buchstabenliste aus "buchstaben" wie hier 3 Elemente enthält. Die Elemente werden von links nach rechts aufgezählt sie fängt bei 0 an. Wenn alles ausgegeben werden müssen dann muss [0:3] eingetragen werden. Und wenn ein dynamisches Element aus "append()" mit hinzugefügt werden soll, dann muss einfach nur Anzahl der Elemente in den eckigen Klammern überschritten werden, z.B. von [0:3] zu [0:4.....].


zahlenliste = [1,2,3,4,5,6,7]
zahlenliste.append(7)
zahlenliste.remove(4) # Entfernt eine bestimmte Zahl aus der 
print("Zahlen", zahlenliste[0:7])



""" Heraufinden, wie Lang eine Liste ist """


# Länge der Liste von "zahlenliste" ermitteln mit dem "len"

print("Länge der Zahlenliste: ", len(zahlenliste))


""" Dictonaries in Python: abspeicherung und Werte ändern"""

# Ein Dictonairy ist eine Sammlung von Schlüssel-Wert-Paaren. Jeder Schlüssel ist Einzigartig und wird verwendet um auf einen bestimmten Wert zuzugreifen. Dictonaries sind veränderbar sowohl der Schlüssel und als auch der Wert. 

mein_dictonary = {"name": "Mehmet", "alter": 39} # Erstellung des Dictonary mit dem Namen "mein_dictonary". Sie enthält zwei Schlüsselpaare, "name": "Mehmet". Der Schlüssel "name" ist mit Wert "Mehmet" verknüpft. "alter": 39, der Schlüssel "alter" ist mit dem Wert 39 verknüpft.

print("Name: ", mein_dictonary["name"]) # Hier wird der Wert ausgegeben der mit Schlüssel "name" im Dictonary zugeordnet ist.


# Wert ändern.

mein_dictonary["name"] = "Bob" # Hier wird der Wert "mehmet" vom Schlüssel "name" in mit "Bob" ersetzt. 

print("Name: ", mein_dictonary["name"]) # Hier wird der neue Wert vom Schlüssel "name" ausgegeben.

""" Auf ein Schlüssel(Key) zugreifen der noch nicht existiert """

# Schlüssel hinzufügen z.B. "hobby"

mein_dictonary["hobby"] = "schwimmen"
print("Hobby: ", mein_dictonary["hobby"]) # Weiterer Schlüssel "hobby" wird mit dem Wert Schwimmen ausgegeben.


""" Keyword del(delete) """

# einen Wert löschen.

print("mein_dictonary vor dem Löschen: ", mein_dictonary)
del mein_dictonary["hobby"]
print("mein_dictonary nach dem löschen: ", mein_dictonary)


