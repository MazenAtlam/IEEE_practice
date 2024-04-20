#include <iostream>

using namespace std;

int str_length(string str) {
	int i, len = 0;

	for (i = 0; str[i] != '\0'; i++)
		len++;

	return len;
}

bool strcmp(string s1, string s2) {
	int i;

	if (str_length(s1) != str_length(s2))
		return false;

	for (i = 0; s1[i] != '\0'; i++) {
		if (s1[i] != s2[i])
			return false;
	}
	return true;
}

int main() {
	string S[] = {"H", "2B", "3B", "HR"};
	string str[4];
	string temp;
	int i, j, k, exist = 0;
	bool matched;

	for (i = 0; i < 4; i++)
		cin >> str[i];

	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4 - exist; j++) {
			matched = strcmp(S[j], str[i]);
			if (matched) {
				for (k = j; k < 3 - exist; k++) {
					temp = S[k + 1];
					S[k + 1] = S[k];
					S[k] = temp;
				}
				exist++;
				break;
			}
		}
		if (!matched) {
			cout << "No" << endl;
			return 0;
		}
	}
	cout << "Yes" << endl;

	return 0;
}
