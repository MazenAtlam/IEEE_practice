#include <iostream>

using namespace std;

int max(int n1, int n2) {
	if (n1 > n2)
		return n1;
	else
		return n2;
}

int main() {
	int num[2];
	int sum[] = {0, 0};
	int i, largest;

	for (i = 0; i < 2; i++)
		cin >> num[i];

	for (i = 0; i < 2; i++) {
		while (num[i] != 0) {
			sum[i] += num[i] % 10;
			num[i] /= 10;
		}
	}
	largest = max(sum[0], sum[1]);
	cout << largest;

	return 0;
}
