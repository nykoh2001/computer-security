#include <stdio.h>

int main() {
	int password = 123;
	int input = 456;

	if (input != password)
		printf("Log in Failure\n");
	else
		printf("Log in Success\n");
	return 0;
}
