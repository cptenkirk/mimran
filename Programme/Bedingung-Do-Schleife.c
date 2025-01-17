/* Ergänzen Sie das Programm so, das die Abgefragte Ganzzahl im Wertbereich von 0 bis kleiner als 10 liegt. */


#include <stdio.h>
#include <windows.h>
int main(void)
{
SetConsoleOutputCP(65001);
SetConsoleCP(65001);
system("cls");
printf("\n\n");


int wert = -1, counter = 0;



while (wert>=10||wert<=0)
{
    
printf("Geben Sie einen Wert von 0-9 ein!:  ");
scanf("%d", &wert);
fflush(stdin);

counter = counter + 1; // hier werden Versuche gezählt

if (counter == 3)
{

    printf("Maximale versuche Erreicht\n\n");
      return 0;        //Programmabbruch
}


} 
// der Schleifenkörper wird ausgeführt, wenn eine der beiden Bedingungen ein True liefert.
printf("Eingabe erfolgreich.....Ende \n\n");






return 0;
}