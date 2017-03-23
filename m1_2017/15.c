#include <stdio.h>
#include <stdlib.h>


int main()
{
    int i=0,t=0;
    char c[1000];
    char b[1000];
    gets(c);
    for(i=0;c[i]!='\0';++i){
        if(c[i]==c[i+1]){
            i=i+1;

        }
        else{
            t=i;

            printf("%c", c[t]);
            t=t+1;

        }

    }
    return 0;
}
