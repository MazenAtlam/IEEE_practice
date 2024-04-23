#include <iostream>

using namespace std;

void swap(short* x, short* y) {
	short temp;

	if (*(x) != *(y)) {
		temp = *(x);
		*(x) = *(y);
		*(y) = temp;
	}
}

int main() {
	short num[3], i;

	for (i = 0; i < 3; i++) {
		cin >> num[i];
	}

	swap(num, num + 1);
	swap(num, num + 2);

	for (i = 0; i < 3; i++) {
		cout << num[i];
		if (i != 2)
			cout << " ";
	}

	return 0;
}
