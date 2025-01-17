#include <stdio.h>
#include <windows.h>
int main(void)
{
SetConsoleOutputCP(65001);
SetConsoleCP(65001);
system("cls");
printf("\n\n");


int raum;
float breit, lang;


printf("Geben Sie die Anzahl der Räume: ");
scanf("%d", &raum);
fflush(stdin);




for (float i = 0; i < raum; i++)
{




printf("\n\nGeben sie die Breite des Raumes ein: ");
scanf("%f", &breit);
fflush(stdin);

printf("\n\nGeben sie die Länge des Raumes ein: ");
scanf("%f", &lang);
fflush(stdin);


}






printf("\n\n ihr Raum hat die größe %.2f m2", lang * breit * raum);





















printf("\n\n");


return 0;
}