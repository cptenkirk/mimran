#include <stdio.h>
#include <windows.h>
int main(void)
{
SetConsoleOutputCP(65001);
SetConsoleCP(65001);
system("cls");
printf("\n\n");



/* Schreiben Sie ein Programm das 0 bis 32 aufzählt */





for (int i = 0; i <= 23; i++) /* i ist die Abkürzung für Iteration */
{
    printf("Zahl: %d\n\n", i);
    usleep(100000);
}/*  */



//die Variable i NUR für die Schleife gültig.
// das i++ steht für i ergibt sich aus i + 1 ----> dieser Vorgang heißt inkrementieren/hochzählen.
//bei i++ wird zunächst der Wert der Variablen verwendet und danach wird die Variable hochgezählt (Postinkrement) inkrementierung nach den Variablen.




return 0;
}