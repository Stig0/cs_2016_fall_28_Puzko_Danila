#include <stdio.h>
#include <string.h>


int main (void)
{
    int n=0;
    

   char a[1000];
   char c[1000];
   printf("Vvedi stroku a:");
   gets(a);


   printf("Vvedi c:");
   gets(c);

   printf("Vvedi n:");
   scanf("%i", &n);
   if (strncmp (a,c,n)==0){
      printf("%i pervyh elementov ravny", n);
      }
      else{
      printf("%i pervyh elementov ne ravny\n", n);
      }


   strncpy (a,c,n);

   printf("%s\n", a);


   strncat(c,a,n);
   printf("Stroka c s skopirovannymi %i simvolami iz tekuschey stroki a:\n%s", n, c);
   
   return 0;
}
