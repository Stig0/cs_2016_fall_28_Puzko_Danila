#include <stdio.h>
#include <stdlib.h>

void reverse(char s[], int n)
{
    char t[1000];
    int i, j;
    for(i=0; i<n; i++){
        t[i]=s[i];
    }
    i=i-2;
    for(j=0; j<n-1; j++, i--){
        s[j]=t[i];
    }
}

int main()
{

    char l[1000];
    int i, m;
    char c;
    i=0;
    while((c=getchar())!='\0')
    {
        l[i]=c;
        i++;
        if(c=='\n')
        {
            l[i]='\0';
            m=i;
            i=0;
            reverse(l, m);
            printf("%s\n", l);
        }
    }
    return 0;
}
