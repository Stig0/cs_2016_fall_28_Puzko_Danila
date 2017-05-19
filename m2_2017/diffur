#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float func(float x)
{
	return x*x;
}

int main()
{
	float h = 0.0, x = 0.0, p = 0.0, a=0.0, b=0.0, p1=0.0, p2=0.0;
	printf("Enter low:");
	scanf("%f", &a);
	printf("Enter high:");
	scanf("%f", &b);
	printf("Enter step:");
	scanf("%f", &h);
	x = a;
	p1 = ((-3) * func(x) + 4 * (func(x+h)) - (func(x+2*h)))/(2*h);
	p2 = (1 / (2 * h))*(-func(x) + func(x + 2 * h));
	printf("%f\n", p1);
	printf("%f\n", p2);
	while (x+2*h <= b)
	{
		p = (1 / (2 * h))*(func(x) - 4 * (func(x + h))+3*(func(x+2*h)));
		x = x + h;
		printf("%f\n", p);
	}

	return 0;
}
