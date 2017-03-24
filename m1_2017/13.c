#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i=0;
    char c[10000];
    printf("Vvedite stroku:\n");
    gets(c);
    for(i=0;c[i]!='\0';++i){
        if(c[i]!=' '){
            printf("-");
        }
        else{
            printf("\n");
        }

        }
    return 0;
}
