import static java.lang.System.out;

public /* public bedeutet das dies ein Öffentlicher Code ist */ class variablen {
    
public static void main(String[] args) {



    int number = 3;
    int number2 = 12;
    int sum = number + number2;
    double number3 = 3.12345; /* Steht für einen wert der true oder false sein kann */
    out.println(sum);
    
    
    /* Variablen in Text Speichern mit "string" */

    String text ="Ich moechte ", apfel = " Aepfel";

    out.println(text + sum + apfel);

    out.println(number3);
    

    }


    
}

// Variablen = Ein wiederverwendbarer Container für einen Wert
    // Eine Variable verhält sich so, als wäre sie der Wert, den sie enthält

    /* Es gibt 2 Arten von Variablen */

    // Primitive = Einfache Werte oder Ganzezahlen, wird in den Speicher gelagert.
    // Referenzierte = Stapelspeicher (Stack) zeigt auf den Speicherhaufen (Heap).

    /* Primitive   vs   Referenzierte
       ------------------------------
       int              string
       double           array
       char             object
       boolean
     */

    /* Stack (Stapelspeicher):

        Funktion:
            Der Stack ist ein Speicherbereich, der für lokale Variablen und Funktionsaufrufe verwendet wird.
            
            Er arbeitet nach dem LIFO-Prinzip (Last-In-First-Out), was bedeutet, dass das zuletzt hinzugefügte Element als erstes entfernt wird.
            
            Er wird vom Betriebssystem automatisch verwaltet.
            
        Speicherung:
        
            Primitive Datentypen (int, float, boolean usw.) werden direkt auf dem Stack gespeichert.
            
            Referenzvariablen (z. B. für Objekte) werden ebenfalls auf dem Stack gespeichert, aber sie speichern nur die Speicheradresse (Referenz) des Objekts, nicht das Objekt selbst.
            
        Lebensdauer:
        
            Variablen auf dem Stack haben eine begrenzte Lebensdauer, die an den Gültigkeitsbereich der Funktion gebunden ist, in der sie deklariert wurden.

            Wenn eine Funktion beendet wird, werden alle ihre lokalen Variablen automatisch vom Stack entfernt.
            
        Heap (Haufenspeicher):
        
            Funktion: 
            
              Der Heap ist ein Speicherbereich, der für dynamisch zugewiesene Objekte verwendet wird.
                
              Er bietet mehr Flexibilität als der Stack, da Objekte zur Laufzeit erstellt und zerstört werden können.
                
              Die Speicherverwaltung auf dem Heap kann manuell (in Sprachen wie C/C++) oder automatisch (in Sprachen wie Java/C#) erfolgen. 
              
            Speicherung:
              Objekte (Instanzen von Klassen, Arrays usw.) werden auf dem Heap gespeichert.

              Die Referenzvariable auf dem Stack enthält die Adresse dieses Objekts im Heap.
              
            Lebensdauer:
              Objekte auf dem Heap können so lange existieren, wie es Referenzen darauf gibt.

              In Sprachen mit automatischer Speicherverwaltung (Garbage Collection) werden Objekte, auf die keine Referenzen mehr verweisen, automatisch freigegeben.

              In Sprachen ohne automatische Speicherverwaltung, ist der Programmierer dazu verpflichtet den Speicher, welcher auf dem Heap reserviert wurde, auch wieder freizugeben.*/

              /* Beispiel */

              class Beispiel {
                public static void main(String[] args) {

                  /* Deklaration */
                    int zahl = 10; // Primitive Variable wird direkt auf dem Stack gepeichert
                    Beispiel objekt = new Beispiel(); // Referenzvariable auf dem Stack, Objekt im Heap, die Adresse des Beispiel-Objekts wir im Heap gespeichert.

                    System.out.printf("Beispiel %d", zahl, objekt);
                }
            }
