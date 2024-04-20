#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	short A, B;
	float C;

	cin >> A >> B;
	C = ((A - B) / 3.0) + B;
	cout << setprecision(8) << C;

	return 0;
}
