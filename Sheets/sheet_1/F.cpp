#include <iostream>

using namespace std;

int main() {
	short num[2];
	short i, fare;

	for (i = 0; i < 2; i++)
		cin >> num[i];
	fare = num[0] + num[1] / 2.0;
	cout << fare;

	return 0;
}
