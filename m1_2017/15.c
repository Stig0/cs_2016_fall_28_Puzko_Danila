#include <stdio.h>
#include <string.h>

int main()
{
    int i=0, k=0;
    char c[1000],b[1000];
    printf("Vvedite stroku:");
    gets(c);
    b[0]=c[0];
    for(i=0;c[i]!='\0';i++)
        { if(b[k-1]!=c[i])
            {
                b[k]=c[i];
                printf("%c",b[k]);
                k++;
             }
        }
    return 0;
}
