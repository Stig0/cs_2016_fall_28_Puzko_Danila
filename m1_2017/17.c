#include <stdio.h>

double delta(double *mas, int a)
{
	double d, e;
	int i=0;
	d=mas[0];
	for (i = 0; i < a; ++i)
	{
		if (d<mas[i]){
			d=mas[i];
		}
	}
	e=mas[0];
	for (i = 0; i < a; ++i)
	{
		if (e>mas[i]){
			e=mas[i];
		}
	}
	return d - e;
}

int main()
{
	int a, i;
	double d;
	printf("Kolichestvo simvolov:");
	scanf("%i", &a);
	double *mas = (double*)malloc(a*8);
	printf("Massiv: ");
	for (i = 0; i < a; ++i){
		scanf("%lf", &mas[i]);
	}
	d=delta(mas, a);
	printf("Max - min=%lf\n", d);
	free(mas);
	return 0;
}
