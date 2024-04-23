#include <iostream>

using namespace std;

int main() {
	int x[5];
	int i;

	for (i = 0; i < 5; i++)
		cin >> x[i];

	for (i = 0; i < 5; i++)
		if (x[i] == 0) {
			cout << i + 1;

			return 0;
		}
	return 0;
}
