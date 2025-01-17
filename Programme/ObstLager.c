#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    /* Deklaration Apfel */

    int qtyApfel = 677;
    double kgPreis = 1.99;

    /* Zuweisung */

    qtyApfel = 677;
    kgPreis = 1.99;

    /* Ausgabe */

    printf("Auswahl 1\n");
    printf("Rote Aepfel aus dem Heimat!\n\n\n");
    printf("Quantitaet: %d\n", qtyApfel);
    printf("Kg Preis: %.2f Euro\n\n\n", kgPreis);

    /* Deklaration Orangen */

    int qtyOrange = 487;
    double kgPreisO = 2.99;

    /* Zuweisung */

    qtyOrange = 487;
    kgPreis = 2.99;

    /* Deklaration Trauben */

    int qtyTrauben = 377;
    double kgPreisT = 4.99;

    /* Zuweisung */

    qtyTrauben = 377;
    kgPreis = 4.99;

    /* Deklaration Mandarinen */

    int qtyMandarinen = 266;
    double kgPreisM = 3.99;


    /* Zuweisung */

    qtyMandarinen = 266;
    kgPreis = 3.99;

    /* Ausgabe */


    printf("Auswahl 2\n");
    printf("Orangen aus Spanien\n\n\n");
    printf("Quantitaet: %d\n", qtyOrange);
    printf("Kg Preis: %.2f Euro\n\n\n", kgPreisO);

    printf("Auswahl 3\n");
    printf("Trauben verschiedene Sorten\n\n\n");
    printf("Quantitaet: %d\n", qtyTrauben);
    printf("Kg Preis: %.2f Euro\n\n\n", kgPreisT);

    printf("Auswahl 4\n");
    printf("Mandarinen aus Tuerkei\n\n\n");
    printf("Quantitaet: %d\n", qtyMandarinen);
    printf("Kg Preis: %.2f Euro\n\n\n", kgPreisM);

    scanf("Produkt auswaehlen: ");



    return 0;

}
