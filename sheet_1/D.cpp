#include <iostream>

using namespace std;

short dice[] = {1, 2, 3, 4, 5, 6};

short get_bottom_face(short x) {
	short i;

	for (i = 0; i < 6; i++) {
		if (x == dice[i]) {
			return dice[5 - i];
		}
	}
}

int main() {
	short top_face[3];
	short i, sum = 0;

	cin >> top_face[0] >> top_face[1] >> top_face[2];
	for (i = 0; i < 3; i++) {
		sum += get_bottom_face(top_face[i]);
	}
	cout << sum << endl;

	return 0;
}
