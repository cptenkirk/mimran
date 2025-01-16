#include <stdio.h>
#include <string.h>
#include <time.h>
#include <windows.h>
#define MAX_Products 4
#define MAX_NAME_LENGTH 50
 struct produkt{
    char name[MAX_NAME_LENGTH];
    double preis;

};

int main(void)


{
    
SetConsoleOutputCP(65001);
SetConsoleCP(65001);
system("cls");
    
    struct produkt produkt[MAX_Products]; 



    
 
    strcpy(produkt[0].name, "4k Widescreen Gaming Display 1000hz");
    produkt[0].preis = 4999.00;

    strcpy(produkt[1].name, "CPU mit 128 Kerne");
    produkt[1].preis = 17999.00;

    strcpy(produkt[2].name, "GPU 24 GB RAM");
    produkt[2].preis = 2999.00;

    strcpy(produkt[3].name, "Einkaufsbeutel");
    produkt[3].preis = 0.90;
    
    int auswahl, menge = 0;
    double gesamtpreis = 0.0;
    int once = 0;
    int usleep();
    
    
     do {
        printf("\n\nWillkommen im Hardwareshop!\n");
        usleep(500000);
        printf("\n\nBitte waehle eine Produkt aus, gib dafür 1, 2, 3 oder 4 ein:\n\n");
        usleep(500000);
        for (int i = 0; i < MAX_Products; i++) {
            printf("%d. %s %.2f €\n", i + 1, produkt[i].name, produkt[i].preis);
            usleep(200000);
        }

     printf("\n\n\nIhr Wahl: ");

    if (scanf("%d", &auswahl) == 1 && auswahl >= 1 && auswahl <= MAX_Products) {usleep(500000);
        printf("\n\nAnzahl eingeben: ");
        scanf("%d", &menge);
        gesamtpreis += produkt[auswahl - 1].preis * menge; usleep(500000);
        printf("\n\nDas macht dann %.2f €", gesamtpreis);
    } 
    
    else if (auswahl == MAX_Products + 1) {
        break;
    } 
    
    
    else {

        usleep(500000);
        printf("\n\nUngueltige Eingabe\n");
    }
} while (once == 1);
    
    usleep(500000);
    printf("\n\nAuf Wiedersehen :)");
    
return 0;


    
        
    
    
}
