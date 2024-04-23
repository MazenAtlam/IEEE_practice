#include <iostream>

using namespace std;

int main() {
	int K, X, coins;

	cin >> K >> X;

	coins = K * 500;
	if (coins < X)
		cout << "No" << endl;
	else
		cout << "Yes" << endl;

	return 0;
}
