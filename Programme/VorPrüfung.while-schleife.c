#include <stdio.h>
#include <stdlib.h>
int main (void)

{
    int anzahl, nummer, nochEiner;
    double preis, summeRechnung;

    /* Startwete */

    nummer = 0;
    summeRechnung = 0.0;

    /* Abfrage */

    printf("Wollen Sie Artikel eingeben? (Ja=1, Nein=0): ");
    scanf("%d", &nochEiner);

    /* Bedingte Wiederholung, Pr�fung vorher */

  while(nochEiner == 1)
    {
        /* Laufende Nummer erh�hen */
        nummer = nummer + 1;

        /* Eingabe */

        printf("Artikel %d, Anzahl: ", nummer);
        scanf("%d", &anzahl);
        printf("Artikel %d, Preis in Euro: ", nummer);
        scanf("%lf", &preis);

        /* Berechnung */

        summeRechnung = summeRechnung + anzahl * preis;

        /* Abfrage */

        printf("Noch ein Artikel? (Ja=1, Nein=0): ");
        scanf("%d", &nochEiner);


    }


         /*Ausgabe*/

    if(nummer == 0)
        printf("Keine Eingabe\n");

    else
        printf("Summe der Rechnung: %.2f Euro\n", summeRechnung);

    return 0;
}
