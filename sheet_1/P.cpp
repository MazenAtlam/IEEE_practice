#include <iostream>

using namespace std;

int max(int x, int y, int z) {
	if (x >= y && x >= z)
		return x;
	if (y >= z && y >= x)
		return y;
	return z;
}

int main() {
	int A, B, largest;

	cin >> A >> B;

	largest = max((A + B), (A - B), (A * B)); 

	cout << largest << endl;

	return 0;
}
