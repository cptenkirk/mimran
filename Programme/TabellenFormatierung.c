#include<stdio.h>
#include<stdlib.h>

int main()

{
    int anzahlApfel = 12, anzahlRadio = 2;
    double preisApfel = 1.45, preisRadio = 109.95;

    /* Ausgabe f�r Tabelle von gasnzen Zahlen, teilweise mit f�hrenden Nullen */

    printf("Anzahl\n");
    printf("%6d\n", anzahlApfel);

    // mit der %6d wird mit mindestbreite von 6 Zeichen formatieren, z.B. sechsmal mit Leerzeichen.

    printf("%06d\n", anzahlRadio);

    // das Format %06d f�hrt dazu das f�hrende Nullen ausgegeben werden.

    /*Ausgabe f�r Tabelle von Zahlen mit Nachkommastellen*/

    printf("\nPreis\n");
    printf("%8.2f Euro\n", preisApfel);
    // mit %8.2f wird mit einer mindestbreite von 8 Zeichen gearbeitet.
    printf("%8.2f Euro\n", preisRadio);

    return 0;


}
