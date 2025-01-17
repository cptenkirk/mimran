#include <stdio.h>
#include <unistd.h>

int main()

{
    int anzahl;
    double preis = 1.45, summe;

    
    
    printf("\n\nTabellenformatierung mit der for-Schleife\n\n");
    printf("Uebungsaufgabe 5.5 Seite 58, weiter mit der EnterTaste\n\n");
    scanf("break");
    
    printf("Anzahl          Preis\n");
    
    for(anzahl = 1; anzahl <=10; anzahl ++)

    {
        summe = anzahl * preis;

        printf("%5d%15.2f Euro\n", anzahl, summe);
        sleep(1);


    }

    sleep(1);
    printf("\n\n Ende der Formatierung\n\n");

return 0;

}