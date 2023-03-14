#include "main.h"
#include <stdio.h>

double square(double number)
{
	return number * number;
}

int main()
{
	printf("%f", square(10000000322));
	return (0);
}
