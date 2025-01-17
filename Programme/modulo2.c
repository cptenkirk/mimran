#include <stdio.h>
#include <windows.h>
int main(void)
{
SetConsoleOutputCP(65001);
SetConsoleCP(65001);
system("cls");
printf("\n\n");



int a, b;

while (TRUE)
{

    printf("geben Sie den Wert a ein:     \n\n");
    scanf("%d", &a);
    fflush(stdin);


    printf("geben Sie den Wert b ein:      \n\n");
    scanf("%d", &b);
    fflush(stdin);

if (b == 0) return 0;


    printf("%d / %d ergibt %d, Rest ist %d\n\n", a, b, a/b, a%b);

}


return 0;
}