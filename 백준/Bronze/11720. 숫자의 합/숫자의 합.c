#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	char x[100];
	scanf("%s", x, sizeof(char) * 100);

	int sum = 0;
	for (int i = 0; i < n; i++) sum += (x[i] - '0');
	printf("%d", sum);
}