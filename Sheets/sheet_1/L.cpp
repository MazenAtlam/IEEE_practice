#include <iostream>

using namespace std;

int main() {
	char vowel[] = {'a', 'e', 'i', 'o', 'u'};
	int i;
	char c;

	cin >> c;

	for (i = 0; i < 5; i++) {
		if (c == vowel[i]) {
			cout << "vowel" << endl;
			return 0;
		}
	}
	cout << "consonant" << endl;

	return 0;
}
