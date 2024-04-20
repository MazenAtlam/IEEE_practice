#include <iostream>

using namespace std;

int main() {
	int X, remain;

	cin >> X;

	if (X >= 90) {
		cout << "expert" << endl;

		return 0;
	}
	if (X >= 70)
		remain = 90 - X;
	else if (X >= 40)
		remain = 70 - X;
	else
		remain = 40 - X;

	cout << remain << endl;

	return 0;
}
