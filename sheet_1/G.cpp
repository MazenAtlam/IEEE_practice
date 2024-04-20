#include <iostream>

using namespace std;

int main() {
	short m, remaining_hours = 24;

	cin >> m;
	remaining_hours += 24 - m;
	cout << remaining_hours;

	return 0;
}
