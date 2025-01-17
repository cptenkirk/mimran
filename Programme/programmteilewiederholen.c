#include <stdio.h>

int main(void)

{

int anzahl, nummer, nocheiner;
double preis, rechnung;

/* Startwert */

rechnung = 0.0;

/* regelmäßige Wiederholung */

for(nummer = 1; nummer < 4; nummer = nummer + 1)

    {
    /* Eingabe */
    printf("Artikel %d, anzahl: ", nummer);
    scanf("%d", &anzahl);

    printf("Artikel %d, preis in Euro: ", nummer);
    scanf("%lf", &preis);

    /*Berechnung*/

    rechnung = rechnung + anzahl * preis;


    }

    /*Ausgabe*/

    printf("Summe der Rechnung : %.2f Euro\n", rechnung);
    printf("weitere Artikel hinzufügen? (Ja=1, Nein=0)");
    scanf("%d", &nocheiner);

    while(nocheiner == 1);

    return 0;

}