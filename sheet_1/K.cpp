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
	string s;

	cin >> s;

	if (strcmp(s, "Hello,World!"))
		cout << "AC" << endl;
	else
		cout << "WA" << endl;

	return 0;
}
