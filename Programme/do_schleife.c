#include <stdio.h>

int main(void)

{
    int anzahl, nummer, nocheiner;
    double preis, rechnung;


    /*Startwerte*/

    nummer = 1;
    rechnung = 0.0;

    /*Bedingte Wiederholungen*/

            do{

                /*Eingabe*/
                printf("Artikel %d, Anzahl: ", nummer);
                scanf("%d", &anzahl);
                printf("Artikel %d, Preis in Euro: ", nummer);
                scanf("%lf", &preis);

                /*Berechnung*/
                rechnung = rechnung + anzahl * preis;

                /*Abfrage*/
                printf("Noch ein Artikel? (Ja=1, Nein=0): ");
                scanf("%d", &nocheiner);

                /*Laufende Nummer erhöhen*/
                nummer = nummer + 1;
            }

while(nocheiner == 1);

/*Ausgabe*/

printf("Summe der Rechnung: %.2f Euro\n", rechnung);

return 0;


}